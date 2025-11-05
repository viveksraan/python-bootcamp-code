class Dog():
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return self.name+ " woof!"
    
class Cat():
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return self.name+ " meow!"
    
niko = Cat("niko")
felix = Dog("felix")
# print(niko.speak())
# print(felix.speak())

for pet in [niko, felix]:
    print(type(pet))
    print(pet.speak())