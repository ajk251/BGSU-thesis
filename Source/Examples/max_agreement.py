
# example from:
#   https://medium.com/homeaway-tech-blog/write-better-python-with-hypothesis-5b31ac268b69


# tldr:
#   - this code can fail in two ways
#       • if one of the lengths is 0
#       • if the max depth is greater than either of the two lists

def average_agreement(list1, list2, max_depth):

    agreements = []

    for depth in range(1, max_depth+1):
        
        set1 = frozenset(list1[:depth])
        set2 = frozenset(list2[:depth])

        intersection = set1 & set2
        n = 2 * len(intersection) / (len(set1) + len(set2))
        agreements.append(n)

    return sum(agreements) / len(agreements)


def average_agreement2(list1, list2, max_depth):

    assert len(list1) > 0, "Length of list1 must be greater than 0"
    assert len(list2) > 0, "Length of list2 must be greater than 0"
    assert min(len(list1), len(list2)) > max_depth, "Depth cannot be greater than either lengths of the lists"

    agreements = []

    for depth in range(1, max_depth+1):

        set1 = frozenset(list1[:depth])
        set2 = frozenset(list2[:depth])

        intersection = set1 & set2
        n = 2 * len(intersection) / (len(set1) + len(set2))
        agreements.append(n)

    return sum(agreements) / len(agreements)


# print(average_agreement(range(0, 100), range(50, 150), 25))
# print(average_agreement(['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'], 2))
