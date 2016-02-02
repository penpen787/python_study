__author__ = 'PenPen'
#   Q1010 다리놓기 문제
#   https://www.acmicpc.net/problem/1010
import sys

# Factorial Function
def factorial(a, b=1):
    if a == b:
        return 1
    return a * factorial(a-1, b)

answers = []
points = []

# Get Inputs
n = int(input())
for i in range(n):
    read = lambda: sys.stdin.readline()
    t1, t2 = map(int, read().split())
    points.append([t1, t2])

# Solve The problem
for i in range(n):
    left = points[i][0]
    right = points[i][1]
    # nCr
    if left == right:
        print(1)
    else:
        t1 = factorial(right, left)
        t3 = factorial(right-left)
        ans = t1 / t3
        print(int(ans))