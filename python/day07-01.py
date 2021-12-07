#!/usr/bin/env python3

# run with:
# cat ../input/day07.txt | ./day07-01.py

import sys, math
from functools import partial
from operator import sub

input = list(map(int, list(map(str, sys.stdin))[0].split(',')))

# can't think of anything better than bruteforce check

def total_fuel(lst, target):
    return sum(map(abs, map(partial(sub, target), lst)))

best = math.inf
for target in range(min(input), max(input)):
    pot = total_fuel(input, target)
    if pot > best: break
    best = pot

print(f"for-loop: {best}")

output = min(map(partial(total_fuel, input), range(min(input), max(input))))

print("Output: {output}".format(output=output))
