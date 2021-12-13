#!/usr/bin/env python3

# run with:
# cat ../input/day14.txt | ./day14-01.py

import sys
from collections import Counter
from itertools import filterfalse
from operator import itemgetter

input = list(map(str.strip, sys.stdin))
template = input[0]
rules = dict(map(lambda r: tuple(r.split(' -> ')), input[2:]))

def windows(lst, n=2):
    for i in range(len(lst)-n+1):
        yield lst[i:i+n]

def gap_index(g, n=2):
    return g * n + 1

for i in range(10):
    gapped = list(' '.join(list(template)))

    for g, gap in enumerate(windows(template)):
        gapped[gap_index(g)] = rules.get(gap, ' ')

    template = ''.join(filterfalse(str.isspace, gapped))

counts = sorted(Counter(''.join(template)).items(), key=itemgetter(1))

print('Output:', counts[-1][1] - counts[0][1])
