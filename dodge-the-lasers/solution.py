import decimal


def solution(s):
    decimal.getcontext().prec = 101

    def solve(n):
        if n == 0:
            return 0

        np = int((decimal.Decimal(2).sqrt() - 1) * n)

        return n * np + n * (n + 1) // 2 - np * (np + 1) // 2 - solve(np)

    return str(solve(int(s)))


assert solution("77") == "4208"
assert solution("5") == "19"
