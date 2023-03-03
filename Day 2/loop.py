# for loop & while loop

def loop():

    for i in range(5):
        print("*" * (i + 1))

    weekday = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    for day in weekday:
        print("It is ", day, " !")

    for letter in "hello world":
        print(letter)

    user_input = ""
    while user_input != "unlock":
        user_input = input(("Enter password : "))
    print("Password correct the password is " + user_input)

    week = ["mon", "tue", "wed", "thurs", "fri", "sat", "sun"]
    for days1 in week:
        if day == "fri":
            break
        print(day1)
    print("All week day")

    user_pass = ""
    while True:
        user_pass = input(("Enter password : "))
        if user_pass == "unlock":
            break
    print("Password is correct and it is " + user_pass)

    weeks = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    for day2 in weeks:
        if day2 == "saturday":
            continue
        print("Day is ", day2)
    print("What day is missing")

    weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday"]
    weekends = ["saturday", "sunday"]

    for i in weekdays:
        pass
    for day3 in weekends:
        print("Today is ", day3)
