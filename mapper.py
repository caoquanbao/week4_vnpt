#!/usr/bin/env python3
import sys

# Kích thước ma trận (ở đây 4x4)
N = 4

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    matrix, i, j, value = line.split(",")
    i, j, value = int(i), int(j), int(value)

    if matrix == "A":
        # A[i][j] nhân với B[j][k] => phát cho tất cả k
        for k in range(N):
            print(f"{i},{k}\tA,{j},{value}")
    else:  # matrix == "B"
        # B[j][k] nhân với A[i][j] => phát cho tất cả i
        for row in range(N):
            print(f"{row},{j}\tB,{i},{value}")
