import operator

def solution(xs):
    zero = [x for x in xs if x == 0]
    pos = [x for x in xs if x > 0]
    neg = [x for x in xs if x < 0]

    if not pos and not neg:
        return str(0)

    if len(neg) == 1:
        if zero:
            return str(0)
        else:
            return str(neg[0])

    if len(neg) % 2 == 1:
        neg.remove(max(neg))

    return str(reduce(operator.mul, pos + neg, 1))
