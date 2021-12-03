#!/usr/bin/env python3

# run with:
# cat ../input/day03.txt | ./day03-02.py

import sys
from collections import Counter

input = list(map(str, sys.stdin))

# ho recursive
def rec_gen(neg=False):
    def rec(arr, bit=0):
        if len(arr) == 1:
            return int(arr[0], 2)

        cnt = Counter({'0': 0, '1': 0})
        lst0, lst1 = [], []

        for a in arr:
            value = a[bit]
            cnt[value] += 1
            (lst0, lst1)[int(value)].append(a)

        return rec((lst0, lst1)[(cnt['1']>=cnt['0'])^neg], bit+1)
    return rec

# generate rating functions via higher-order function
oxy_rating = rec_gen()
co2_rating = rec_gen(neg=True)

output = oxy_rating(input) * co2_rating(input)

print("Output: {output}".format(output=output))
