def funcwithdefaultargument(a, step = 1):
    return a + step

b = 1
b = funcwithdefaultargument(b)
print(b)

b = funcwithdefaultargument(b, 10)
print(b)

# variable argument
c = funcwithdefaultargument(step =  50, a = 7)
print(c)

def varg(a, *arg):
    print(a, arg)

varg(1, 10, 30)

# 정의되지 않은 키워드 처리
def f(width, height, **kw):
    print(width, height)
    print(kw)

f(width= 10, height = 5, depth = 10, dimension = 3)
# 10 5
# {'depth': 10, 'dimension': 3}

