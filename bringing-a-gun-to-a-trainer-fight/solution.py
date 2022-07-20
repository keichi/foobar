from math import atan2, sqrt

def solution(dim, my, enem, max_dist):
    def dist(p):
        return sqrt((p[0] - my[0]) ** 2 + (p[1] - my[1]) ** 2)

    pos = []
    angles = set([])

    for tx in range((my[0] + max_dist + dim[0] - 1) / dim[0]):
        for ty in range((my[1] + max_dist + dim[1] - 1) / dim[1]):
            m = ((my[0] if tx % 2 == 0 else dim[0] - my[0]) + tx * dim[0],
                 (my[1] if ty % 2 == 0 else dim[1] - my[1]) + ty * dim[1])
            e = ((enem[0] if tx % 2 == 0 else dim[0] - enem[0]) + tx * dim[0],
                 (enem[1] if ty % 2 == 0 else dim[1] - enem[1]) + ty * dim[1])

            pos.append((m[0], m[1], False))
            pos.append((-m[0], m[1], False))
            pos.append((m[0], -m[1], False))
            pos.append((-m[0], -m[1], False))

            pos.append((e[0], e[1], True))
            pos.append((-e[0], e[1], True))
            pos.append((e[0], -e[1], True))
            pos.append((-e[0], -e[1], True))

    del pos[0]
    pos.sort(key=dist)

    count = 0

    for p in pos:
        if dist(p) > max_dist:
            break

        angle = atan2(p[1] - my[1], p[0] - my[0])

        if angle not in angles and p[2]:
            count += 1

        angles.add(angle)

    return count
