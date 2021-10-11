
# This code comes from:
#     https://bitbucket.org/takluyver/greentreesnakes/src/master/examples/test_framework/run.py
#  based on:
#     https://greentreesnakes.readthedocs.io/en/latest/examples.html

 # partially based off:
#   https://www.pythoninsight.com/2018/02/assertion-rewriting-in-pytest-part-3-the-ast/
#   https://www.pythoninsight.com/2018/02/assertion-rewriting-in-pytest-part-4-the-implementation/

# The code is:
#   https://github.com/pytest-dev/pytest/blob/main/src/_pytest/assertion/rewrite.py

# pytest does something similiar:
#   https://docs.pytest.org/en/6.2.x/assert.html
#   https://pybites.blogspot.com/2011/07/behind-scenes-of-pytests-new-assertion.html

   

import ast

filename = "/media/aaron/Shared2/School/BGSU-thesis/sandbox-code/asserts.py"
with open(filename, encoding='utf-8') as f:
    code = f.read()

    
class AssertCmpTransformer(ast.NodeTransformer):
    """Transform 'assert a==b' into 'assert_equal(a, b)'
    """
    def visit_Assert(self, node):
        if isinstance(node.test, ast.Compare) and \
                len(node.test.ops) == 1 and \
                isinstance(node.test.ops[0], ast.Eq):
            call = ast.Call(func=ast.Name(id='assert_equal', ctx=ast.Load()),
                            args=[node.test.left, node.test.comparators[0]],
                            keywords=[])
            # Wrap the call in an Expr node, because the return value isn't used.
            newnode = ast.Expr(value=call)
            ast.copy_location(newnode, node)
            ast.fix_missing_locations(newnode)
            return newnode
        
        # Return the original node if we don't want to change it.
        return node



# use custom error type
def assert_equal(a, b):
    if a != b:
        # raise AssertionError("%r != %r" % (a, b))
        print(f'Watch out! {a} ≠ {b}')
        raise AssertionError("%r != %r" % (a, b))


tree = ast.parse(code)
lines = [''] + code.splitlines()  # None at [0] so we can index lines from 1
test_namespace = {'assert_equal': assert_equal}

# code = '''
# l = [1,2,3,4]
# assert len(l) == 4
# '''

tree = ast.parse(code)
tree = AssertCmpTransformer().visit(tree)

print(ast.dump(tree, indent=4))

print('―'*25)

# bc = compile(tree, '<string>', mode='eval')
# eval(bc, {}, {})

for node in tree.body:

    wrapper = ast.Module(body=[node], type_ignores=[])
    
    try:
        co = compile(wrapper, filename, mode='exec')
        exec(co, test_namespace)

    except AssertionError as e:
        print("Assertion failed on line", node.lineno, ":")
        print(lines[node.lineno])
        # If the error has a message, show it.
        if e.args:
            print(e)
        print()
