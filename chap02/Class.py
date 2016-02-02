__author__ = 'PenPen'
class A:
    scale = 10
    def area(self, width, height):
        return self.scale * width * height
    def seta(self, a):
        self.a = a
    def geta(self):
        return self.a

print(A.scale)
print(A.area)