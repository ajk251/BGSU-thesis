
import ast
import token

from tokenize import generate_tokens, tok_name, tokenize


def visit(file_path):


    positions = {}

    with open(file_path, 'r') as file:

        tree = ast.parse(file.read(), type_comments=True)

        for node in ast.walk(tree):
            # print(node)
            # print(type(node), node._fields, node.__dict__)
            # print()

            if hasattr(node, 'lineno'):
                positions[(node.lineno, node.col_offset)] = (node, )

            for child in ast.iter_child_nodes(node):
                if hasattr(node, 'lineno'):
                    positions[(node.lineno, node.col_offset)] = (child, )

    with open(file_path, 'r') as file:

        for tkn in generate_tokens(file.readline):
            # print(tkn.start)
            if tkn.start in positions:
                positions[tkn.start] += (tkn, )
            else: 
                positions[tkn.start] = (tkn, )
    
    for value in positions.items():

        if len(value) == 2:
            print(value[0], value[1])
        else:
            print(value)


f = '/media/aaron/Shared2/School/BGSU-thesis/sandbox-code/loc-tests/paper-example.py'
visit(f)