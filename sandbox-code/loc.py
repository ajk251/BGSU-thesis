
import argparse
from functools import reduce
import re
import os

import os.path as path

from typing import Dict

# help from:
#   https://docs.python.org/3/library/re.html#module-re

# TODO:
#   • add multiple files as input
#   • count print statements (?)

nl           = re.compile('\n', re.MULTILINE)
blank        = re.compile('^\s*$', re.MULTILINE)
comment      = re.compile('^ *\#\s*', re.MULTILINE)
line_comment = re.compile('[\w\S]+[ ]*(\#)', re.MULTILINE)      # this is not perfect, will capture ￫ # 'https.../#thing  # this 
multi_comment = re.compile('\"\"\"[\s\S]*?\"\"\"', re.MULTILINE)
code         = re.compile('^\s*\w+', re.MULTILINE)

funcs        = re.compile('^def .+\:$', re.MULTILINE)        # unique & line-starting
classes      = re.compile('^class [\w\d]+', re.MULTILINE)
class_def    = re.compile('^ +def .+\:$', re.MULTILINE)
imports      = re.compile('^import |^from ', re.MULTILINE)
assertions   = re.compile('^\s*assert ', re.MULTILINE)       # all assertions start with white-space*

# -----------------------------------------------
# NOTE/Warning:
#   a) not efficient - it uses 1 regex per pass, 11 regexes
#   b) not fool proof - things like links with '#' can screw up the counts (like above)
#   c) not a parser & not perfect, just *mostly useful*
#   d) alias="python3 <path>/loc.py"  ⇒ helps

def count_lines(file_path: str) -> Dict[str, int]:
    """Count the number of lines of code, comments, blank lines, ect in a file."""

    results = {}

    with open(file_path, mode='r') as file:

        text = file.read()

        results['total-chars'] = len(text)
        results['non-ws chars'] = len(tuple(filter(lambda c: c not in (' ', '\n', '\t', '\r'), text)))
        results['total lines'] = len(nl.findall(text)) + 1                        # IDEs give the extra line
        results['blank']     = len(blank.findall(text))
        results['comment']   = len(comment.findall(text))
        results['inline comment'] = len(line_comment.findall(text))
        # results['multi-comment'] = len(multi_comment.findall(text))
        
        # this is a special case - have to count the number of lines inside the comments
        #   it counts the right number, but the lines inside count as code

        n = 0

        for line in multi_comment.findall(text):

            sublines = line.split('\n')

            if len(sublines) == 1:
                continue

            for subline in sublines:
                if subline != '"""': n += 1

        results['lines-code'] = len(code.findall(text)) - n

        results['functions'] = len(funcs.findall(text))
        results['classes'] = len(classes.findall(text))
        results['class-defs'] = len(class_def.findall(text))
        results['imports'] = len(imports.findall(text))
        results['assertions'] = len(assertions.findall(text))

    return results


def pretty(results: Dict[str, int]) -> str:

    line =  '╭' + ' total chars:      ' + format(results['total-chars'], '>6,') + ' ╮\n'
    line += '╰' + ' non-ws chars:     ' + format(results['non-ws chars'],'>6,') + ' ╯\n'
    line += '╭' + ' total lines:      ' + format(results['total lines'], '>6,') + ' ╮\n'
    line += '│' + ' lines of code:    ' + format(results['lines-code'], '>6,') + ' │\n'
    line += '╰' + ' blank lines:      ' + format(results['blank'], '>6,') + ' ╯\n'
    line += '╭' + ' comments:         ' + format(results['comment'], '>6,') + ' ╮\n'
    line += '╰' + ' in-line comments: ' + format(results['inline comment'], '>6,') + ' ╯\n'
    line += '╭' + ' def stmts:        ' + format(results['functions'], '>6,') + ' ╮\n'
    line += '│' + ' imports:          ' + format(results['imports'], '>6,') + ' │\n'
    line += '╰' + ' assertions:       ' + format(results['assertions'], '>6,') + ' ╯\n'
    line += '╭' + ' classes:          ' + format(results['classes'], '>6,') + ' ╮\n'
    line += '╰' + ' class defs:       ' + format(results['class-defs'], '>6,') + ' ╯\n'

    return line

# ---------------------------------------------

parser = argparse.ArgumentParser(description="Count the number of lines in code.")

parser.add_argument('file', type=str, nargs=1, help='The file to count the number of lines of code')

# -----------------------------------------------

if __name__ == '__main__':

    args = parser.parse_args()

    file = args.file[0]

    if not path.exists(file):
        raise FileNotFoundError(f"Path {file} was not found")
   
    # is it a directory?

    if path.isdir(file) or file == '.':

        if not os.path.isdir(file):
            raise FileNotFoundError(f"Path {file} was not found")

        with os.scandir(file) as directory:

            for file_ in directory:

                if file_.name.endswith('.py') and file_.is_file():
                    
                    results = count_lines(file_.path)

                    print()
                    print(f'File "{file_.name}" has:\n')

                    # for variable, count in results.items():
                    #     print('  ', '{:<15}'.format(variable), '{:>7}'.format(count))

                    print(pretty(results))

                    print('\n', '-' * 25, '\n')

        print()
    elif path.isfile(file) and file.endswith('.py'):
        
        results = count_lines(file)

        print()
        print(f'File "{file}" has:\n')

        # for variable, count in results.items():
        #     print('  ', '{:<15}'.format(variable), '{:>7}'.format(count))

        print(pretty(results))

        print()
