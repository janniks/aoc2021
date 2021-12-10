#!/usr/bin/env python3

# run with:
# cat ../input/day10.txt | ./day10-01.py

import sys

input = list(map(str.strip, sys.stdin))

chunk_map = { '(': ')', '[': ']', '{': '}', '<': '>' }
score_map = dict(zip(chunk_map.values(), [3, 57, 1197, 25137]))

opens = set(chunk_map.keys())

def chunk_check(line):
    stack = []
    for l in line:
        if l in opens:
            stack.append(l) # open chunk
        elif l == chunk_map[stack[-1]]:
            stack.pop() # close chunk
        else:
            return l # corrupt
    return None # fine or incomplete

output = sum(map(score_map.get, filter(None, map(chunk_check, input))))

print("Output: {output}".format(output=output))
