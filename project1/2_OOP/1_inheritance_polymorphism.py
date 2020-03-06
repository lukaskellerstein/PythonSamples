class Animal:
    def __init__(self):
        print("Animal created")

    def whoami():
        print("I am an animal")

    def eat():
        print("i am eating")

    # abstract method
    def speak():
        raise NotImplementedError("Subclass must implement this abstract method")


# Inheritance
class Dog(Animal):
    def __init__(self):
        # call super class
        Animal.__init__(self)
        print("Dog created")

    # Polymorphysm - override
    def whoami():
        print("I am a dog")

    def speak():
        print("BARK BARK")

    def eat():
        print("dog is eating")

    # Polymorphysm - overload - PYTHON DOESN'T HAVE A METHOD OVERLOADING
    # def eat(text):
    #     print(f"dog eating {text}")


# Inheritance
class Cat(Animal):
    def __init__(self):
        # call super class
        Animal.__init__(self)
        print("Cat created")

    # Polymorphysm - override
    def whoami():
        print("I am a cat")

    def speak():
        print("MEOW MEOW")

    def eat():
        print("cat is eating")

    # Polymorphysm - overload - PYTHON DOESN'T HAVE A METHOD OVERLOADING
    # def eat(text):
    #     print(f"dog eating {text}")
