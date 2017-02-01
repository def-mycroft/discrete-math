import math
import itertools


def list_combinations(n, r):
    """Returns a list of all possible r-comb of a n-sized list"""
    return list(itertools.combinations(n,r))


def list_permutations(n,r):
    """Returns a list of all possibl r-perm of a n-sized list"""
    return list(itertools.permutations(n,r))


def r_permutations(n, r):
    """Calculates the number of r combintaions of an n-sized set"""
    return math.factorial(n) / math.factorial(n - r)


def r_combinations(n,r):
    """Calculates the number of r combintaions of an n-sized set"""
    return r_permutations(n,r) / math.factorial(r)
