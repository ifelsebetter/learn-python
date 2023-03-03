'''

Operator

1. Addition
2. Sunbtraction
3. Multiplication
4. Division
5. Exponetial
6. Modulos
7. Floor division

'''

def normal_operator():
    addition = 32 + 54
    subtraction = 42 - 19
    multiplication = 12 * 14
    division = 72 / 6
    exponential = 5 ** 3
    modulo = 45 % 7
    floor_division = 33 // 4

    print(addition, subtraction, multiplication, division, exponential, modulo, floor_division)

def assign_operator():
    a = 4 * 3
    
    b = 1
    b += 5
    
    c = 14
    c -= 3

    x = 6
    x *= 4

    y = 35
    y /= 7

    z = 14
    z %= 8

    i = 54
    i //= 5

    print(a, b, c, x, y, z, i)

def relational_operator():
    a = 1 * 2 > 2 * 2

    b = 1 * 2 < 2 * 2

    c = 3 * 5 <= 15

    x = 15 >= 5 * 3

    y = 15 == 3 * 5
    
    z = 15 != 5 * 3

    print(a, b, c, x, y, z)

