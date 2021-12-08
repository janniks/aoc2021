#!/usr/bin/env python3

# run with:
# cat ../input/day08.txt | ./day08-02.py

import sys
from itertools import filterfalse, tee

input = list(map(lambda x: (*map(lambda x: map(frozenset, x.strip().split(' ')), x.split('|')),), map(str.strip, sys.stdin)))

def partition(pred, iterable):
    t1, t2 = tee(iterable)
    return list(filterfalse(pred, t1)), list(filter(pred, t2))

def non_unique(num): return len(num) in range(5, 7)

# returns first set in `lst` that is subset of `sub`
def ct(lst, sub): return list(filter(lambda s: sub.issubset(s), lst))[0]

def derive(left):
    [uniq, rem] = partition(non_unique, set(map(frozenset, left)))
    [dl5, dl6] = partition(lambda x: len(x) == 6, rem) # ambiguous digits by length

    h = {} # helper segments
    d = {} # digits
    dl = {len(ud): ud for ud in uniq} # unique digits by length

    d[1] = dl[2]
    d[4] = dl[4]
    d[7] = dl[3]
    d[8] = dl[7]
    d[3] = ct(dl5, d[1])
    h[3] = d[4] & d[3] - d[1]
    d[0] = d[8] - h[3]
    h[1] = d[4] - d[1] - h[3]
    d[5] = ct(dl5, h[1])
    h[4] = d[0] - d[3] - d[4]
    d[6] = ct(dl6, h[3] | h[4])
    h[2] = d[1] - d[6]
    d[9] = ct(dl6, h[3] | h[2])
    d[2] = ct(dl5, h[4])

    return dict(map(reversed, d.items()))

output = sum(map(int, map(lambda x: "".join(map(str, map(derive(x[0]).get, x[1]))), input)))

print("Output: {output}".format(output=output))
