#!/usr/bin/env python3

# run with:
# cat ../input/day15.txt | ./day15-02.py

import sys, math
from collections import defaultdict
from functools import partial
from itertools import filterfalse
from operator import contains

import heapq

input = list(map(lambda x: list(map(int, list(x))), map(str.strip, sys.stdin)))
cavern = dict(((x, y), r) for x, a in enumerate(input) for y, r in enumerate(a))
n = len(input) # small, square cavern

def sides(c):
    x, y = c
    return [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]

def inc(x, diff):
    incd = (x + diff) % 9
    return incd if incd != 0 else 9

# fill bigger cavern
small_cavern = list(cavern.items())
for i in range(5):
    for j in range(5):
        if i + j == 0: continue
        for c, r in small_cavern:
            x, y = c
            cavern[(i*n + x, j*n + y)] = inc(r, i+j)

start = (0, 0)

costs = defaultdict(lambda:math.inf)
costs[start] = 0

heap = [(0, start)]
visited = set()

while heap:
    r, curr = heapq.heappop(heap)

    if curr in visited: continue
    visited.add(curr)

    neighs = list(filter(partial(contains, cavern), sides(curr)))
    for neigh in filterfalse(partial(contains, visited), neighs):
        costs[neigh] = min(costs[neigh], cavern[neigh]+costs[curr])
        heapq.heappush(heap, (costs[neigh], neigh))

print('Output:', costs[(n*5-1, n*5-1)])
