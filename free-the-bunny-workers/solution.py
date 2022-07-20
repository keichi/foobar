from itertools import combinations
from math import factorial

def comb(c, r):
    return factorial(c) / factorial(r) / factorial(c - r)

def solution(num_buns, num_required):
    num_keys = comb(num_buns, num_required - 1)
    num_copies = num_buns - num_required + 1

    res = [[] for _ in range(num_buns)]

    for key, buns in enumerate(combinations(range(num_buns), num_copies)):
        for bun in buns:
            res[bun].append(key)

    return res
