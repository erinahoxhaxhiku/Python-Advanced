from ChallengeDay import Challenge as abstractmethod

# Abstract base class
class Person():
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

# Property for weight
@property
def weight(self):
    return self.weight

@weight.setter
def weight(self, value):
    if value > 0:
        self.weight = value
    else:
        print("Weight must be positive!")

# Property for height

    @property

    def height(self):

        return self.height



    @height.setter

    def height(self, value):

        if value > 0:

            self.height = value

        else:

            print("Height must be positive!")



    @abstractmethod

    def calculate_bmi(self):

        pass



    @abstractmethod

    def get_bmi_category(self):

        pass



    def print_info(self):

        bmi = self.calculate_bmi()

        category = self.get_bmi_category()

        print(f"\nName: {self.name}")

        print(f"Age: {self.age}")

        print(f"BMI: {bmi:.2f}")

        print(f"Category: {category}")

# Adult class

class Adult(Person):

    def calculate_bmi(self):

        return self.weight / (self.height ** 2)



    def get_bmi_category(self):

        bmi = self.calculate_bmi()

        if bmi < 18.5:

            return "Underweight"

        elif bmi < 25:

            return "Normal weight"

        elif bmi < 30:

            return "Overweight"

        else:

            return "Obese"





