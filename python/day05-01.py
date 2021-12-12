#!/usr/bin/env python3

# run with:
# cat ../input/day05.txt | ./day05-01.py

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

count_2s = len(list(filter(partial(le, 2), flat(state))))

output = count_2s

print("Output: {output}".format(output=output))
