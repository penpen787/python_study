# Example from https://wikidocs.net/28
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        return self.first + self.second

    def mul(self):
        return self.first * self.second


a1 = FourCal()
a1.setdata(3, 7)
print(a1.sum())


class MyName:
    lastname = "Jeon"

    def __init__(self, lastname):
        self.lastname = lastname

    def setname(self, firstname):
        self.fullname = firstname + self.lastname

name0 = MyName()
print(MyName.lastname)
MyName.lastname = "Lee"  # does it mean 'prototype' ??
print(MyName.lastname)

name1 = MyName()
print(name1.lastname)  # Lee
name1.lastname = "Kim"
print(name1.lastname)  # Kim
print(MyName.lastname)  # Lee

MyName.lastname = "Park"
print(name1.lastname)  # Kim
print(MyName.lastname)  # Park

print(name0.lastname)  # Park

