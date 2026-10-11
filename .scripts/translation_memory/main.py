"""Translation memory lookup over this repo's .po files via agentic-retrieval.

Usage (run from anywhere; the repo root is always the index root)::

    .scripts/translation_memory.sh index [--force]
    .scripts/translation_memory.sh query "<text>" [--top-k N] [--fetch N]
        [--include-fuzzy] [--include-untranslated] [--json] [--max-chars N]

Engine resolution:

1. ``AGENTIC_RETRIEVAL_ENGINE`` = path to an agentic-retrieval ``engine``
   directory (needs ``uv``); run with ``uv run --frozen``.
2. Otherwise a ``retrieval`` executable on ``PATH``.
3. Otherwise exit with status 3.

The index lives in ``.agentic-retrieval/`` (gitignored). ``query`` always runs
``index`` first so the cjk tokenizer is guaranteed; a fresh index is a cheap
no-op. Exit codes: 0 ok, 2 usage error, 3 engine unavailable or failed.
Supports macOS and Linux only.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Dict, List

REPO_ROOT = Path(__file__).resolve().parents[2]
ENV_VAR = "AGENTIC_RETRIEVAL_ENGINE"
EXIT_UNAVAILABLE = 3


def fail(message: str) -> None:
    print(f"translation-memory: {message}", file=sys.stderr)
    sys.exit(EXIT_UNAVAILABLE)


def resolve_engine_cmd() -> List[str]:
    engine = os.environ.get(ENV_VAR)
    if engine:
        if not (Path(engine) / "pyproject.toml").is_file():
            fail(
                f"{ENV_VAR}={engine} is not an agentic-retrieval engine "
                "directory (no pyproject.toml)"
            )
        if not shutil.which("uv"):
            fail(
                "'uv' not found on PATH (needed to run the engine from "
                f"{ENV_VAR})"
            )
        return ["uv", "run", "--frozen", "--quiet", "--directory", engine,
                "retrieval"]
    found = shutil.which("retrieval")
    if found:
        return [found]
    fail(
        "agentic-retrieval engine not found. Either\n"
        f"  export {ENV_VAR}=/path/to/agentic-retrieval/engine\n"
        "or install it so that 'retrieval' is on PATH."
    )
    return []  # unreachable


def run_engine(engine_cmd: List[str], args: List[str]) -> str:
    try:
        proc = subprocess.run(
            engine_cmd + args, capture_output=True, encoding="utf-8"
        )
    except OSError as exc:
        fail(f"cannot run engine: {exc}")
    if proc.returncode != 0:
        sys.stderr.write(proc.stdout or "")
        sys.stderr.write(proc.stderr or "")
        fail(f"engine exited with status {proc.returncode}")
    return proc.stdout


def run_index(engine_cmd: List[str], force: bool) -> None:
    args = ["index", "--root", str(REPO_ROOT), "--retriever", "lexical",
            "--tokenizer", "cjk"]
    if force:
        args.append("--force")
    out = run_engine(engine_cmd, args)
    if out.strip():
        sys.stderr.write(out)


def cmd_index(args: argparse.Namespace) -> int:
    start = time.monotonic()
    run_index(resolve_engine_cmd(), args.force)
    print(
        f"translation-memory: index ready in {time.monotonic() - start:.1f}s",
        file=sys.stderr,
    )
    return 0


def keep_hit(meta: Dict[str, Any], args: argparse.Namespace) -> bool:
    if meta.get("kind") != "po_entry":
        return False
    if not args.include_untranslated and not meta.get("translated"):
        return False
    if not args.include_fuzzy and meta.get("fuzzy"):
        return False
    return True


def collect_entries(
    hits: List[Dict[str, Any]], args: argparse.Namespace
) -> List[Dict[str, Any]]:
    entries: List[Dict[str, Any]] = []
    seen = set()
    for hit in hits:
        meta = hit.get("metadata") or {}
        if not keep_hit(meta, args):
            continue
        key = (meta.get("msgid"), meta.get("msgstr"))
        if key in seen:
            continue
        seen.add(key)
        path = hit.get("path", "")
        if os.path.isabs(path):
            path = os.path.relpath(path, REPO_ROOT)
        entry = {
            "path": path,
            "line": meta.get("line"),
            "msgid": meta.get("msgid", ""),
            "msgstr": meta.get("msgstr", ""),
            "fuzzy": bool(meta.get("fuzzy")),
            "translated": bool(meta.get("translated")),
            "references": meta.get("references") or [],
        }
        if meta.get("msgctxt"):
            entry["msgctxt"] = meta["msgctxt"]
        entries.append(entry)
        if len(entries) >= args.top_k:
            break
    return entries


def compact(text: str, max_chars: int) -> str:
    text = " ".join(str(text).split())
    if max_chars and len(text) > max_chars:
        return text[:max_chars].rstrip() + "..."
    return text


def format_entry(entry: Dict[str, Any], max_chars: int) -> str:
    header = f"{entry['path']}:{entry['line']}"
    if entry["fuzzy"]:
        header += "  [fuzzy]"
    if not entry["translated"]:
        header += "  [untranslated]"
    lines = [header]
    if "msgctxt" in entry:
        lines.append(f"  msgctxt: {compact(entry['msgctxt'], max_chars)}")
    lines.append(f"  msgid: {compact(entry['msgid'], max_chars)}")
    lines.append(f"  msgstr: {compact(entry['msgstr'], max_chars)}")
    return "\n".join(lines)


def cmd_query(args: argparse.Namespace) -> int:
    engine_cmd = resolve_engine_cmd()
    run_index(engine_cmd, False)
    fetch = args.fetch or max(3 * args.top_k, 20)
    out = run_engine(
        engine_cmd,
        ["query", args.text, "--root", str(REPO_ROOT), "--retriever",
         "lexical", "--top-k", str(fetch), "--json", "--stale-ok"],
    )
    try:
        hits = json.loads(out).get("results", [])
    except ValueError as exc:
        fail(f"engine returned invalid JSON: {exc}")
    entries = collect_entries(hits, args)
    if args.json:
        print(json.dumps(entries, ensure_ascii=False, indent=2))
    elif entries:
        print("\n\n".join(format_entry(e, args.max_chars) for e in entries))
    if not entries:
        print("translation-memory: no matching translated entries",
              file=sys.stderr)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Translation memory over this repo's .po files."
    )
    sub = parser.add_subparsers(dest="command", required=True)
    p_index = sub.add_parser("index", help="build or refresh the index")
    p_index.add_argument("--force", action="store_true")
    p_index.set_defaults(func=cmd_index)
    p_query = sub.add_parser("query", help="find similar translated entries")
    p_query.add_argument("text")
    p_query.add_argument("--top-k", type=int, default=5)
    p_query.add_argument("--fetch", type=int, default=0,
                         help="hits to fetch before filtering "
                              "(default max(3*top-k, 20))")
    p_query.add_argument("--include-fuzzy", action="store_true")
    p_query.add_argument("--include-untranslated", action="store_true")
    p_query.add_argument("--json", action="store_true")
    p_query.add_argument("--max-chars", type=int, default=300,
                         help="truncate each field (0 = no truncation)")
    p_query.set_defaults(func=cmd_query)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
