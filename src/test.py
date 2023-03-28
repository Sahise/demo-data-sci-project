#Trying to calculate both the Area and Circ. of a circle with a function and calculate both by inputting the radius

def Circle(r):
    pi = 3.14
    d = r/2
    circle_area = pi * r**2
    circle_circ = 2*pi * r
    return circle_area, circle_circ

print (Circle(7))


#Trying to use Pytagoras formula to calculate the C with a function

def Triangle(a, b):
    a = a**2
    b = b**2
    c = a + b
    c = pow(c, 1/2)
    return c

print (Triangle(3, 7))