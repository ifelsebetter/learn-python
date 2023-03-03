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
    for dayss in week:
        if day == "fri":
            break
        print(day)
    print("All week day")

    user_pass = ""
    while True:
        user_pass = input(("Enter password : "))
        if user_pass == "unlock":
            break
    print("Password is correct and it is " + user_pass)

    weeks = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    for days in weeks:
        if days == "saturday":
            continue
        print("Day is ", day)
    print("What day is missing")

    weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday"]
    weekends = ["saturday", "sunday"]

    for i in weekdays:
        pass
    for daysss in weekends:
        print("Today is ", day)
