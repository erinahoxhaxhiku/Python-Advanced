class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Some generic animal sound")
    def description(self):
        print(f"This is animal named {self.name}.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        super().sound()

        print("Woof!")

    def description(self):
        super().description()
        print(f"Breed: {self.breed}")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color=color

        def sound(self):
            super().sound()
            print("Meow")

        def description(self):
            super().description()
            print(f"Color:{self.color}")

animal = Animal("Generic Animal")
print(animal.sound())
print(animal.description())

dog = Dog("Rex" ,"Golden Retriever")
print(dog.sound())
print(dog.description())

cat = Cat("Whiskers","white")
print(cat.sound())
print(cat.description())
