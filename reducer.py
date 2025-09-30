#!/usr/bin/env python3
import sys
from collections import defaultdict

current_key = None
values = []

def process(key, values):
    # values: list of ("A", j, val) or ("B", j, val)
    A_vals = defaultdict(int)
    B_vals = defaultdict(int)
    for tag, j, val in values:
        if tag == "A":
            A_vals[j] += val
        else:
            B_vals[j] += val
    total = 0
    for j in set(A_vals.keys()).union(B_vals.keys()):
        total += A_vals[j] * B_vals[j]
    print(f"{key}\t{total}")

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    key, rest = line.split("\t")
    tag, j, val = rest.split(",")
    j, val = int(j), int(val)

    if current_key == key:
        values.append((tag, j, val))
    else:
        if current_key is not None:
            process(current_key, values)
        current_key = key
        values = [(tag, j, val)]

# xử lý key cuối
if current_key is not None:
    process(current_key, values)
