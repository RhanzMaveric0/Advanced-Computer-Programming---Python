class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says Woof!")
    
    def info(self):
        print(f"{self.name} is {self.age} years old")

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

dog1.bark()
dog1.info()

dog2.bark()
dog2.info()

print()

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

cat = Cat("Whiskers")
cat.speak()
