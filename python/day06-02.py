#!/usr/bin/env python3

# run with:
# cat ../input/day06.txt | ./day06-02.py

import sys

input = list(map(int, list(map(str, sys.stdin))[0].split(',')))

prev = [0] * 9
for l in input:
    prev[l] += 1

# simulate
days = 256
for d in range(days):
    nxt = [0] * 9
    for n in range(9):
        if n == 0:
            nxt[6] += prev[0]
            nxt[8] += prev[0]
        else:
            nxt[n-1] += prev[n]
    prev = nxt

output = sum(prev)

print("Output: {output}".format(output=output))
