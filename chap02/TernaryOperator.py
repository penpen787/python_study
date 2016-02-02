__author__ = 'PenPen'
a = 5
x = a * 2 if a > 5 else a / 2
print(x)

b = 10
print((b/2, b*2, b*3)[2])
# print((print("True"),print("False")[True]))

def add(a, b):
    return a+b
def sub(a, b):
    return a-b
test = 1
print((add, sub)[test](2, 3))


boolean = (True == 0)
print(boolean)