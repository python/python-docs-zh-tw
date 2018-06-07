import subprocess
import re

STRING = r'"((?:[^\"]|\\|\")*)"'
MSGID = r'^msgid ' + STRING
MSGSTR = r'^msgstr ' + STRING

HEADERS = [
    'Project-Id-Version',
    'Report-Msgid-Bugs-To',
    'POT-Creation-Date',
    'PO-Revision-Date',
    'Last-Translator',
    'Language-Team',
    'Language',
    'MIME-Version',
    'Content-Type',
    'Content-Transfer-Encoding',
    'Plural-Forms',
    'X-Generator',
]

def extract(lines, startline, first_line_regex=MSGID):
    first_line_match = re.match(first_line_regex, lines[startline])
    current_string = ""
    if first_line_match:
        current_string += first_line_match.group(1)
        lineno = startline + 1
        while lineno < len(lines):
            msg_match = re.match(STRING, lines[lineno])
            if msg_match is None:
                return current_string, lines[startline:lineno], lineno
            else:
                current_string += msg_match.group(1)
                lineno += 1
        else:
            return current_string, lines[startline:lineno], lineno
    return None, None, startline

def get_msgs(lines):
    msgids = []
    msgstrs = []
    lineno = 0
    while lineno < len(lines):
        string, raw_lines, lineno = extract(lines, lineno, MSGID)
        if string is not None:
            msgids.append((string, raw_lines))
            continue
        string, raw_lines, lineno = extract(lines, lineno, MSGSTR)
        if string is not None:
            msgstrs.append((string, raw_lines))
            continue
        lineno += 1
    return msgids, msgstrs

def main(fp):
    p = subprocess.Popen(['git', 'show', 'HEAD:' + fp], stdout=subprocess.PIPE)
    out, err = p.communicate()
    head_po = out.decode().splitlines()
    msgids, msgstrs = get_msgs(head_po)
    msgids = iter(msgids)
    msgstrs = iter(msgstrs)
    with open(fp) as f:
        lines = f.read().splitlines()
        output_lines = []
        lineno = 0
        while lineno < len(lines):
            for first_line_regex, original_msgs in [(MSGID, msgids), (MSGSTR, msgstrs)]:
                string, raw_lines, lineno = extract(lines, lineno, first_line_regex)
                if string is not None:
                    original_msg, original_lines = next(original_msgs)
                    if original_msgs is msgstrs:
                        lines_in_msg = string.split('\\n')[:-1]
                        for line in lines_in_msg:
                            if not any(line.startswith(h + ':') for h in HEADERS):
                                break
                        else:
                            del raw_lines[1:]
                            for header_line in lines_in_msg:
                                if header_line.startswith('Language: '):
                                    raw_lines.append('"Language: zh-Hant\\n"')
                                else:
                                    raw_lines.append('"{}\\n"'.format(header_line))
                    if string == original_msg:
                        output_lines.extend(original_lines)
                    else:
                        output_lines.extend(raw_lines)
                    break
            else:
                output_lines.append(lines[lineno])
                lineno += 1
    return output_lines


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Usage: python fix_diffs.py <po_file_path>')

    fp = sys.argv[1]
    output_lines = main(fp)

    with open(fp, 'w') as f:
        f.writelines([s + '\n' for s in output_lines])
