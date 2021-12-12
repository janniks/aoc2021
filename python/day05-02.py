#!/usr/bin/env python3

# run with:
# cat ../input/day05.txt | ./day05-02.py

import sys
from functools import partial
from operator import le

def flat(x):
    return [z for y in x for z in y]

def flat3(x):
    return [a for y in x for z in y for a in z]

input = list(map(str.strip, sys.stdin))

lines = list(map(lambda x: sorted(map(tuple, map(lambda y: map(int, y.split(',')), x.split(' -> ')))), input))

n = max(map(int, flat3(lines))) + 1

state = [[0] * n for _ in range(n)]

def diag(a, b):
    (ax, ay), (bx, by), (cx, cy) = a, b, a

    dx = 1 if ax < bx else -1
    dy = 1 if ay < by else -1

    yield a
    while (cx, cy) != b:
        cx += dx
        cy += dy
        yield (cx, cy)

# count line fields
for l in lines:
    [(ax, ay), (bx, by)] = l
    if ax == bx:
        # horizontal
        for i in range(ay, by+1):
            state[ax][i] += 1
    elif ay == by:
        # vertical
        for i in range(ax, bx+1):
            state[i][ay] += 1
    else:
        # diagonal
        for x, y in diag(*l):
            state[x][y] += 1

count_2s = len(list(filter(partial(le, 2), flat(state))))

output = count_2s

print("Output: {output}".format(output=output))
