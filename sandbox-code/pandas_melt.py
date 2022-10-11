
from collections import defaultdict
from random import choice, choices, randint, random, randrange, sample, triangular, uniform
from typing import Tuple
from string import ascii_letters

from Falcon.domains import domain
from Falcon.predicates import predicate

import pandas as pd

# Docs: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.melt.html

# This function is useful to massage a DataFrame into a format where one or more columns\
#   are identifier variables (id_vars), while all other columns, 
#   considered measured variables (value_vars), are “unpivoted” to the row axis, 
#   leaving just two non-identifier columns, ‘variable’ and ‘value’.


# properties to test
#   shape
#   columns
#   df.melt == pd.melt
#   column names

# categories
letters = ['A', 'B', 'C', 'D', 'E']
numbers = list(range(10))
days = ['sun', 'mon', 'tue', 'wed', 'thr', 'fri', 'sat']
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

# -----------------------------------------------

# sut 
def melt_sut(values):
    return values[0], values[1]

def df_generator(n: int = 10, max_cols: int = 100, max_rows: int = 10_000):
    # yields key, melted-df

    # column
    make_columns = lambda n: ['C'+str(n) for n in range(0, n)]
    rcolumn_int = lambda n: [randint(-1_000, 1_000) for _ in range(n)]
    rcolumn_float = lambda n: [uniform(-1_000.0, 1_000.0) for _ in range(n)]

    # optionally calls with
    #   id_vars
    #   var_name
    #   value_name

    # ARGS              SHAPE
    # _             -> (df.shape[0] * df.shape[1]), 2)
    # id_vars       -> (df.shape[0] * len(mdf['variable'].unique(), 3)
    # value_args    -> (df.shape[0] * len(key['var-name']), 2)
    # id & value    -> (len(key['var-name'] * df.shape[0]), 3)

    i = 0

    while i < n:

        key = dict.fromkeys(['categorical', 'columns', 'width', 'height',
                             'id-var', 'var-name', 'value-name',
                             'all-column-total', 'partial-total', 'partial-total-2'], None)

        # triangular is better for testing the tests
        # width, height = int(triangular(2.0, max_cols, 10.0)), int(triangular(0, max_rows, 50.0))
        # width, height = randrange(2, max_cols), randrange(2, max_rows)       # shape of the df
        width, height = 3, 5       # shape of the df
        columns = make_columns(width)                                        # column names

        # dict of column: data...
        # NOTE: it doesn't add up floats reliably when checked, if python ￫ numpy .sum()
        data = {col: rcolumn_float(height) if random() <= 0.0 else rcolumn_int(height) for col in columns}

        # add a random categorical column
        col_melt = choice([ascii_letters, letters, numbers, days, months])      # categorical column
        rcolumn = choice(columns)
        data[rcolumn] = choices(col_melt, k=height)

        # the columns with the category removed
        data_ = set(columns)
        data_.remove(rcolumn)
        data_ = tuple(data_)

        total = sum((sum(data[column]) for column in data_))            # this is used to check the sum

        # basic info
        key['width'] = width
        key['height'] = height
        key['categorical'] = rcolumn
        key['columns'] = columns
        key['data'] = tuple(data_)
        key['unique'] = len(columns) - 1
        key['id-var'] = None
        key['var-name'] = None
        key['len-vars'] = 0
        key['all-column-total'] = total

        # for naming, these are the defaults
        key['value-names'] = 'value'
        key['var-name']    = 'variable'

        df = pd.DataFrame(data)

        yield key, pd.melt(df)                                       # call with no args

        key['id-var'] = rcolumn                                      # call with id_var

        yield key, pd.melt(df, id_vars=key['categorical'])

        key['id-var'] = None
        key['var-name'] = sample(data_, k=randint(1, len(data_)))    # call with value_args
        key['len-vars'] = len(key['var-name'])
        key['partial-total'] = sum(sum(data[column]) for column in key['var-name'])
        yield key, pd.melt(df, value_vars=key['var-name'])

        key['id-var'] = rcolumn                                      # call with id_var & value_args
        key['var-name'] = sample(data_, k=randint(1, len(data_)))
        key['len-vars'] = len(key['var-name'])
        key['partial-total-2'] = sum(sum(data[column]) for column in key['var-name'])
        # print(' ---> ', sum(sum(data[column]) for column in key['var-name']))

        yield key, pd.melt(df, id_vars=key['categorical'], value_vars=key['var-name'])

        i += 1

#predicates -------------------------------------

def valid_dataframe(key, df) -> bool:
    """Tests that it is a DataFrame and is of the expected shape"""
    return isinstance(df, pd.DataFrame)


# def agrees(key, df):
#     # have to figure out the kind of melt it is first
#     pass


# def right_columns(key, df):
#     # are the columns named correctly
#     return True


def sums_correctly(key, df) -> bool:
    # the sums of the columns add up correctly
    # note: some columns are dropped, so they have different sums
    df_sum = int(pd.to_numeric(df['value'], errors='coerce').sum())   # the sum, as an int
    return df_sum == key['all-column-total'] or \
           df_sum == key['partial-total'] or \
           df_sum == key['partial-total-2']


def is_melted_no_args(key, df) -> bool:
    return df.shape == (key['width'] * key['height'], 2)


def is_melted_id_args(key, df) -> bool:
    return df.shape == (key['height'] * key['unique'], 3)


def is_melted_value_vars(key, df) -> bool: 
    # (df.shape[0] * len(key['var-name']), 2))
    return df.shape == (key['height'] * key['len-vars'], 2)


def is_melted_id_value(key, df) -> bool:
    # (len(key['var-name']) * df.shape[0], 3))
    return df.shape == (key['len-vars'] * key['height'], 3)

# melt() == pd.melt()

# -----------------------------------------------

# add empty frame
# add unique values, test the sum -- should always be the same
# add check for column names

for key, df in df_generator(5):

    print(df.columns, key['value-names'], key['var-name'])

    if valid_dataframe(key, df):
        print('valid!')

    if sums_correctly(key, df):
        print('sums correctly')

    if is_melted_no_args(key, df):
        print('melted - no args')

    if is_melted_id_args(key, df):
        print('melted - id args')

    if is_melted_value_vars(key, df):
        print('melted value vars')

    if is_melted_id_value(key, df):
        print('melted - both')
        # print(df)

    # print(df.columns)
    # print(df)
    # print(pd.to_numeric(df['value'], errors='coerce').sum())

    # print('Random DF')
    # # print(df)
    # print(df.shape, key['id-var'], key['var-name'])
    # print()

    # print('with no args')
    # mdf = pd.melt(df)
    # # print(mdf)
    # print(mdf.shape, ' expected ', (df.shape[0] * df.shape[1]), 2)
    # print('\t'*5, mdf.shape == (df.shape[0] * df.shape[1], 2))
    # print()

    # print('with id_vars')
    # mdf = pd.melt(df, id_vars=key['categorical'])
    # # print(mdf)
    # print(df.shape, mdf.shape, ' expected ', (df.shape[0] * len(mdf['variable'].unique()), 3))
    # print('\t'*5, mdf.shape == (df.shape[0] * len(mdf['variable'].unique()), 3))
    # print('\t->', len(mdf['variable'].unique()), key['unique'], key['height'] * key['unique'])
    # print()

    # print('with value_vars     ', key['var-name'])    
    # mdf_value = pd.melt(df, value_vars=key['var-name'])
    # print(mdf_value)
    # print(mdf_value.shape)
    # print('\t'*5, mdf_value.shape == (df.shape[0] * len(key['var-name']), 2))
    # print()

    # print('with id_vars & value_vars  ', key['categorical'], key['var-name'])
    # mdf_id_value = pd.melt(df, id_vars=key['categorical'], value_vars=key['var-name'])
    # print(mdf_id_value)
    # print(mdf_id_value.shape)
    # print('expected: ', (len(key['var-name']) * df.shape[0], 3))
    # print('\t'*5, mdf_id_value.shape == (len(key['var-name'] * df.shape[0]), 3))

    print('-' * 25)