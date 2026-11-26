class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f"{self.name} says Woof!")

animal1 = Animal("Charlie")
animal1.speak()

dog1 = Dog("Buddy", "Golden Retriever")
dog1.speak()
print(dog1.breed)