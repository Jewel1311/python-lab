class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        area = self.length * self.breadth
        return area
    
    def perimeter(self):
        perimeter = 2*(self.length + self.breadth)
        return perimeter

    
length1 = int(input("Enter the length of rectangle 1  : "))
breadth1 = int(input("Enter the breadth of rectangle 1 : "))

length2 = int(input("Enter the length of rectangle 2  : "))
breadth2 = int(input("Enter the breadth of rectangle 2 : "))

ob1 = Rectangle(length1, breadth1)
ob2 = Rectangle(length2, breadth2)

area1 = ob1.area()
perimeter1 = ob1.perimeter()

area2 = ob2.area()
perimeter2 = ob2.perimeter()

print("\nArea of rectangle 1 : ", area1)
print("Perimeter of rectangle 1 : ", perimeter1)

print("Area of rectangle 2 : ", area2)
print("Perimeter of rectangle 2 : ", perimeter2)

if area1 == area2:
    print("\nRectangle areas are equal ")
else:
    if area1 < area2:
        print("\nArea of rectangle 1 is greater")
    else:
        print("\nArea of rectangle 2 is greater ")



