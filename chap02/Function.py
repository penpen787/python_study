import sys
_author__ = "Kyunghun Jeon"


# define function
def add(a , b):
    return a+b

aa = add(3, 4)
print(aa)  # 7


# # check reference count
a = 823423442583
print(sys.getrefcount(a))  # 4
print(sys.getrefcount(823423442583))  # 4

# delete this variable
del a
print(sys.getrefcount(823423442583))  # 3
