def solution(total_lambs):
    tmp = total_lambs
    cur = 1
    generous = 0
    while tmp >= cur:
        tmp -= cur
        cur *= 2
        generous += 1

    tmp = total_lambs
    cur, prev = 1, 0
    stingy = 0
    while tmp >= cur:
        tmp -= cur
        prev, cur = cur, prev + cur
        stingy += 1

    return stingy - generous
