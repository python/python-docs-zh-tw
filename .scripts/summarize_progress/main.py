import re
import polib
import glob
import datetime
import requests

from pathlib import Path


def entry_check(pofile: polib.POFile) -> str:
    '''
    Check the po file with how many entries are translated or not.
    '''

    lines_tranlated = len(pofile.translated_entries())
    lines_untranlated = len(pofile.untranslated_entries())

    if lines_tranlated == 0:
        result = "❌"
    elif lines_untranlated == 0:
        result = "✅"
    else:
        lines_all = lines_tranlated + lines_untranlated
        progress = lines_tranlated / lines_all
        progress_percentage = round(progress * 100, 2)
        result = f"Ongoing, {progress_percentage} %"

    return result


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
    2. Filter the issue if it have no assignee
    3. Filter the issue if it have no "Translate" in the title
    4. Filter the issue if it have no correct filepath in the title
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
        if issue["assignee"] is None:
            continue

        title = issue["title"]
        if "翻譯" not in title and "translate" not in title.lower():
            continue

        match = re.search("(?P<dirname>[^\s`][a-zA-z-]+)/(?P<filename>[a-zA-Z0-9._-]+(.po)?)", title)
        if not match:
            continue
        
        dirname, filename = match.group('dirname', 'filename')
        if not filename.endswith('.po'):
            filename += '.po'

        result_list.append(((dirname, filename), issue["assignee"]["login"]))

    return result_list

def format_line_file(filename: str, result: str) -> str:
    return f"  - {filename.ljust(37, '-')}{result}\r\n"


def format_line_directory(dirname: str) -> str:
    return f"- {dirname}/\r\n"


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
        summary.setdefault(dirname, {})[filename] = entry_check(po)

    '''
    Unpack the open issue list, and add assignee after the progress
    '''
    for (category, filename), assignee in issue_list:
        try:
            summary[category][filename] += f", 💻 {assignee}"
        except KeyError:
            pass

    '''
    Format the lines that will write into the markdown file,
    also sort the directory name and file name.
    '''
    writeliner = []
    summary_sorted = dict(sorted(summary.items()))
    for dirname, filedict in summary_sorted.items():
        writeliner.append(format_line_directory(dirname))
        filedict_sorted = dict(sorted(filedict.items()))
        for filename, result in filedict_sorted.items():
            writeliner.append(format_line_file(filename, result))

    with open(
        f"summarize_progress/dist/summarize_progress.md",
        "w",
    ) as file:
        file.writelines(writeliner)
