# -*- coding: utf-8 -*-


def solve(N, test_data=None):
    l = [[0] * N for _ in range(N)]

    for i in range(N):
        row = input()
        for j, cell in enumerate(row):
            l[i][j] = cell

    ret = [[0] * N for _ in range(N)]

    for t in range(N):
        for u in range(N-1, -1, -1):
            ret[t][u] = l[u][t]

    for r in ret:
        print("".join(reversed(r)))


if __name__ == '__main__':
    N = int(input())
    solve(N)