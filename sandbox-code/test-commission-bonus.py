
from enum import Enum


# An extenstion of the locks, stocks, & barrels problem







# commission ----------------------------------------------



# bonuses -------------------------------------------------
def bonus_goodwork(paygrade, sales):
    return 0

def bonus_greatwork(paygrade, sales):
    return 0

def bonus_best(paygrade, sales):
    return 0

def bonus_greatsummer(paygrade, sales):
    return 0


# ―――――――――――――――――――――――――――――――――――――――――――――――――――――――――

PAYGRADE = Enum('Paygrade', 'juniorA, juniorB, specialistA, specialistB, specialistC, seniorA, seniorB')

# level = enum('Level', '_1, _3, _<')
SALARY= {  '<1': 10_000,
           '<3': 12_000,
           '<5': 15_000,
          '<10': 18_000,
          '<15': 21_000,
          '<20': 25_000,
          '>25': 30_000}

BONUSES = [bonus_goodwork, bonus_greatwork, bonus_best, bonus_greatsummer]