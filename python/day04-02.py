#!/usr/bin/env python3

# run with:
# cat ../input/day04.txt | ./day04-02.py

import sys
from functools import partial
import numpy as np

def flat(x):
    return [z for y in x for z in y]

input = list(map(str.strip, map(str, sys.stdin)))

numbers = list(map(int, input[0].split(',')))

boards = list('#'.join(input[2:]).split("##"))
boards = [[list(map(int, filter(None, c.split(' ')))) for c in b.split('#')]
          for b in boards]

# it's 1 AM, this is not going to be efficient or beautiful

def contains_empty(b):
    return 0 in list(map(len, map(list, map(partial(filter, None), b))))

def is_bingo(b):
    bc = b.copy()
    bn = np.transpose(np.array(b.copy()))

    return contains_empty(bc) or contains_empty(bn)

prev = -1
magic = 0
unsum = 0
won = set()

for n in numbers:
    for b in boards:

        for i in range(0, 5):
            for j in range(0, 5):
                if b[i][j] == n:
                    b[i][j] = None # Mark!

        # Check!
        if is_bingo(b) and prev != id(b) and id(b) not in won:
            magic = n
            unsum = sum(filter(None, flat(b.copy())))
            prev = id(b)
            won.add(id(b))


# create inverted index of numbers in boards? no time

output = magic * unsum

print("Output: {output}".format(output=output))
