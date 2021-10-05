
# https://realpython.com/python-with-statement/#handling-exceptions-in-a-context-manager
# https://docs.python.org/3/reference/datamodel.html#context-managers
# https://docs.python.org/3.8/library/contextlib.html
# https://stackoverflow.com/questions/40538628/error-with-context-manager-definition
# https://stackoverflow.com/questions/58808055/what-are-the-python-builtin-exit-argument-types

import contextlib

class Winnow():

    def __init__(self):
        self.fn = None

    def __enter__(self):
        print('starting...')
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):

        # if exc_value:
        #     self.entrance = False
        # # signal that the exception was handled and the program should continue
        # return True

        # try:
        #     if isinstance(exc_value, AssertionError):
        #         print("Caught'ya! ", exc_value)
        #         # self.entrance = False
        # except AssertionError as error:
        #     print('trapped.')
        #     # return True
        
        if isinstance(exc_value, AssertionError):
            print("Caught'ya! ", exc_value)

        print('exiting...')

        return True



from contextlib import suppress
import os

with suppress(FileNotFoundError):
    print('suppressing')
    os.remove('somefile.tmp')
    print('here')
    print('and here')



with Winnow() as test:
    assert 1 + 1 == 2
    assert 2 + 2 == 2, 'Is this right?'
    assert 2 + 2 == 4
    assert True
    assert False == True, 'What about this?'


# -------------------------------------------------
print('-'*25)

class MyContextManager(object):

    def __init__(self):
        self.entrance = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            self.entrance = False
            print(exc_val)
        # signal that the exception was handled and the program should continue
        return True


# with MyContextManager() as cm:
#     print (cm.entrance)
#     raise Exception('First')
#     raise Exception('Second')

# print (cm.entrance)

# ----------------------------------------------------

from contextlib import suppress
import os

with suppress(FileNotFoundError):
    os.remove('somefile.tmp')
    print('here')
    print('and here')