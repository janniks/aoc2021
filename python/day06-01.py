#!/usr/bin/env python3

# run with:
# cat ../input/day06.txt | ./day06-01.py

import sys

input = list(map(int, list(map(str, sys.stdin))[0].split(',')))

prev = [0] * 9
for l in input:
    prev[l] += 1

# simulate
days = 80
for d in range(days):
    z = prev.pop(0)
    prev = prev + [z]
    prev[6] += z

output = sum(prev)

print("Output: {output}".format(output=output))
