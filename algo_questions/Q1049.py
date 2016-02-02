__author__ = 'PenPen'
# Q1049 기타줄 해결
import sys
# Init Variables

# Get Inputs
read = lambda: sys.stdin.readline()
n, cn = map(int, read().split())

tp, p = 1000

for i in range(n):
    read1 = lambda: sys.stdin.readline()
    t1, t2 = map(int, read().split())
    if t1 < tp:
        tp = t1
    if t2 < p:
        p = t2

# Solve the Problem
