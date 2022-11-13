
import csv
import json



f = '/media/aaron/Shared2/School/BGSU-thesis/sandbox-code/falcon-tree.csv'


with open(f, 'r') as file:

    reader = csv.reader(file, delimiter='\t')

    for line in reader:
        
        line = line[0].split('\t')
        print(len(line), line)

        print(json.load(line[2]))
