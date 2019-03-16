import random


class Robot:

    def __init__(self):
        self.name = Robot.__generate_name(self)

    def reset(self):
        random.seed(random.randint(0, 10000000))
        self.name = Robot.__generate_name(self)

    def __generate_name(self):
        a_letter = self.__random_letter()
        another_letter = self.__random_letter()
        return a_letter + another_letter + self.__random_number()

    @staticmethod
    def __random_letter():
        return chr(random.randint(65, 65 + 26))

    @staticmethod
    def __random_number():
        return str(random.randint(0, 999)).zfill(3)
