from copy import deepcopy
from fractions import gcd, Fraction

def show(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(A[i][j]),
        print

def transpose(_A):
    A = [[Fraction(0) for _ in range(len(_A))] for _ in range(len(_A[0]))]

    for i in range(len(_A)):
        for j in range(len(_A[0])):
            A[j][i] = _A[i][j]

    return A

assert transpose([[Fraction(1), Fraction(2), Fraction(3)],
                  [Fraction(4), Fraction(5), Fraction(6)]]) \
              == [[Fraction(1), Fraction(4)],
                  [Fraction(2), Fraction(5)],
                  [Fraction(3), Fraction(6)]]

def inv(_A):
    assert len(_A) > 0
    assert len(_A) == len(_A[0])

    A = [[Fraction(0) for _ in range(2 * len(_A))] for _ in range(len(_A))]

    for i in range(len(A)):
        for j in range(len(A)):
            A[i][j] = _A[i][j]

            if i == j:
                A[i][j + len(_A)] = Fraction(1)

    for k in range(len(A)):
        Akk = A[k][k]
        for j in range(len(A[0])):
            A[k][j] /= Akk

        for i in range(len(A)):
            if i == k:
                continue
            Aik = A[i][k]
            for j in range(len(A[0])):
                A[i][j] -= A[k][j] * Aik

    return [x[len(A):] for x in A]

assert inv([[Fraction(1), Fraction(2)], [Fraction(3), Fraction(4)]]) \
    == [[Fraction(-2), Fraction(1)], [Fraction(3, 2), Fraction(-1, 2)]]

def mul(A, B):
    assert len(A) > 0 and len(A[0]) > 0
    assert len(B) > 0 and len(B[0]) > 0
    assert len(A[0]) == len(B)

    C = [[Fraction(0) for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
       for j in range(len(B[0])):
           for k in range(len(B)):
               C[i][j] += A[i][k] * B[k][j]

    return C

assert mul([[Fraction(1), Fraction(2)], [Fraction(3), Fraction(4)]],
           [[Fraction(5), Fraction(6)], [Fraction(7), Fraction(8)]]) \
    == [[Fraction(19), Fraction(22)], [Fraction(43), Fraction(50)]]


def standard_form(P):
    assert len(P) == len(P[0])

    P = deepcopy(P)

    for i in range(len(P)):
        denom = sum(P[i])

        if denom == 0:
            denom = 1

        for j in range(len(P)):
            P[i][j] = Fraction(P[i][j], denom)

    S = [[Fraction(0) for _ in range(len(P))] for _ in range(len(P))]

    abs_states = [i for i in range(len(P)) if all(x == 0 for x in P[i])]
    non_abs_states = [i for i in range(len(P)) if any(x != 0 for x in P[i])]
    num_abs_states = len(abs_states)

    for i, ix in enumerate(abs_states + non_abs_states):
        S[ix][i] = Fraction(1)

    P = mul(mul(transpose(S), P), S)
    R = [x[:num_abs_states] for x in P[num_abs_states:]]
    Q = [x[num_abs_states:] for x in P[num_abs_states:]]

    return R, Q


assert standard_form([[0, 2, 1, 0, 0],
                      [0, 0, 0, 3, 4],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0]]) \
    == ([[Fraction(1, 3), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(3, 7), Fraction(4, 7)]],
       [[Fraction(0), Fraction(2, 3)],
        [Fraction(0), Fraction(0)]])

def solution(m):
    if m == [[0]]:
        return [1, 1]

    R, Q = standard_form(m)

    for i in range(len(Q)):
        for j in range(len(Q[0])):
            if i == j:
                Q[i][j] = Fraction(1) - Q[i][j]
            else:
                Q[i][j] = -Q[i][j]

    X = mul(inv(Q), R)

    solution = X[0]

    denoms = [x.denominator for x in solution]

    lcm = denoms[0]
    for d in denoms[1:]:
        lcm = lcm / gcd(lcm, d) * d

    nums = [x.numerator * (lcm / x.denominator) for x in solution]

    return nums + [lcm]

assert(solution([[0, 2, 1, 0, 0],
               [0, 0, 0, 3, 4],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0]]) == [7, 6, 8, 21])

assert(solution([[0, 1, 0, 0, 0, 1],
               [4, 0, 0, 3, 2, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0]]) == [0, 3, 2, 9, 14])
assert(solution([[1, 2, 3, 0, 0, 0],
                 [4, 5, 6, 0, 0, 0],
                 [7, 8, 9, 1, 0, 0],
                 [0, 0, 0, 0, 1, 2],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0]]) == [1, 2, 3])

assert(solution([[0]]) == [1, 1])

assert(solution([[0, 0, 12, 0, 15, 0, 0, 0, 1, 8],
                 [0, 0, 60, 0, 0, 7, 13, 0, 0, 0],
                 [0, 15, 0, 8, 7, 0, 0, 1, 9, 0],
                 [23, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                 [37, 35, 0, 0, 0, 0, 3, 21, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == [1, 2, 3, 4, 5, 15])

assert(solution([[0, 7, 0, 17, 0, 1, 0, 5, 0, 2],
                 [0, 0, 29, 0, 28, 0, 3, 0, 16, 0],
                 [0, 3, 0, 0, 0, 1, 0, 0, 0, 0],
                 [48, 0, 3, 0, 0, 0, 17, 0, 0, 0],
                 [0, 6, 0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == [4, 5, 5, 4, 2, 20])

assert(solution([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == [1, 1, 1, 1, 1, 5])

assert(solution([[1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == [2, 1, 1, 1, 1, 6])

assert(solution([[0, 86, 61, 189, 0, 18, 12, 33, 66, 39],
                 [0, 0, 2, 0, 0, 1, 0, 0, 0, 0],
                 [15, 187, 0, 0, 18, 23, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == [6, 44, 4, 11, 22, 13, 100])

assert(solution([[0, 0, 0, 0, 3, 5, 0, 0, 0, 2],
                 [0, 0, 4, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 4, 4, 0, 0, 0, 1, 1],
                 [13, 0, 0, 0, 0, 0, 2, 0, 0, 0],
                 [0, 1, 8, 7, 0, 0, 0, 1, 3, 0],
                 [1, 7, 0, 0, 0, 0, 0, 2, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == [1, 1, 1, 2, 5])
