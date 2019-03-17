import random
import math
import string


class Robot:

    def __init__(self):
        self.name = Robot.__generate_name(self)

    def reset(self):
        random.seed(self.name)
        self.name = Robot.__generate_name(self)

    def __generate_name(self):
        a_letter = self.__random_letter()
        another_letter = self.__random_letter()
        a_three_digit_number = self.__three_digit_number_as_string(self)
        return a_letter + another_letter + a_three_digit_number

    @staticmethod
    def __random_letter():
        alphabet = list(string.ascii_uppercase)
        return random.choice(alphabet)

    @staticmethod
    def __three_digit_number_as_string(self):
        return str(self.__random_number(3)).zfill(3)

    @staticmethod
    def __random_number(number_of_digits):
        return random.choice(range(1, int(math.pow(10, number_of_digits))))
