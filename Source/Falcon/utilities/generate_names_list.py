
import csv

# these are the predicate files -----------------
from Falcon.predicates.basic import *
from Falcon.predicates.cardnality import *
from Falcon.predicates.numerical import *
from Falcon.predicates.pytypes import *
from Falcon.predicates.sequence import *

# these are the domain files --------------------
from Falcon.domains.domains import *
from Falcon.domains.basic import *
from Falcon.domains.csv_domain import *
from Falcon.domains.ART import *

# these are the algorithm files -----------------
from Falcon.algorithms.algorithms import ALGORITHMS
from Falcon.algorithms import algorithms
from Falcon.algorithms import adaptive_random_testing

PATH = '/media/aaron/Shared2/School/BGSU-thesis/Source'

# write to file ---------------------------------

with open(PATH + '/falcon-predicates.csv', 'w') as file:

    write = csv.writer(file, delimiter=',')
    header = 'predicate_name,name,symbol,is_symbolic,is_error,is_group,doc_error,error_message'.split(',')
    write.writerow(header)

    for key, predicate in PREDICATES.items():

        write.writerow((key, predicate.name, predicate.symbol, predicate.is_symbolic,
                        predicate.is_error, predicate.is_group, predicate.doc_error,
                        predicate.doc_error, predicate.error_message))

# domains -------------------------------------------------

with open(PATH + '/falcon-domains.csv', 'w') as file:

    write = csv.writer(file, delimiter=',')
    header = 'falcon_name,fn_name'.split(',')
    write.writerow(header)

    for key, domain in DOMAINS.items():
        write.writerow((key,domain))

# algorithms ----------------------------------------------

with open(PATH + '/falcon-algorithms.csv', 'w') as file:

    write = csv.writer(file, delimiter=',')
    header = 'falcon_name,fn_name'.split(',')
    write.writerow(header)

    for key, algorithm in ALGORITHMS.items():
        write.writerow((key, algorithm))
