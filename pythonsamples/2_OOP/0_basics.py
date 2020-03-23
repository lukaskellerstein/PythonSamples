# -----------------------------------
# CLASS
# -----------------------------------


class Dog:

    id = ""
    name = ""
    description = ""

    # constructor WITHOUT additional parameters
    def __init__(self):
        print("constructor")

    def makeSound(self):
        print(f"{self.name} is barking on you")


class Vehicle:

    id = ""

    # constructor WITH additional parameters
    def __init__(self, wheelCount):
        self.whelsCount = wheelCount


class Circle:

    # class object attributes (can be accessed via class name only - as static variables)
    name = ""
    pi = 3.14159

    def __init__(self, radius=1):
        self.name = "Circle-1"
        self.radius = radius
        self.area = radius * radius * self.pi  # accessed via self

    def get_circumference(self):
        print(self.name)
        return self.radius * self.pi * 2  # accessed via self


class Circle2:

    # class object attributes (can be accessed via class name only - as static variables)
    name = ""
    pi = 3.14159

    def __init__(self, radius=1):
        self.name = "Circle-2"
        self.radius = radius
        self.area = radius * radius * Circle.pi  # accessed via class name

    def get_circumference(self):
        print(self.name)
        return self.radius * Circle.pi * 2  # accessed via class name


c1 = Circle()
c1.get_circumference()

c2 = Circle2(20)
c2.get_circumference()
