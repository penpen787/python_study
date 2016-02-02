__author__ = 'PenPen'
#   Q1004 어린왕자문제
import sys
import math

def getdt(x1, y1, x2, y2):
    return math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))

inputs = []  # [[[-5 1 12 1][1 1 8][-3 -1 1] ...]]

# Test Values
# inputs = [[[-5, 1, 12, 1], [[1, 1, 8], [-3, -1, 1], [2, 2, 2], [5, 5, 1], [-4, 5, 1], [12, 1, 1], [12, 1, 2]]], [[-5, 1, 5, 1], [[0, 0, 2]]]]
# n = 2

# Get Inputs
n = int(input())
for i in range(n):
    # Get the 4 points
    read = lambda: sys.stdin.readline()
    x1, y1, x2, y2 = map(int, read().split())
    tmpList = [[x1, y1, x2, y2]]
    tmpCnt = int(input())
    tmpInnerList = []
    for j in range(tmpCnt):
        readInner = lambda: sys.stdin.readline()
        xx, yy, rr = map(int, read().split())
        tmpInnerList.append([xx, yy, rr])
    tmpList.append(tmpInnerList[:])
    inputs.append(tmpList[:])

# Solve The problem
for i in range(n):
    ans = 0
    x1, y1, x2, y2 = inputs[i][0]
    for j in range(len(inputs[i][1])):
        # Check which one is shorter the two points and the circle radius
        xx = inputs[i][1][j][0]
        yy = inputs[i][1][j][1]
        rr = inputs[i][1][j][2]
        # TO DO : Refactoring
        dt1 = getdt(xx, yy, x1, y1)
        dt2 = getdt(xx, yy, x2, y2)
        circleType = 0
        if dt1 <= rr:
            circleType += 1
        if dt2 <= rr:
            circleType += 1

        if circleType != 2:
            ans += circleType
    print(ans)
