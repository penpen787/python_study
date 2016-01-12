__author__ = 'PenPen'
# IO Examples
a = b = 'STR'

# print function
print("1", a, "b", b)  # 공백이 사이에 추가됨
print("1" + a + "b" + str(b))

# print with 'END' keyword
print("a", end = "ENDED\n")  # aENDED

# separator
print(1,2,3,4,5, sep = ', ')

# Console Input
a = input()

# Console Output
print(a)

# Type Casting
b = int(input())
print(type(b))
