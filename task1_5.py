from main import create_personal_numbers
from utils.task1_utils import *


def task1_5(pn):
    number_str = f"{pn[0][0]}{pn[0][1]}{pn[7][0]}{pn[7][1]}"
    print(number_str)
    print(decimal_to_binary(int(number_str)))


if __name__ == '__main__':
    personalNumbers, listedLetters = create_personal_numbers()
    print(f"Букви, отримані з вашого імені:\n{listedLetters}")
    print(f"Цифри, перетворені через конвертаційну таблицю з вибраних букв:\n{personalNumbers}")
    splitter()
    task1_5(personalNumbers)
