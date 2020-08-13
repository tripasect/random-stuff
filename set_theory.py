from itertools import *
import math

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def X(*sets):
    result = []
    for element in product(*list(sets)):
        result.append(element)
    return result
