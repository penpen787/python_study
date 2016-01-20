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
print(l)  #  [1, 5, 3]

