#!/usr/bin/env python3

# run with:
# cat ../input/day10.txt | ./day10-02.py

import sys
from functools import reduce
from itertools import count

input = list(map(str.strip, sys.stdin))

chunk_map = { '(': ')', '[': ']', '{': '}', '<': '>' }
score_map = dict(zip(chunk_map.keys(), count(1)))

opens = set(chunk_map.keys())

def chunk_check(line):
    stack = []
    for l in line:
        if l in opens:
            stack.append(l) # open chunk
        elif l == chunk_map[stack[-1]]:
            stack.pop() # close chunk
        else:
            return None # corrupt
    return list(reversed(stack)) # fine or incomplete

def score(missing):
    return reduce(lambda acc, m: acc * 5 + score_map[m], missing, 0)

scores = sorted(map(score, filter(None, map(chunk_check, input))))

output = scores[int(len(scores)/2)]

print("Output: {output}".format(output=output))
