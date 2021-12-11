#!/usr/bin/env python3

# run with:
# cat ../input/day11.txt | ./day11-01.py

import sys
from collections import Counter

input = list(map(lambda l: list(map(int, list(l.strip()))), sys.stdin))
n = len(input)
matrix = {(x, y): e for x, l in enumerate(input) for y, e in enumerate(l)}

def flat(x): return [z for y in x for z in y]

def adjacent(c):
    x, y = c
    return [(a, b) for a in range(x-1, x+2)
                   for b in range(y-1, y+2)
                   if (a, b) != c and a in range(0, n) and b in range(0, n)]

def simulate(matrix):
    def flashy(c): return matrix[c] > 9

    matrix.update({c: e+1 for c, e in matrix.items()})

    flashed = set()
    flashers = set(filter(flashy, matrix.keys()))

    while flashers:
        flashed |= flashers
        # important: needs to allow duplicates (counter rather than set)
        neigh = Counter(flat(map(adjacent, list(flashers))))
        matrix.update({c: matrix[c]+v for c, v in neigh.items() if c not in flashed})
        flashers = set(filter(flashy, neigh)) - flashed

    matrix.update({c: 0 for c in flashed})

    return len(flashed)

output = sum([simulate(matrix) for _ in range(100)])

print("Output: {output}".format(output=output))
