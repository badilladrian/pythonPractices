# Now lets get to serious bussiness. OOP-
from datetime import date


class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Persona object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Persona is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Persona("Juan", 123)
person2 = Persona.fromBirthYear("Pedro", 34)


print(person1.age)
print(person2.age)

# print the result
print(Persona.isAdult(22))
