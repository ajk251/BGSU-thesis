

# example from:
#   https://medium.com/homeaway-tech-blog/write-better-python-with-hypothesis-5b31ac268b69


# tldr:
#   - this code can fail in two ways
#       • if one of the lengths is 0
#       • if the max depth is greater than either of the two examples

def average_agreement(list1, list2, max_depth):

    agreements = []

    for depth in range(1, max_depth+1):
        
        set1 = frozenset(list1[:depth])
        set2 = frozenset(list2[:depth])

        intersection = set1 & set2
        n = 2 * len(intersection) / (len(set1) + len(set2))
        agreements.append(n)

    return sum(agreements) / len(agreements)


print(average_agreement(range(0, 100), range(50, 150), 10))


def satify_agreement_properties(list1, list2, depth):

    answer = average_agreement(list1, list2, depth)
    inverse_answer = average_agreement(list2, list1, depth)    

    if not (0.0 <= answer <= 1.0):
        return False
    elif not (0.0 <= inverse_answer <= 1.0):
        return False
    elif not (answer == inverse_answer):
        return False

    return True



def test_domain(n: int = 100, length_max = 100_000, depth_max: int = 10_000):

    from random import randint

    for _ in range(n):

        l1_size = randint(0, length_max)
        l2_size = randint(0, length_max)

        depth = randint(0, depth_max)

        l1 = [randint(0, 5) for _ in range(l1_size)]
        l2 = [randint(0, 5) for _ in range(l2_size)]

        assert satify_agreement_properties(l1, l2, depth)

    return 


test_domain()

# between? 0.0 1.0


