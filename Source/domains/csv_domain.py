
from domains.domains import domain

import csv
import os

from collections import namedtuple
from enum import Enum
from operator import itemgetter

DomainType = Enum('DomainType', 'dict, namedtuple, tuple')

@domain(alias=['CSVDomain'])
def CSVDomain(file, columns=None, read_as=DomainType.dict, newline='\n'):

    # TODO: This isn't robust and assumes all arguments are well formed & valid
    # REFACTOR: Just use DictReader & itemgetter directly

    # if columns is not None and read_as is DomainType.dict:
    #     get_columns = itemgetter(*columns)
    if columns is not None:                                           # assume it is dict|namedtuple
        get_columns = itemgetter(*[columns.index(col) for col in columns])  # convert items

    with open(file, 'r', newline=newline) as csvfile:

        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)

        if read_as == DomainType.dict:

            reader = csv.DictReader(csvfile, dialect=dialect)

            for row in reader:

                if columns is not None:
                    row = {col: row[col] for col in columns}
                
                yield row
        elif read_as == DomainType.namedtuple:

            reader = csv.reader(csvfile, dialect=dialect)
            _ = next(reader)
            Value = namedtuple('Value', ','.join(columns))

            for row in reader:

                if columns is not None:
                    row = get_columns(row)
                
                value = Value(*row)

                yield value
        elif read_as == DomainType.tuple:
            
            reader = csv.reader(csvfile, dialect=dialect)
            _ = next(reader)

            for row in reader:

                if columns is not None:
                    row = get_columns(row)

                yield row

def CSVMultipleDomain(file, columns, read_as=DomainType.tuple, delimiter=',', newline='\n'):

    # TODO: This isn't robust and assumes all arguments are well formed & valid

    # if read_as is DomainType.dict:
    get_columns = [itemgetter(*dcolumns) for dcolumns in columns]
    # else:                                                                   # assume it is dict|namedtuple
    #     get_columns = itemgetter(*[columns.index(col) for col in columns])  # convert items

    with open(file, 'r', newline=newline) as csvfile:

        if read_as == DomainType.dict:

            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)

            reader = csv.DictReader(csvfile, dialect=dialect)
            
            for row in reader:
                items = tuple()
                for columns_ in columns:

                    values = {col: row[col] for col in columns_}
                    items += (values,)
            
                yield items
        elif read_as == DomainType.namedtuple:

            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)

            reader = csv.DictReader(csvfile, dialect=dialect)
            Values = [namedtuple('Value', ','.join(col)) for col in columns]
            
            for row in reader:
                items = tuple()
                for values_kind, cols in zip(Values, columns):
                    cols = {col: row[col] for col in cols}
                    values = values_kind(**cols)
                    items += (values,)
            
                yield items
        elif read_as == DomainType.tuple:

            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            
            reader = csv.DictReader(csvfile, dialect=dialect)
            
            for row in reader:
                items = tuple()
                for getter in get_columns:

                    values = getter(row)
                    items += (values,)
            
                yield items



# hotels = CSVDomain('/media/aaron/Shared2/School/BGSU-thesis/sandbox-code/sample-domain.csv', \
#                     columns=None, read_as=DomainType.dict)
# values = CSVDomain('/media/aaron/Shared2/School/BGSU-thesis/sandbox-code/sample-domain.csv', \
#                     columns=['pool', 'pets', 'smoking', 'king', 'stars'], read_as=DomainType.dict)

# for hotel, value in zip(hotels, values):
#     print(hotel, value)
    
# hotels = CSVDomain('/media/aaron/Shared2/School/BGSU-thesis/sandbox-code/sample-domain.csv', \
#                     columns=['hotel', 'distance'], read_as=DomainType.namedtuple)
# values = CSVDomain('/media/aaron/Shared2/School/BGSU-thesis/sandbox-code/sample-domain.csv', \
#                     columns=['pool', 'pets', 'smoking', 'king', 'stars'], read_as=DomainType.namedtuple)

# for hotel, value in zip(hotels, values):
#     print(hotel, value)

# print('⋯'*25)

# hotelsDB = CSVMultipleDomain('/media/aaron/Shared2/School/BGSU-thesis/sandbox-code/sample-domain.csv', \
#                     columns=[['hotel', 'distance'], ['pool', 'pets', 'smoking', 'king'], ['stars']], \
#                     read_as=DomainType.dict)

# for hotel, values, stars in hotelsDB:
#     print(f'Hotel: {hotel}, {stars} | {values}')
