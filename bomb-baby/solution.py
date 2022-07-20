def solution(x, y):
    x, y = int(x), int(y)
    steps = 0

    while x > 1 and y > 1:
        if x % y == 0 or y % x == 0:
            return "impossible"

        if x > y:
            q, x = divmod(x, y)
        else:
            q, y = divmod(y, x)

        steps += q

    return str(steps + max(x, y) - 1)

assert solution("4", "7") == "4"
assert solution("2", "1") == "1"
assert solution("10", "2") == "impossible"
