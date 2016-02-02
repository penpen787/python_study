__author__ = 'PenPen'
#   Q1032 명령프롬프트 문제

# Init Variables
inputList = []
lastSamePos = 0

# Test Values
# inputList = ['config.inf', 'config.sys', 'config.res']
inputList = ['zonfig.inf', 'aonfig.sys', 'aonfig.res']

n = 3


# Get Inputs
# n = int(input())
# for i in range(n):
#     line = input()
#     inputList.append(line)

print(inputList)
# Solve the Problem
isSame = True
cnt = 0
# 한 문자열 길이
for i in range(len(inputList[0])):
    isSame = True
    s = inputList[0][i]
    # 입력된 문자행 수
    for j in range(n):
        if j == 0:
            continue
        if s != inputList[j][i]:
            cnt = i-1
            isSame = False
    # 뒤부터 검사하여 isSame 이 True라면 그곳까지까 공통
    if not isSame:
        break

print(cnt)
print(inputList[0][0:cnt], end='')
print('?' * (len(inputList[0]) - cnt))

