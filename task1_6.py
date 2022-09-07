from main import create_personal_numbers
from utils.task1_utils import *


def task1_6(pn):
    pass


if __name__ == '__main__':
    personalNumbers, listedLetters = create_personal_numbers()
    print(f"Букви, отримані з вашого імені:\n{listedLetters}")
    print(f"Цифри, перетворені через конвертаційну таблицю з вибраних букв:\n{personalNumbers}")
    splitter()
    task1_6(personalNumbers)
    