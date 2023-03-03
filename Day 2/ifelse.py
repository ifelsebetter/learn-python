# if else statement

def check_condition():

    guess_num = [10, 20, 30, 40, 50]
    guess1 = eval(input("Enter number : "))
    if guess1 in guess_num:
        print("Your guess correct")
    print("Your guess is incorrect")

    num_list = [10, 20, 30, 40, 50]
    guess2 = eval(input("Enter number : "))
    if guess2 in num_list:
        print("Your guess is correct")
    else:
        print("Your guess is incorrect")
    print("Try again next time")

    num1_list = [1, 3, 5, 7, 9]
    num2_list = [2, 4, 6, 8, 19]
    guess3 = eval(input("Enter number : "))
    if guess3 in num1_list:
        print("Your guess is in first list")
    elif guess3 in num2_list:
        print("Your guess is in second list")
    else:
        print("Make new guess next time")

    num3_list = [10, 20, 30, 40, 50]
    num4_list = [60, 70, 80, 90, 100]
    guess4 = eval(input("Enter number : "))
    if guess4 < 100:
        if guess4 in num3_list:
            print("Your guess is in list 1")
        elif guess4 in num4_list:
            print("Your guess is in list 2")
        else:
            print("Your guess is wrong")
    elif guess4 > 100:
        print("Your guess is to high")
    else:
        print("Your guess is incorrect")

    print("Try again until you guess it correct")

