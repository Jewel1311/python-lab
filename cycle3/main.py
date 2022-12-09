from mypackage import circle
from mypackage import rectangle
from mypackage.threedgraphics import *

print("\n-----From mypackage ----\n")

r = int(input('Enter the radius of circle : '))
l = int(input('Enter the length of rectangle : '))
b= int(input('Enter the breadth of rectangle : '))

ca = circle.cirarea(r)
cp = circle.cirper(r)
ra = rectangle.rectarea(l,b)
rp = rectangle.rectper(l,b)

print("\nArea of circle : ",ca)
print("Perimeter of circle : ",cp)
print("Area of rectangle : ",ra)
print("Perimeter of rectangle : ",rp)


print("\n----From 3d graphics----\n")

sr = int(input('Enter the radius of sphere : '))
cl = int(input('Enter the length of cuboid : '))
cb= int(input('Enter the breadth of cuboid : '))
ch= int(input('Enter the height of cuboid : '))

cb_area = cuboid.cuboidarea(cl,cb,ch)
cb_per = cuboid.cuboidperi(cl,cb,ch)
sp_vol = sphere.spherevol(sr)
sp_area = sphere.spherearea(sr)


print("\nArea of Cuboid: ",cb_area)
print("Perimeter of Cuboid: ",cb_area)
print("Volume of Sphere : ",sp_vol)
print("Area of Sphere : ",sp_area)





