import math
import itertools


def list_combinations(n, r, multiset=False):
    """Returns a list of all possible r-comb of a n-sized list"""
    if not multiset:
        return list(itertools.combinations(n,r))

    # If there are multiple occurences of the same object, can use this option
    # which will strip out duplicates from the result. Not sure if this
    # is entirely accurate or not. 
    elif multiset:
        return set(list(itertools.combinations(n,r)))


def list_permutations(n,r, multiset=False):
    """Returns a list of all possibl r-perm of a n-sized list"""
    if not multiset:
        return list(itertools.permutations(n,r))

    elif multiset:
        return set(list(itertools.permutations(n,r)))


def r_permutations(n, r):
    """Calculates the number of r combintaions of an n-sized set"""
    return math.factorial(n) / math.factorial(n - r)


def r_combinations(n,r):
    """Calculates the number of r combintaions of an n-sized set"""
    return r_permutations(n,r) / math.factorial(r)

