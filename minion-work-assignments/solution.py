from collections import defaultdict

def solution(data, n):
    counts = defaultdict(int)

    for x in data:
        counts[x] += 1

    res = []

    for x in data:
        if counts[x] <= n:
            res.append(x)

    return res


print(solution([1, 2, 3], 0))
print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1))
