import matplotlib.pyplot as plt
import numpy as np
s = {3 + 3j, 4 + 2j, 2 + 1j, 2.5 + 4j, 3.25 + 2.5j}
print('select operations:')
print('1:Addition of 2 complex numbers')
print('2:plot points from a set of complex number')
print('3:translation')
print('4:scaling')
print('5:Rotation')
print('6:conjugate')
print('7:Exit')
while True:
    ch = int(input('Enter choice for operation'))

    if ch == 1:
        c1 = complex(input('enter 1st complex number'))
        c2 = complex(input('enter 2nd complex number'))
        print('Addition of 2 complex number c1 and c2= ', c1 + c2)

    if ch == 2:
        s1 = s
        print(s1)

    if ch == 3:
        c = complex(input('Enter a complex no for translation:'))
        s1 = {x + c for x in s}

    if ch == 4:
        scale = float(input('Enter scale point:'))
        s1 = {x * scale for x in s}

    if ch == 5:
        angle = int(input('Enter angle of rotation 90/180/270'))
        if angle == 90:
            s1 = {x * 1 for x in s}
        if angle == 180:
            s1 = {x * (-1) for x in s}
        if angle == 270:
            s1 = {x * 1j * (-1) for x in s}
        else:
            print('invalid angle')