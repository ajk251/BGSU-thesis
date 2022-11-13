



def get_values(f):

    with open(f, 'r') as file:

        predicates = file.read().split('\n')

        print(predicates)

        for predicate in predicates:

            if predicate == '': continue

            name = predicate.replace('_', '\_')
            print(f'{name} &     \\\\')



f = '/media/aaron/Shared2/School/BGSU-thesis/notes/list-of-predicates.txt'

get_values(f)