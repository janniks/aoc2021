#!/usr/bin/env python3

# run with:
# cat ../input/day01.txt | ./day01-02.py

import sys
from operator import sub, gt
from functools import partial

def windows(lst, n=3):
    for i in range(len(lst)-n+1):
        yield lst[i:i+n]

input = list(map(int, sys.stdin))
output = sum(map(partial(gt, 0), map(sub, map(sum, windows(input[:-1])), map(sum, windows(input[1:])))))
# output = sum(map(partial(gt, 0), map(lambda x: sum(x[:-1]) - sum(x[1:]), windows(input, 4)))) # alternative

print("Output: {output}".format(output=output))
