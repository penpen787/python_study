#  Test class for example FUNCTION
#  Python pass the parameter by 'Call by Object Reference or Call by Sharing'
def f(t):
    t = 10

a = 20
f(a)
print(a)  # 20, not Call by Reference


def listchange(list):
    list[1] = 5 # list 참조값을 받아, list 두번째 값을 직접 변경, 즉 list 에 대한 직접 참조값은 변하지 않는다 ! 유의할 것 !

l = [1, 2, 3]
listchange(l)
print(l)  #  [1, 5, 3]0

x = 10  # Global scope
y = 11  # Global scope

def foo():
    # Global variable
    global gvar  # make it global variable, can be accessed in outer scope
    gvar = 30
    x = 20  # foo 함수의 Local, bar 함수에 Enclosing Function Local - 함수를 내포하는 또 다른 함수 영역

    def bar():
        a = 30  # Local : 함수 내에 정의된 지역 변수
        print(a, x, y)
    bar()  # 30 20 11
    x = 40
    bar()  # 30 40 11

foo()
print(gvar)
gvar = 10;
print(gvar)
foo()
print(gvar)

# non local
def outer():
    x = 1
    def inner():
        nonlocal x  # 함수 outer의 x를 사용하게 됨
        x = 2  # 함수 inner의 지역변수가 아님, 변수체인에 따라 바로 위 outer의 x를 가리킴
        print("inner: ", x)
    inner()
    print("outer: ", x)

outer()