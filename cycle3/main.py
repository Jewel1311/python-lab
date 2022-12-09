from mypackage import circle
from mypackage import rectangle
from mypackage.threedgraphics import *

print("\n-----From mypackage ----\n")

r = int(input('Enter the radius of circle : '))
l = int(input('Enter the length of rectangle : '))
b= int(input('Enter the breadth of rectangle : '))

ca = circle.cirarea(r)
ra = rectangle.rectarea(l,b)

print("Area of circle : ",ca)
print("Area of rectangle : ",ra)

print("\n----From 3d graphics----\n")

sr = int(input('Enter the radius of sphere : '))
cl = int(input('Enter the length of cuboid : '))
cb= int(input('Enter the breadth of cuboid : '))
ch= int(input('Enter the height of cuboid : '))

cb_area = cuboid.cuboidarea(cl,cb,ch)
sp_area = sphere.spherearea(sr)

print("Area of Cuboid: ",cb_area)
print("Area of Sphere : ",sp_area)





