class Animal:
    # Constructor method of the Animal class
    def __init__ (self):
        print("Animal Created")
    
    # who am I method for identification of the Animal
    def who_am_i(self):
        print("I am an animal")

    # eat method to display what Animal object eats
    def eat(self):
        print("I am eating")


class Dog(Animal):
    # Initializer/Constructor method for Dog class
    def __init__(self):
        # We are simply calling the parent class initializer
        Animal.__init__(self)
        print("Dog Created")
    
    def who_am_i(self):
        print("I am a Dog")



dog = Animal()
dog.who_am_i()
dog.eat()

dog = Dog()
dog.who_am_i()
dog.eat()
