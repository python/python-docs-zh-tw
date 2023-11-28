import polib
import os
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
        progress = round(progress * 100, 2)
        result = f"Ongoing, {str(progress)} %"

    return result


def get_github_issue():
    NUMBER_OF_ISSUES = 100

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

        if len(title) < 2:
            continue
        if title[0] != "翻譯" and title[0].lower() != "translate":
            continue
        if issue["assignee"] is None:
            continue

        filename = title[1].strip("`")

        filename_segments = filename.split("/")
        if len(filename_segments) < 2:
            continue
        if filename_segments[1][-3:] != ".po":
            filename_segments[1] += ".po"

        result_list.append([filename, issue["assignee"]["login"]])

    return result_list


def format_line_file(filename, result):
    return f"  - {filename.ljust(37, '-')}{result}\r\n"


def format_line_directory(dirname):
    tmp = f"- {dirname}/\r"
    return tmp


if __name__ == "__main__":
    issue_list = get_github_issue()

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

    for dir_name in directories:
        summary[dir_name] = {}
        for root, _, files in os.walk(f"../{dir_name}"):
            for file in files:
                if file.endswith(".po"):
                    filepath = os.path.join(root, file)
                    po = polib.pofile(filepath)
                    result = entry_check(po)
                    summary[dir_name][file] = result

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
