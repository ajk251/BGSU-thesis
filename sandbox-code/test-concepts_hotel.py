
from collections import namedtuple
from random import choices, randint, random




Hotel = namedtuple('Hotel', 'price, nbeds, stars, pets, pool')


def make_hotel() -> Hotel:
    return Hotel(randint(65, 150),
                 randint(1,3),
                 choices([1,2,3,4,5], weights=[.1, .15, .45, .15, .15])[0],
                 True if random() <= 0.5 else False,
                 True if random() <= 0.4 else False)


def make_rooms(number: int):
    return tuple(make_hotel() for _ in range(number))



print(make_rooms(10))