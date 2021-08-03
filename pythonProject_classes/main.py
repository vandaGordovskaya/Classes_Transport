""" Класс Transport.

    Подумать об атрибутах и методах, дополнить класс ими.
    Подумать и реализовать класс наследники класса Transport(минимум 4),
    Переопределить методы и атрибуты для каждого класса.
"""


class Transport:
    operations = "move"

    def __init__(self):
        self.myName = self.__class__.__name__

    def what_i_can(self):
        about_me = f"I am from {self.myName} class and I can {self.operations}"
        return about_me


class WaterTransport(Transport):
    operations = ["move", "swim"]

    def what_i_can(self):
        return f"I am from {self.myName} class. I can " \
               f"{self.operations[0]} and {self.operations[1]}."


class AirTransport(Transport):
    operations = ["move", "flight in air"]

    def what_i_can(self):
        print("I am from %s class. I can %s and %s."
              % (self.myName, self.operations[0], self.operations[1]))


class LandTransport(Transport):
    operations = ["move"]

    def what_i_can(self):
        print("I am from %s class. I can %s."
              % (self.myName, self.operations[0]))


class SpaceTransport(Transport):
    operations = "flight in space"

    def what_i_can(self):
        about_me = "I am from %s class. I can %s."
        print(about_me % (self.myName, self.operations))


transport = Transport()
boat = WaterTransport()
car = LandTransport()
plane = AirTransport()
rocket = SpaceTransport()

print(transport.what_i_can())
print(boat.what_i_can())
car.what_i_can()
plane.what_i_can()
rocket.what_i_can()
