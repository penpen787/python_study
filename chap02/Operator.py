__author__ = 'PenPen'
# 리스트는 [ ] 대괄호로 표현
l = [0, 1, 2]
print(len(l))
print(l)

# 튜플은 소괄호를 사용, 리스트와의 차이점은 튜플은 값의 변경이 불가하다
t = (1, 2, 3)
print(t)
print(t[0])
print(t[-1])
print(t[0:1])
print(t*5)
print(2 in t)

t[0] = 10 # 에러 튜플은 값 변경 안됨



