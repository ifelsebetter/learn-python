# Import & using module

import random
import math

def module():

    print(random.randint(1, 10))

    myList = ["Joe", 1, True, "blue", 15.48]
    print(random.randint(0, len(myList)-1))

    print(random.sample(range(0, 101), 10))

    print("Ceiling value of 13.45 is ", math.ceil(13.45))

    print("Square root value of 100 is", math.sqrt(100))

    print("Absolute value of -14 is", math.fabs(-14))

    weight = int(input('What is your weight(kg): '))
    height = int(input('What is your height(cm): '))
    print('Your BMI is: ',int(weight / ((height/100) ** 2)))

module()
