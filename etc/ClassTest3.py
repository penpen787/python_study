# Inheritance example
class Parent:
    lastname = "Jeon"

    def showname(self):
        print(self.lastname)



class Child(Parent):
    firstname = "KH"

    def showname(self):
        print(self.firstname + self.lastname)

    #  Pyhon supports Operator Overloading just like C++
    def __add__(self, other):
        print("Add operator" + self.firstname + other.firstname)

    # def __mul__(self, other):
    #     print("Multiply operator" + self.firstname + other.nonexistfield)

child = Child()
child.showname()
fullname = child.firstname + child.lastname
print(fullname)

child2 = Child()
child2.firstname = "YOU"
child + child2

# AttributeError: 'Child' object has no attribute 'nonexistfield'
# child * child2
