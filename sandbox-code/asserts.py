
# some generic test code

import random

diceroll = random.randint(1, 6)

# All but one of these will fail.
assert diceroll == 1, 'Diceroll does not equal 1'
assert diceroll == 2, 'Diceroll does not equal 2'
assert diceroll == 3, 'Diceroll does not equal 3'
assert diceroll == 4, 'Diceroll does not equal 4'
assert diceroll == 5, 'Diceroll does not equal 5'
assert diceroll == 6, 'Diceroll does not equal 6'

# assert "Because it's parsing the code first, it works with" < \
#        "Multi-line statements too." < \
#        "This one will pass."