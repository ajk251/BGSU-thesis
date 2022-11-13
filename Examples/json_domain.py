
import json


d = {'a': [('asa', (2, 3), ('asfa', (2,4)))],
     'b': [('asx', (2, 3), ('asfx', (2,4)))],
     'c': [('asy', (2, 3), ('asfy', (2,4)))]}


# group: results  ￫ outcome of evaluation
#        cases    ￫ the test case
# ~~~or~~~
# group: (result, case) 


def write_json_file(file_location: str, dictionary):

    # help from: https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file

    with open(file_location, 'w', encoding='utf-8') as file:
        json.dump(dictionary, file, ensure_ascii=False)

def read_json_as_domain(file):

    # expects {group: [(result, case), …],
    #                 [(result, case), …] …}
    # yields (group, result, case)

    pass



write_json_file('./temp-file.json', d)

