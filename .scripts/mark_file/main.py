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
        progress = round(progress*100, 2)
        result = f"Ongoing, {str(progress)} %"

    return result


def get_github_issue():
    NUMBER_OF_ISSUES = 100

    url = f"https://api.github.com/repos/python/python-docs-zh-tw/issues?per_page={NUMBER_OF_ISSUES}"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    r = requests.get(url=url, headers=headers)
    result = r.json()

    result_list = []
    for issue in result:
        title = issue['title'].split(" ")

        if len(title) < 2:
            continue
        if title[0] != "翻譯" and title[0].lower() != "translate":
            continue
        if issue["assignee"] is None:
            continue

        filename = title[1]
        if filename[0] == "`":
            filename = filename[1:]
        if filename[-1] == "`":
            filename = filename[:-1]

        filename = filename.split("/")
        if len(filename) < 2:
            continue
        if filename[1][-3:] != ".po":
            filename[1] += ".po"

        result_list.append([filename, issue["assignee"]["login"]])

    return result_list


def format_line_file(filename, result):
    tmp = f"  - {filename}"
    tmp = f"{tmp}{'-' * (40-len(tmp))}{result}\r"
    return tmp


def format_line_directory(dirname):
    tmp = f"- {dirname}/\r"
    return tmp


if __name__ == "__main__":

    issue_list = get_github_issue()

    directories = ["c-api", "distributing", "extending", "faq", "howto", "includes",
                   "installing", "library", "reference", "tutorial", "using", "whatsnew"]

    summary = {}

    for dir_name in directories:
        summary[dir_name] = {}
        for root, dirs, files in os.walk(f"../{dir_name}"):
            for file in files:
                if file.endswith(".po"):
                    filepath = os.path.join(root, file)
                    po = polib.pofile(filepath)
                    result = entry_check(po)
                    summary[dir_name][file] = result

    for issue in issue_list:
        title = issue[0]
        assignee = issue[1]

        try:
            summary[title[0]][title[1]] += f", 💻 {assignee}"
        except KeyError:
            pass

    writeliner = []
    for dirname, filedict in summary.items():
        writeliner.append(format_line_directory(dirname))
        for filename, result in filedict.items():
            writeliner.append(format_line_file(filename, result))

    file = open(
        f"mark_file/dist/mark_file_{datetime.datetime.today().strftime('%Y%m%d_%H%M%S')}.md", "w")
    file.writelines(writeliner)
    file.close()
