# Example from https://wikidocs.net/28
#  Only structure


class Simple:
    pass  # 'pass' does nothing


class EasyClass(object):
    simpleVariable = "Simple Variable"
    v1 = 1
    v2 = 2

    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def add(self):
        return self.v1 + self.v2

#  in Python. 'self' indicates the instance itself
class  Service:
    secret = "영구는 배꼽이 두개"

    def sum(self, a, b):
        result = a + b
        print("Hey %s , %s + %s = %s" % (self.name, a, b, result))

    def setName(self, name):
        self.name = name

simple = Simple()
simple.v1 = "aa"
print(simple.v1)


c1 = EasyClass(3, 5)
result = c1.add()
print(c1.simpleVariable)
print(result)

id = Service()
id.setName("Hun")
id.sum(2, 5)

Service.sum(id, 3, 7)  # call method from the Class directly, need to indicate the target instance

print(type(Service()))


id.addedField = "addedFIELD"
print(id.addedField)

id2 = Service()
#  print(id2.addedField)  -- Error , no field
