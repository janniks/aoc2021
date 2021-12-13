#!/usr/bin/env python3

# run with:
# cat ../input/day14.txt | ./day14-02.py

import sys
from collections import Counter
from operator import itemgetter

def pairs(lst): return zip(lst[:-1], lst[1:])

input = list(map(str.strip, sys.stdin))

template = input[0]
rules = dict(map(lambda d: (tuple(d[0]), d[1]), map(lambda r: r.split(' -> '), input[2:])))

prev_counts = Counter(template)
prev_pairs = Counter(pairs(template))

for _ in range(40):
    nxt_counts = prev_counts.copy()
    nxt_pairs = Counter()

    for pair in prev_pairs:
        b = rules[pair] # assuming it exists
        a, c = pair

        nxt_pairs[(a, b)] += prev_pairs[pair]
        nxt_pairs[(b, c)] += prev_pairs[pair]

        nxt_counts[b] += prev_pairs[pair]

    prev_counts = nxt_counts
    prev_pairs = nxt_pairs

prev_counts = sorted(prev_counts.items(), key=itemgetter(1))

print('Output:', prev_counts[-1][1] - prev_counts[0][1])
