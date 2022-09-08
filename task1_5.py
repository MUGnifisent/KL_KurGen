from main import create_personal_numbers
from utils.task1_utils import *


def print_bin(number):
    i = 0
    for c in number:
        i += 1
        print(c, end="")
        if i == 4:
            print(" ", end="")
            i = 0


def full_form_bin(number, bits):
    l = len(number)
    if l < bits:
        for i in range(bits-l):
            number = f"0{number}"
    return number


def task1_5(pn):
    numberHex = f"{pn[0][0]}{pn[0][1]}{pn[7][0]}{pn[7][1]}"
    numberHex = "3553"
    numberBin = hexadecimal_to_binary(numberHex, "")[0]
    
    numberBin = full_form_bin(numberBin, 16)


    print(numberHex)
    print_bin(numberBin)






if __name__ == '__main__':
    personalNumbers, listedLetters = create_personal_numbers()
    print(f"Букви, отримані з вашого імені:\n{listedLetters}")
    print(f"Цифри, перетворені через конвертаційну таблицю з вибраних букв:\n{personalNumbers}")
    splitter()
    task1_5(personalNumbers)
