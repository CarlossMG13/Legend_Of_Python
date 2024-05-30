from math import sqrt

#inputs
side1 = int(input('1st Short side of the triangle: '))
side2 = int(input('2nd Short side of the triangle: '))

#Operations
c = (side1 ** 2) + (side2 ** 2)
hypotenuse = sqrt(c)

print(hypotenuse)

