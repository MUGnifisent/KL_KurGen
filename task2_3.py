from main import create_personal_numbers, pause
from utils.task1_utils import *
from utils.task2_utils import *


def task2_3(pn, ll):
    print('\n\n2.3')


if __name__ == '__main__':
    personalNumbers, listedLetters = create_personal_numbers()
    print(f"Букви, отримані з вашого імені:\n{listedLetters}")
    print(f"Цифри, перетворені через конвертаційну таблицю з вибраних букв:\n{personalNumbers}")
    task2_3(personalNumbers, listedLetters)
    pause()