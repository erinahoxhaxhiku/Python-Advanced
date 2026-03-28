class Animal:
    def __init__(self, typeOfAnimal, raca, ngjyra):
        self.typeOfAnimal = typeOfAnimal
        self.raca = raca
        self.ngjyra=ngjyra

    def greet(self):
        print("The type of the Animal is ", self.typeOfAnimal, ". The race is ", self.raca, ". And the color is ", self.ngjyra)


dog = Animal("Dog", "Husky", "White")
cat = Animal("Cat", "British", "Gray")

print(dog.greet())
print(cat.greet())
