#!/usr/bin/env python3

# run with:
# cat ../input/day07.txt | ./day07-02.py

import sys, math
from functools import partial
from operator import sub

input = list(map(int, list(map(str, sys.stdin))[0].split(',')))

# can't think of anything better than bruteforce check

def tri(x):
    return (x+1) * x // 2

def total_fuel(lst, target):
    return sum(map(tri, map(abs, map(partial(sub, target), lst))))

output = min(map(partial(total_fuel, input), range(min(input), max(input))))

print("Output: {output}".format(output=output))
