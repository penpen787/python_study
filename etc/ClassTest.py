#  Only structure
class Simple:
    pass


class EasyClass(object):
    simpleVariable = "Simple Variable"
    v1 = 1
    v2 = 2

    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def add(self):
        return self.v1 + self.v2


simple = Simple()
simple.v1 = "aa"
print(simple.v1)


c1 = EasyClass(3, 5)
result = c1.add()
print(c1.simpleVariable)
print(result)
