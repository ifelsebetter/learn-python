'''

set is group of element in array but it cannot be repeat
work like math set

'''

def set_list():

    int_set = {1, 2, 3, 3, 4, 5}
    str_set = {"a", "b", "c", "a", "b", "d"}
    mix_set = {1, 3.25, "hi", (6, 7, 8)}
    my_set1 = set([1, 2, 3, 4, 3])
    my_set2 = set((1, 2, 3, 4, 2))

    print(int_set, str_set, mix_set, my_set1, my_set2)

    num1_set = {1, 2, 3, 5}
    num1_set.add(4)
    print(num1_set)

    num2_set = {2, 4, 6}
    num2_set.update([1, 3, 5])
    print(num2_set)

    num3_set = {1, 2, 3, 4, 5}
    num3_set.remove(3)
    print(num3_set)

    num4_set = {10, 20, 30, 40, 50}
    num4_set.clear()
    print(num4_set)

    set1 = {1, 2, 3}
    set2 = {2, 4, 5}

    set1.union(set2)
    print(set1)

    set3 = {1, 3, 4}
    set4 = {1, 2, 5}

    set3.intersection(set4)
    print(set3)

    set5 = {1, 2, 3}
    set6 = {1, 2, 4}

    set5.difference(set6)
    print(set5)

    set7 = {1, 2, 3}
    set8 = {1, 2, 4}

    set7.symmetric_difference(set8)
    print(set7)

    set9 = {1, 2, 3}
    set10 = {1, 2, 4}

    print(3 in set9, 2 in set10)

