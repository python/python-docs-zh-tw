import polib
import glob
import datetime
import requests


def entry_check(pofile):
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
        result = f"Ongoing, {str(progress_percentage)} %"

    return result


def get_open_issues_count() -> int:
    url = f"https://api.github.com/search/issues?q=repo:python/python-docs-zh-tw+type:issue+state:open"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    r = requests.get(url=url, headers=headers)
    result = r.json()

    return result["total_count"]


def get_github_issues():
    NUMBER_OF_ISSUES = get_open_issues_count()

    url = f"https://api.github.com/repos/python/python-docs-zh-tw/issues?per_page={NUMBER_OF_ISSUES}"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    r = requests.get(url=url, headers=headers)
    result = r.json()

    result_list = []
    for issue in result:
        title_segments = issue["title"].split()

        if len(title_segments) < 2:
            continue
        if title_segments[0] != "翻譯" and title_segments[0].lower() != "translate":
            continue
        if issue["assignee"] is None:
            continue

        filename = title_segments[1].strip("`")

        filename_segments = filename.split("/")
        if len(filename_segments) < 2:
            continue
        if filename_segments[1][-3:] != ".po":
            filename_segments[1] += ".po"

        result_list.append([filename_segments, issue["assignee"]["login"]])

    return result_list


def format_line_file(filename, result):
    return f"  - {filename.ljust(37, '-')}{result}\r\n"


def format_line_directory(dirname):
    tmp = f"- {dirname}/\r"
    return tmp


if __name__ == "__main__":
    issue_list = get_github_issues()

    directories = [
        "c-api",
        "distributing",
        "extending",
        "faq",
        "howto",
        "includes",
        "installing",
        "library",
        "reference",
        "tutorial",
        "using",
        "whatsnew",
    ]

    summary = {}

    file_list = glob.glob("./../**/*.po", recursive=True)
    file_list.sort()

    for filepath in file_list:
        if len(filepath.split("/")) == 4:  # in-dir files
            _, _, dirname, filename = filepath.split("/")
        else:  # root dir files
            _, _, filename = filepath.split("/")
            dirname = "/"

        if dirname not in summary:
            summary[dirname] = {}

        po = polib.pofile(filepath)
        result = entry_check(po)
        summary[dirname][filename] = result

    for (category, filename), assignee in issue_list:
        try:
            summary[category][filename] += f", 💻 {assignee}"
        except KeyError:
            pass

    writeliner = []
    for dirname, filedict in summary.items():
        writeliner.append(format_line_directory(dirname))
        for filename, result in filedict.items():
            writeliner.append(format_line_file(filename, result))

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(
        f"summarize_progress/dist/summarize_progress_{timestamp}.md",
        "w",
    ) as file:
        file.writelines(writeliner)
