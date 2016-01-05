__author__ = 'PenPen'
# 여러줄을 한줄로 표현
a = 1; b = 2
if(a == 3) or \
        (b == 2):
    print(b)

# 여러값을 한줄에 치환
c, d = 1, 2
x = y = z = 0
e = 3.5; f = 5.6
e, f = f, e  # 값 교환
c, d, e = e, c, d
print(c, d, e)

# unpacking, 왼쪽부터 대입후 남는거는 몰아서 대입
a, b = 1, 2
print(a, b)
a, *b = [1, 2, 3, 4, 5]  # 1 [2, 3, 4, 5] , 확장된 언팩킹
print(a, b)

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

# t[0] = 10 # 에러 튜플은 값 변경 안됨

# eval 은 내부코드를 실행함, 즉 문자열로 표현된 파이썬 식(expression) 을 인수로 받아 컴파일 코드로 변환
a = 5
b = eval('a + 4')
print(b)  # 9

# exec 는 문자열로 표현된 문(statement)를 받아 파이썬 컴파일 코드로 변환한다
a = 5
exec('a = a + 1')
print(a)  # 6

s = '''  # multi-line string
a = 1
if a> 0:
    print('SUC')
'''
exec(s)
