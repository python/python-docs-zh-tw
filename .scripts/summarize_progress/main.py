import re
import polib
import glob
import requests

from pathlib import Path

MAX_FILENAME_LEN = 0
MAX_PROGRESS_LEN = 10
MAX_ISSUE_LEN = 10
MAX_ASSIGNEE_LEN = 0


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
        result = f"{progress_percentage} %"

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
        assignee = issue["assignee"]["login"] if issue["assignee"] is not None else ""

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
    global MAX_ASSIGNEE_LEN, MAX_FILENAME_LEN, MAX_PROGRESS_LEN, MAX_ISSUE_LEN
    return [f"|{'Filename'.ljust(MAX_FILENAME_LEN, ' ')}|{'Progress'.ljust(MAX_PROGRESS_LEN,' ')}|{'Issue'.ljust(MAX_ISSUE_LEN,' ')}|{'Assignee'.ljust(MAX_ASSIGNEE_LEN,' ')}|\r\n",
            f"|{':'.rjust(MAX_FILENAME_LEN, '-')}|{':'.ljust(MAX_PROGRESS_LEN,'-')}|{':'.ljust(MAX_ISSUE_LEN,'-')}|{':'.ljust(MAX_ASSIGNEE_LEN,'-')}|\r\n"]

def format_issue_link(url: str) -> str:
    return f"[{url.split('/')[-1]}]({url})" if len(url) > 0 else ''

def format_line_file(data: dict) -> str:
    global MAX_ASSIGNEE_LEN, MAX_FILENAME_LEN, MAX_PROGRESS_LEN, MAX_ISSUE_LEN

    filename_split = list(data['filename'])
    # Adding \\ to avoid Markdown rendering bold font
    if '_' in filename_split:
        add_index = [index for index, chac in enumerate(filename_split) if chac == "_"]
        add_index.sort(reverse=True)
        for index in add_index:
            filename_split.insert(index, '\\')

    filename = ''.join(filename_split)

    return f"|{filename.rjust(MAX_FILENAME_LEN, ' ')}|{data['progress'].ljust(MAX_PROGRESS_LEN, ' ')}|{format_issue_link(data['issue']).ljust(MAX_ISSUE_LEN, ' ')}|{data['assignee'].ljust(MAX_ASSIGNEE_LEN, ' ')}|\r\n"


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

        MAX_FILENAME_LEN = len(filename) if len(
            filename) > MAX_FILENAME_LEN else MAX_FILENAME_LEN
        
        summary.setdefault(dirname, []).append({
            'filename': filename,
            'progress': entry_check(po),
            'issue': '',
            'assignee': '',
        })

    '''
    Unpack the open issue list, and add assignee after the progress
    '''
    for (category, filename), assignee, issue_url in issue_list:
        try:
            exist_file_dict = next(
                (target_dict for target_dict in summary[category] if target_dict['filename'] == filename), None)
            if exist_file_dict is None:
                continue

            MAX_ASSIGNEE_LEN = len(assignee) if len(
                assignee) > MAX_ASSIGNEE_LEN else MAX_ASSIGNEE_LEN
            MAX_ISSUE_LEN = len(issue_url) if len(
                issue_url) > MAX_ISSUE_LEN else MAX_ISSUE_LEN
            
            target_index = summary[category].index(exist_file_dict)
            summary[category][target_index]['issue'] = issue_url
            summary[category][target_index]['assignee'] = assignee
        except KeyError:
            pass
    
    '''
    Adding Space for Formatting Markdown Link
    '''
    MAX_ISSUE_LEN += 10
    
    '''
    Format the lines that will write into the markdown file,
    also sort the directory name and file name.
    '''
    writeliner = []
    summary_sorted = dict(sorted(summary.items()))
    for dirname, filelist in summary_sorted.items():
        writeliner.append(format_line_directory(dirname))
        writeliner.extend(format_line_table_header())

        
        filelist_sorted = sorted(filelist, key=lambda item: item['filename'])
        for filedata in filelist_sorted:
            writeliner.append(format_line_file(filedata))

    with open(
        f"summarize_progress/dist/summarize_progress.md",
        "w",
    ) as file:
        file.writelines(writeliner)
