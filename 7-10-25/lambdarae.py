area_square=lambda a:a*a
a=int(input("Enter the side of the square"))
print(area_square(a))
area_rectangle=lambda l,b:l*b
l=int(input("Enter the length of the rectangle"))
b=int(input("Enter the breadth of the rectangle"))
print(area_rectangle(l,b))
area_triangle=lambda h,b:(1/2)*b*h
b=int(input("Enter the base of the triangle"))
h=int(input("Enter the height of the triangle"))
print(area_triangle(b,h))


