
# this was used in iconv_test2.py


# ---------------------------------------------------------

# for case in generate_cases(100):

#     # print(case)
#     case = identity_iconv(case)

#     print(case['source'], ' ￫ ', case['dest'])

#     if does_load(case):
#         print('\tloads')
#     else:
#         print('\tno load')

#     if like_iconv(case):
#         print('\tlike iconv ')
#     else:
#         print('\tnot iconv  ')

#     # other tests
#     if valid_points(case):
#         print('\tvalid')
#     else:
#         print('\tno points')

#     if most_128(case):
#         print('\tmost 128')
#     else:
#         print('\t< 128')

#     if most_256(case):
#         print('\tmost 256')
#     else:
#         print('\t< 256')

# print('-' * 35)

# for case in generate_pycases(100):

#     print(case['source'], ' ￫ ', case['dest'], len(case['points']))

#     if loads_in_iconv(case):
#         print('\tloads 🗸')
#     else:
#         print('\tload ✗')


#     if converts_in_iconv(case):
#         print('\tconverts 🗸')
#     else:
#         print('\tconvert ✗')


#     if matchs_python_codec(case):
#         print('\tmatches 🗸')
#     else:
#         print('\tmatches ✗')


#     if matches_iconv(case):
#         print('\ticonv 🗸')
#     else:
#         print('\ticonv ✗')
