import re
import polib
import glob
import requests

from pathlib import Path


def get_progress(pofile: polib.POFile) -> float:
    '''
    Check the po file with how many entries are translated or not.
    '''

    lines_tranlated = len(pofile.translated_entries())
    lines_untranlated = len(pofile.untranslated_entries())

    # if lines_tranlated == 0:
    #     result = "❌"
    # elif lines_untranlated == 0:
    #     result = "✅"
    # else:
    lines_all = lines_tranlated + lines_untranlated
    progress = lines_tranlated / lines_all
    progress_percentage = round(progress * 100, 2)
    return progress_percentage


def get_open_issues_count() -> int:
    '''
    Fetch GitHub API to get the number of OPEN ISSUES.
    '''

    url = f"https://api.github.com/search/issues?q=repo:python/python-docs-zh-tw+type:issue+state:open"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    r = requests.get(url=url, headers=headers)
    result = r.json()

    return result["total_count"]


def get_github_issues() -> list:
    '''
    Fetch GitHub API to collect the infomation of OPEN ISSUES,
    including issue title and assignee.

    Steps:
    1. Fetch GitHub API and get open issue list
    2. Filter the issue if it have no "Translate" in the title
    3. Filter the issue if it have no correct filepath in the title

    Expected Output:
    [ ((dirname, filename), assignee_id, issue_url), ... ]
    '''
    NUMBER_OF_ISSUES = get_open_issues_count()

    url = f"https://api.github.com/search/issues?q=repo:python/python-docs-zh-tw+type:issue+state:open&per_page={NUMBER_OF_ISSUES}"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    r = requests.get(url=url, headers=headers)
    result = r.json()

    result_list = []
    for issue in result["items"]:
        assignee = issue["assignee"]["login"] if issue["assignee"] else ""

        title = issue["title"]
        if "翻譯" not in title and "translate" not in title.lower():
            continue

        match = re.search(
            "(?P<dirname>[^\s`][a-zA-z-]+)/(?P<filename>[a-zA-Z0-9._-]+(.po)?)", title)
        if not match:
            continue

        dirname, filename = match.group('dirname', 'filename')
        if not filename.endswith('.po'):
            filename += '.po'

        result_list.append(((dirname, filename), assignee, issue["html_url"]))

    return result_list


def format_line_table_header() -> list:
    return [f"|Filename|Progress|Issue|Assignee|\r\n",
            f"|-------:|:-------|:----|:-------|\r\n"]


def format_line_po_issue_display(issue_link: str, issue_number: str, progress: float, create_issue_link: str) -> str:
    if issue_link:
        return f"[{issue_number}]({issue_link})"
    if progress != 100.:
        return f"[create issue]({create_issue_link})"
    return ""


def format_line_po(filename: str, po_link: str, progress: str, issue_display: str, assignee: str) -> str:
    progress_display = f"{progress} %"
    if progress == 0:
        progress_display = "❌"
    elif progress == 100:
        progress_display = "✅"
    return f"|[`{filename}`]({po_link})|{progress_display}|{issue_display}|{assignee}|\r\n"


def format_line_directory(dirname: str) -> str:
    return f"## {dirname}\r\n"


if __name__ == "__main__":
    issue_list = get_github_issues()

    '''
    Search all the po file in the directory,
    and record the translation progress of each files.
    '''
    BASE_DIR = Path("../")
    summary = {}
    for filepath in glob.glob(str(BASE_DIR / "**/*.po"), recursive=True):
        path = Path(filepath)
        filename = path.name
        dirname = path.parent.name if path.parent.name != BASE_DIR.name else '/'
        po = polib.pofile(filepath)

        summary.setdefault(dirname, {})[filename] = {
            'progress': get_progress(po),
            'issue': '',
            'assignee': '',
        }

    '''
    Unpack the open issue list, and add assignee after the progress
    '''
    for (category, filename), assignee, issue_url in issue_list:
        try:
            summary[category][filename]['issue'] = issue_url
            summary[category][filename]['assignee'] = assignee
        except KeyError:
            pass

    '''
    Adding Space for Formatting Markdown Link
    '''

    '''
    Format the lines that will write into the markdown file,
    also sort the directory name and file name.
    '''
    writeliner = []
    summary_sorted = dict(sorted(summary.items()))
    for dirname, filedict in summary_sorted.items():
        writeliner.append(format_line_directory(dirname))
        writeliner.extend(format_line_table_header())

        filedict_sorted = dict(sorted(filedict.items()))
        for filename, filedata in filedict_sorted.items():
            file_path = f"{dirname}/{filename}" if dirname else filename
            po_link = f"https://github.com/python/python-docs-zh-tw/tree/3.13/{file_path}"
            issue_link = filedata['issue']
            issue_number = f"#{issue_link.split('/')[-1]}"
            create_issue_link = f"https://github.com/python/python-docs-zh-tw/issues/new?title=Translate%20`{file_path}`"
            issue_display = format_line_po_issue_display(issue_link, issue_number, filedata['progress'], create_issue_link)
            line_po = format_line_po(filename, po_link, filedata['progress'], issue_display, filedata['assignee'])
            writeliner.append(line_po)

    with open(
        f"summarize_progress/result.md",
        "w",
    ) as file:
        file.writelines(writeliner)
