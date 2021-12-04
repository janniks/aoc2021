#!/usr/bin/env python3

# run with:
# cat ../input/day04.txt | ./day04-01.py

import sys

input = list(map(str.strip, map(str, sys.stdin)))

numbers = list(map(int, input[0].split(',')))

boards = list('#'.join(input[1:]).split("##"))
boards = [list(map(int, filter(None, c.split(' '))))
          for b in boards for c in b.split('#')]

print(boards)
print(numbers)

# create inverted index of numbers in boards?
