def solution(n):
    memo = {}

    def solve(n, k, depth):
        if (n, k) in memo:
            return memo[n, k]

        ret = 0

        if n == 0 and depth > 1:
            ret = 1
        elif n <= 0 or k <= 0:
            ret = 0
        else:
            ret = solve(n, k - 1, depth + 1) + solve(n - k, k - 1, depth + 1)

        memo[n, k] = ret

        return ret

    return solve(n, n, 0)

assert solution(3) == 1
assert solution(4) == 1
assert solution(5) == 2
assert solution(6) == 3
assert solution(7) == 4
assert solution(8) == 5
assert solution(200) == 487067745
