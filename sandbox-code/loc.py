
import argparse
import ast
import re
import os
import token

from collections import defaultdict, namedtuple
from functools import reduce
from keyword import iskeyword, issoftkeyword, kwlist
from math import log2
from statistics import mean
from tokenize import generate_tokens, tok_name, tokenize
from types import SimpleNamespace
from typing import Dict, List, Tuple

import os.path as path

# help from:
#   https://docs.python.org/3/library/re.html#module-re

# myers complexity:
#   https://www.perforce.com/blog/qac/what-cyclomatic-complexity

# Halstead:
#   https://www.javatpoint.com/software-engineering-halsteads-software-metrics

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

# this is useful on a per-line basis ------------
# nl           = re.compile('\n')
# blank        = re.compile('^\s*$')
# comment      = re.compile('^ *\#\s*')
# line_comment = re.compile('[\w\S]+[ ]*(\#)')      # this is not perfect, will capture ￫ # 'https.../#thing  # this 
# multi_comment = re.compile('\"\"\"[\s\S]*?\"\"\"')
# code         = re.compile('^\s*\w+')

# funcs        = re.compile('^def .+\:$')        # unique & line-starting
# classes      = re.compile('^class [\w\d]+')
# class_def    = re.compile('^ +def .+\:$')
# imports      = re.compile('^import |^from ')
# assertions   = re.compile('^\s*assert ')       # all assertions start with white-space*

# -----------------------------------------------
# NOTE/Warning:
#   a) not efficient - it uses 1 regex per pass, 11 regexes
#   b) not fool proof - things like links with '#' can screw up the counts (like above)
#   c) not a parser & not perfect, just *mostly useful*
#   d) alias="python3 <path>/loc.py"  ⇒ helps

# -----------------------------------------------

def tokens_by_line(file_path):
    """All tokens per line in a list (even newlines). Returns List[List[Tokens, ...], ...]"""

    lines = []
    line = []

    with open(file_path, mode='r') as file:

        for tkn in generate_tokens(file.readline):

            if tkn.type == 62 or tkn.type == 4:
                lines.append(line)
                line = [tkn]
                # lines.append(line)
                # print(lines)
            else:
                # print('adding: ', tkn.string)
                line.append(tkn)

    return lines


# -----------------------------------------------

def ast_walk(file_path: str):


    # cyclomatic complexity
    # halstead
    # counts
    #   functions
    #       names, lines, arguments (all 5) halstead, complexity
    #       has-docstring, comments (both), lines
    #       out fn calls
    #   classes
    #       names, total funcs, magic methods
    #       inherits n, 
    #   counts
    #       imports
    #       asserts


    results = dict.fromkeys(('cyclomatic', 'myers'), 0)

    with open(file_path, 'r') as file:
        tree = ast.parse(file.read(), type_comments=True)

    for node in ast.walk(tree):
        print(node)
        print(type(node), node._fields, node.__dict__)
        print()
        

        # cyclomatic complexity





def cyclomatic_complexity(tokens) -> Tuple[int, int]:


    constructs = {'if', 'elif', 'for', 'while', 'except', 'with', 'assert', 'and', 'or'}
    mconstructs = {'and', 'or', 'not', '&', '|', '==', '!='}

    cyclomatic = 1
    myers = 1

    for line in tokens:
        for tkn in line:

            if tkn.type != 1: continue

            if tkn.string in constructs:
                cyclomatic += 1
            if tkn.string in mconstructs:
                myers += 1

    return cyclomatic, myers


def halstead(tokens):

    # From geeks for geeks, for C
    #   https://www.geeksforgeeks.org/software-engineering-halsteads-software-metrics/
    #   comments & function identifers & directives are ignored
    #   variables, constants are operands
    #   all local vars are considered unique operands
    #   brackets, commas, terminators are operands
    #   func calls are operators
    #   all loops & control statements are operators
    #   ⁺¯ are treated with numbers
    #   array names are operands and [] are operators, ie X[]

    Halstead = namedtuple('Halstead', 'N,N1,N2,n,n1,n2')
    Metric   = namedtuple('Metric', 'difficutly,vocabulary,length,volume,effort,time_required,bugs')
    
    # note: only counting left ({[
    ignore = frozenset([token.NL, token.NEWLINE, token.INDENT, token.DEDENT, token.COMMENT, token.RPAR, token.RBRACE, token.RSQB])
    # kw_operators = frozenset(['str', 'int', 'float', 'complex', 'dict', 'set', 'frozenset', 'list', 'tuple', 'self'])
    operands_types = frozenset([token.OP, token.NUMBER, token.NAME, token.STRING])

    operators: Dict[str, int] = defaultdict(int)
    operands: Dict[str, int]  = defaultdict(int)

    indent = 0

    for line in tokens:
        for tkn in line:

            if tkn.type == 5:                               # indent in the code
                indent += 1
            elif tkn.type == 6:                             # dedent in the code
                indent -= 1 
            
            # skip these
            if tkn.type in ignore:
                continue
            elif tkn.type == token.OP and tkn.string == ')':
                continue

            # print(tok_name[tkn.type], tkn.type, ' ￫ ', tkn.string)

            # is it a function or class definition?
            if indent == 0 and tkn.string == 'class' or tkn.string == 'def':
                break                                                                       # skip the line

            if iskeyword(tkn.string) or issoftkeyword(tkn.string) or tkn.type == token.OP:  # operators -> keyword or operator
                operators[tkn.string] += 1
            elif tkn.type in operands_types:                                                  # count operands
                operands[tkn.string] += 1
    
    # print(operators.keys())
    # print(operands.keys())

    halstead = dict.fromkeys(['N', 'N1', 'N2', 'n', 'n1', 'n2', 'length', 'volume', 'difficulty', 'effort', 'time', 'bugs'], 0.0)

    halstead['N1'] = sum(operators.values())                # total operators
    halstead['N2'] = sum(operands.values())                 # total operands
    halstead['n1'] = len(operators)                         # distinct operators
    halstead['n2'] = len(operands)                          # distinct operands

    halstead['N'] = halstead['N1'] + halstead['N2']
    halstead['n'] = halstead['n1'] + halstead['n2']

    halstead['length'] = halstead['n1'] * log2(halstead['n1']) + halstead['n2'] * log2(halstead['n2'])
    halstead['volume'] = halstead['N'] * log2(halstead['n'])
    halstead['difficulty'] = (halstead['n1'] / 2.0) * (halstead['N2'] / halstead['n2'])
    halstead['effort'] = halstead['difficulty'] * halstead['volume']
    halstead['time'] = halstead['effort'] / 18.0
    halstead['bugs'] = halstead['volume'] / 3000.0

    return halstead


def by_def(tokens):

    is_def = lambda tkn, indent: tkn.type == 1 and tkn.string == 'def' and indent == 0

    indent = 0                  # the current indentation
    defs = {}
    current = None              # the current def

    depths = {}
    max_depth = 0

    in_def = False              # currently in a def stmt?

    print(len(tokens))

    for line in tokens:        
        for i,tkn in enumerate(line):

            if tkn.type == 5:                               # indent in the code
                indent += 1
            elif tkn.type == 6:                             # dedent in the code
                indent -= 1

            if is_def(tkn, indent):
                current = line[i+1].string
                defs[current] = []
                depths[current] = 0

            if indent >= 1 and current is not None:
                defs[current].append(tkn)
                max_depth = indent
                depths[current] = max(max_depth, indent)
            else:
                current = None


    # the various metrics ---

    print(defs.keys())
    metrics = {}

    for func, tokens in defs.items():

        metrics[func] = {}
        metrics[func]['max-depth']  = depths[func]
        metrics[func]['cyclomatic'] = cyclomatic_complexity(tokens)

    print('functions: ', metrics.items())


def counts(tokens):

    # with open(file_path, 'r') as f:

    #     tokens = tuple(generate_tokens(f.readline))

    indent = 0
    line = 0
    # chars = 0           # code
    # nws_chars = 0       # non-ws chars

    results = dict.fromkeys(['comments', 'def', 'closures', 'class', 'imports', 'import', 'from', 'assertions', 'raise', 'return', 'yield', 'pass', 'lambda', 'decorators'], 0)

    for line in tokens:
        for tkn in line:

            # for tkn in tokens:

            if tkn.type == 5:                           # indent/dedent
                indent +=1
            elif tkn.type == 6:
                indent -= 1

            if tkn.type == token.COMMENT:
                results['comments'] += 1
            elif tkn.type == 1:
                if tkn.string == 'def' and indent == 0:
                    results['def'] += 1
                elif tkn.string == 'class'  and indent == 0:
                    results['class'] += 1
                elif tkn.string == 'def':
                    results['closures'] += 1
                elif tkn.string == 'assert':
                    results['assertions'] += 1
                elif tkn.string == 'raise':
                    results['raise'] += 1
                elif tkn.string == 'return':
                    results['return'] += 1
                elif tkn.string == 'yield':
                    results['yield'] += 1
                elif tkn.string == 'pass':
                    results['pass'] += 1  
                elif tkn.string == 'lambda':
                    results['lambda'] += 1
                elif tkn.string == 'import' and indent == 0:
                    results['import'] += 1
                    results['imports'] += 1
                elif tkn.string == 'from'  and indent == 0:
                    results['from'] += 1
                elif tkn.string == '@':
                    results['decorators'] += 1
        
    return results


# -----------------------------------------------

def count_lines(file_path: str) -> Dict[str, int]:
    """Count the number of lines of code, comments, blank lines, ect in a file."""

    results = dict.fromkeys(['blank', 'loc', 'sloc', 'max-line-length', 'lines-over-80',
                             'mean-line-length', 'inline comment', 'total-chars', 'complexity'], 0)


    tokens = tokens_by_line(file_path)
    results['cyclomatic'], results['myers'] = cyclomatic_complexity(tokens)
    # by_def(tokens)
    # counts(tokens)
    # print(halstead(tokens))
    # print(tokens_by_line(file_path))
    ast_walk(file_path)

    with open(file_path, mode='r') as file:

        text = file.read()

        for line in text.split('\n'):

            results['total-chars'] += len(line)
            # results['blank-chars'] += len(line)

            results['blank'] += 0 if line == '' else 1
            results['loc'] += 1
            results['sloc'] += 1 if line != '' and (not line.startswith('#')) else 0

        code_lines = tuple((line for line in text.split('\n') if (line != '' and (not line.startswith('#')))))
        lengths = tuple((len(line) for line in code_lines))

        results['max-line-length'] = max(lengths)
        results['lines-over-80'] = len(tuple((len(line) >= 80 for line in code_lines)))
        results['mean-line-length'] = mean(lengths)

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

    line = 'Characters\n'
    line += '╭ total chars:      ' + format(results['total-chars'], '>6,') + ' ╮\n'
    line += '│ non-ws chars:     ' + format(results['non-ws chars'],'>6,') + ' │\n'
    line += '╰ %                 ' + format(results['non-ws chars'] / results['total-chars'], '>6.3f') + ' ╯\n'
    line += '\nLines\n'
    line += '╭' + ' total lines:      ' + format(results['total lines'], '>6,') + ' ╮\n'
    line += '│' + ' lines of code:    ' + format(results['lines-code'], '>6,') + ' │\n'
    line += '╰' + ' blank lines:      ' + format(results['blank'], '>6,') + ' ╯\n'
    line += '\nLine Length\n'
    line += '╭' + ' max line length:  ' + format(results['max-line-length'], '>6,') + ' ╮\n'
    line += '│' + ' mean line length: ' + format(results['mean-line-length'], '>6.1f') + ' │\n'
    line += '╰' + ' lines >80 chars:  ' + format(results['lines-over-80'], '>6,') + ' ╯\n'
    line += '\nComments\n'
    line += '╭' + ' comments:         ' + format(results['comment'], '>6,') + ' ╮\n'
    line += '╰' + ' in-line comments: ' + format(results['inline comment'], '>6,') + ' ╯\n'
    line += '\nFunction def\n'
    line += '╭' + ' def stmts:        ' + format(results['functions'], '>6,') + ' ╮\n'
    line += '│' + ' imports:          ' + format(results['imports'], '>6,') + ' │\n'
    line += '╰' + ' assertions:       ' + format(results['assertions'], '>6,') + ' ╯\n'
    line += '\nClass def\n'
    line += '╭' + ' classes:          ' + format(results['classes'], '>6,') + ' ╮\n'
    line += '╰' + ' class defs:       ' + format(results['class-defs'], '>6,') + ' ╯\n'

    line += '\n Cyclomatic Complexity: ' + str(results['cyclomatic'])
    line += '\n Myers Complexity:      ' + str(results['myers'])

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
