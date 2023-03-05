def oop():
    class Bankaccount:
        pass
    account = Bankaccount()
    print(type(account))

    class shape:
        def __init__(self):
            self.color = "black"

        def get_color(self):
            return self.color

    class circle(shape):
        def __init__(self):
            super().__init__()
            self.radius = 10

        def get_radius(self):
            return self.radius

    cl = circle()
    print("Radius of circle is ", cl.get_radius())
    print("Color is ", cl.get_color())

    class Shape:
        def __init__(self):
            self.color = "black"

    class Rectangle(Shape):
        pass

    class Circle(Shape):
        color = "blue"

    S1 = Rectangle()
    print("Color of Rectangle S1: ", S1.color)
    S2 = Circle()
    print("Color of Circle S2: ", S2.color)

    class Bankaccount:
        backaccount_type = "Saving Account"

        def __init__(self, owner, amount=0):
            self.owner = owner
            self.amount = amount

    account1 = Bankaccount("Joe")
    print(account1.owner)
    print(account1.amount)

    class Bankaccount:
        backaccount_type = "Saving Account"

        def __init__(self, owner, amount=0):
            self.owner = owner
            self.amount = amount

        def __str__(self):
            return "The account of user {} has {} Baht in total".format(self.owner, self.amount)

    account2 = Bankaccount("John")
    print(str(account2))


oop()
