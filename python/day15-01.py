#!/usr/bin/env python3

# run with:
# cat ../input/day15.txt | ./day15-01.py

import sys, math
from collections import defaultdict, deque
from operator import itemgetter

input = list(map(lambda x: list(map(int, list(x))), map(str.strip, sys.stdin)))
cavern = dict(((x, y), r) for x, a in enumerate(input) for y, r in enumerate(a))
n = len(input) # square cavern

def sides(c):
    x, y = c
    return [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]

start = (0, 0)

costs = defaultdict(lambda:math.inf)
costs[start] = 0

queue = deque([start])
visited = set(queue)

while queue:
    curr = queue.popleft()

    neighs = list(filter(itemgetter(1), map(lambda s: (s, cavern.get(s)), sides(curr))))
    queue.extend(set(map(itemgetter(0), neighs)) - visited)

    for neigh in neighs:
        c, r = neigh
        costs[c] = min(costs[c], r+costs[curr])
        visited.add(c)

print('Output:', costs[(n-1, n-1)])
