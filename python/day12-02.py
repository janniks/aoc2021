#!/usr/bin/env python3

# run with:
# cat ../input/day12.txt | ./day12-02.py

import sys
from collections import defaultdict, namedtuple
from itertools import filterfalse, tee
from typing import Counter

input = list(map(lambda x: tuple(x.strip().split('-')), sys.stdin))

def partition(pred, iterable): # itertools recipe
    t1, t2 = tee(iterable)
    return list(filterfalse(pred, t1)), list(filter(pred, t2))

segments = defaultdict(lambda:set())
for start, end in input:
    segments[start].add(end)
    segments[end].add(start) # also add reverse direction

Part = namedtuple("PathPart", ['previous', 'cave'])

paths = []
curr = [Part([], 'start')]
while curr:
    nxt = []
    for p in curr:
        visited_small = Counter(filter(str.islower, p.previous+[p.cave]))
        def reenterable(cave):
            if cave == 'start': return False
            if cave.isupper(): return True
            return 2 not in visited_small.values() # no duplicate small cave visit yet

        no_reentry = set(filterfalse(reenterable, p.previous))
        destinations = segments[p.cave] - no_reentry
        nxt.extend(Part(p.previous+[p.cave], d) for d in destinations)
    curr, ended = partition(lambda p: p.cave == 'end', nxt)
    paths.extend(map(lambda p: p.previous[1:], ended))

output = len(paths)

print("Output: {output}".format(output=output))
