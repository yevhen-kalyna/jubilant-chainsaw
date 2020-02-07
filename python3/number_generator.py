import random

class Generate():
    @staticmethod
    def random_int16():
        return random.randrange(-32768, 32768, 1)
    @staticmethod
    def given(number):
        return number
