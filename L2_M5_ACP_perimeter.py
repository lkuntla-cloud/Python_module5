import math
class circle:
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        print("The area of the circle is: ", math.pi*(self.radius**2))
    def perimeter(self):
        print("The perimeter if the circle is: ",math.pi*self.radius*2)
x=int(input("Enter the radius of the circle: "))
result=circle(x)
result.area()
result.perimeter()