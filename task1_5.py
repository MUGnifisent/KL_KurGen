import math

from main import create_personal_numbers
from utils.task1_utils import *

# test
def print_bin(number):
    i = 0
    for c in number:
        i += 1
        print(c, end="")
        if i == 4:
            print(" ", end="")
            i = 0
    print("")

# test
def print_bin_k(number, control_pos):
    j = 0
    for i in range(len(number)):
        if (i+1) in control_pos[j:]:
            print(f"({number[i]})", end="")
            j += 1
        else:
            print(number[i], end="")
    print("")


def print_table(matrix):
    max_space = 4
    for row in matrix:
        for item in row:
            space = ""
            for i in range(max_space-len(str(item))+1):
                space += " "
            if item == None:
                print("     ", end="")
            else:
                print(f"{item}", end=space)
        print("")


def full_form_bin(number, bits):
    l = len(number)
    if l < bits:
        for i in range(bits-l):
            number = f"0{number}"
    return number


def log2(x):
    return (math.log10(x) / math.log10(2))


def is_power_of_2(n):
	return (math.ceil(log2(n)) == math.floor(log2(n)))


def get_control_pos(number):
    l = []
    for i in range(len(number)):
        if is_power_of_2(i+1):
            l.append(i+1)
    return l


def convert_to_list(number, control_pos):
    l = []
    j = 0
    for i in range(0, len(control_pos)+len(number)):
        if (i+1) in control_pos[j:]:
            l.append(0)
            j += 1
        else:
            l.append(int(number[i-j]))
    return l.copy()


def task1_5(pn):
    numberHex = f"{pn[0][0]}{pn[0][1]}{pn[7][0]}{pn[7][1]}"
    numberHex = "3553"
    numberBin = hexadecimal_to_binary(numberHex, "")[0]
    
    numberBin = full_form_bin(numberBin, 16)
    controlPositions = get_control_pos(numberBin)
    numberBinLst = convert_to_list(numberBin, controlPositions)
    numberLen = len(numberBinLst)
    
    binIndeces = []
    for i in range(1, numberLen+1):
        binIndeces.append(list(full_form_bin(bin(i)[2:], 5))) # remove 5 constant
    
    # Fill check matrix
    checkMatrix = []
    row = []
    for i in range(len(binIndeces[0])): # range(5)
        for j in range(len(binIndeces)):
            row.append(int(binIndeces[j][i]))
        checkMatrix.append(row.copy())
        row.clear()

    j = 0
    for i in range(1, numberLen+1):
        if i in controlPositions[j:]:
            row.append(f"k{i}")
            j += 1
        else:
            row.append(f"i{i}")
    
    checkMatrix.append(row.copy())
    row.clear()
    checkMatrix.append(numberBinLst)

    failureBitsLst = [None] * numberLen
    failureBitsLst[18] = int(not numberBinLst[18])
    checkMatrix.append(failureBitsLst)
    


    

    # k1 = 0
    # index = 1
    # while index <= 21:
    #     k1 ^= numberBin[index-1]
    #     index += 2

    print(numberHex)
    print(controlPositions)
    print_bin(numberBin)
    print(numberBinLst)
    print_bin_k(numberBinLst, controlPositions)
    print_table(checkMatrix)








if __name__ == '__main__':
    personalNumbers, listedLetters = create_personal_numbers()
    print(f"Букви, отримані з вашого імені:\n{listedLetters}")
    print(f"Цифри, перетворені через конвертаційну таблицю з вибраних букв:\n{personalNumbers}")
    splitter()
    task1_5(personalNumbers)
