__author__ = 'PenPen'
import sys

# Init Variables
xMinValue = 10001
yMinValue = 10001

# Get Inputs
read = lambda: sys.stdin.readline()
x, y, w, h = map(int, read().split())

# Solve The Problem
if x < (w - x):
    xMinValue = x
else:
    xMinValue = (w - x)

if y < (h - y):
    yMinValue = y
else:
    yMinValue = (h - y)

if xMinValue < yMinValue:
    print(xMinValue)
else:
    print(yMinValue)
