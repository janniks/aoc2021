#!/usr/bin/env python3

# run with:
# cat ../input/day01.txt | ./day01-01.py

import sys
from operator import sub, gt
from functools import partial

input = list(map(int, sys.stdin))
output = sum(map(partial(gt, 0), map(sub, input, input[1:])))

print("Output: {output}".format(output=output))
