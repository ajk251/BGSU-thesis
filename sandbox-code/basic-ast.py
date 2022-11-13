
import ast



def get_ast(file_path: str):

    with open(file_path, 'r') as file:
        tree = ast.parse(file.read(), type_comments=True)

    for node in ast.walk(tree):
        print(node)
        print(node.__dict__)
        print('\t', str([child for child in ast.iter_child_nodes(node)]))

        if 
        print('')




f = '/media/aaron/Shared2/School/BGSU-thesis/sandbox-code/loc-tests/loc-test.py'
get_ast(f)