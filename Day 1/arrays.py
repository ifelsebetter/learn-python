# Create list and print out element in array

def list():

    weekend = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Print element form arrya. Array will always start at 0
    print(weekend[0])

    name_list = [1, "Wednesday", 0.46, 15, "Hi"]
    print(name_list[3])
    print(name_list[-2])

    everyday = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]

    print(everyday[0:5])
    print(everyday[2:6])
    print(everyday[:2])
    print(everyday[:])

    num1_list = [1, 2, 3, 4, 6, 9]
    num1_list.append(5)
    print(num1_list)

    num2_list = [10, 20, 30, 40, 50]
    num2_list.extend([60, 70, 80, 90])
    print(num2_list)

    num3_list = [1, 2, 4, 6, 7]
    num3_list.insert(3, 5)
    print(num3_list)

    num4_list = [1, 2, 3, 4, 8, 9, 10]
    num3_list[4:3] = [5, 6, 7]
    print(num3_list)

    num5_list = [1, 2, 3, 4, 5]
    num5_list[0] = 7
    print(num5_list)

    num6_list = [10, 20, 30, 40, 50]
    num6_list[0:3] = [1, 2, 3]
    print(num6_list)

    concatenating1_list = ["Mon", "Tue", "Wed", "Thur"]
    concatenating2_list = ["Fri", "Sat", "Sun"]
    concatenating1_list += concatenating2_list
    print(concatenating1_list)

    repeating_list = [1, 2, 3, 4, 5] * 3
    print(repeating_list)

    remove_list = [10, 20, 30, 40, 50]
    remove_list.remove(20)
    print(remove_list)

    pop_list = [1, 2, 3, 4, 5]
    pop_list.pop(2)
    print(pop_list)

    del1_list = [1, 2, 3, 4, 5]
    del del1_list[3]
    print(del1_list)

    del2_list = [10, 20, 30, 40, 50]
    del del2_list[1:3]
    print(del2_list)

    clear1_list = [1, 2, 3, 4, 5]
    clear1_list.clear()
    print(clear1_list)

    clear2_list = [1, 2, 3, 4, 5]
    clear2_list[:] = []
    print(clear2_list)

    check_in_list = [1, 2, 3, 4, 5]
    print(7 in check_in_list)
    print(3 not in check_in_list)

    sort_list = [2, 4, 5, 1, 3]
    sort_list.sort()
    print(sort_list)

    reverse_list = [5, 6, 7, 8, 9, 10]
    reverse_list.reverse()
    print(reverse_list)

