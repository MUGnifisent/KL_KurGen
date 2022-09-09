import math
import random

from main import create_personal_numbers
from utils.task1_utils import *


def print_table(matrix, posoffbit):
    print("Перевірочна матриця (таблиця)")
    max_space = 4
    for row in matrix:
        for item in row:
            space = ""
            for i in range(max_space-len(str(item))+1):
                space = f"{space} "
            print(f"{item}", end=space)
        print("")
    for _ in range((max_space+1)*(posoffbit-1)-1):
        print(" ", end="")
    bit = int(not matrix[len(matrix)-1][posoffbit-1])
    print(f"({bit})")
    print(f"Припустимо, що помилка сталася у біті i{posoffbit}")
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


def random_fail_bit_pos(number_len, control_pos):
    l = []
    for i in range(number_len):
        if (i+1) not in control_pos:
            l.append(i+1)
    print(l)
    return random.choice(l)


def calc_k1(number_bin_lst, label):
    # Not flexible (only for 16-bit numbers)
    outStrCalcValues = ""
    outStrCalc = f"{label}1  = "
    k1 = 0
    index = 3
    while index <= 21:
        i = number_bin_lst[index-1]
        k1 ^= i
        if index != 3:
            outStrCalcValues = f"{outStrCalcValues} ⊕ "
            outStrCalc = f"{outStrCalc} ⊕ "
        outStrCalcValues = f"{outStrCalcValues}{i}"
        outStrCalc = f"{outStrCalc}i{index}"
        index += 2
    outStrCalc = f"{outStrCalc} = {outStrCalcValues} = {k1}"
    return (k1, outStrCalc)


def calc_k2(number_bin_lst, label):
    # Not flexible (only for 16-bit numbers)
    outStrCalcValues = ""
    outStrCalc = f"{label}2  = "
    k2 = 0
    index = 3
    change = False
    while index <= 19:
        i = number_bin_lst[index-1]
        k2 ^= i
        if index != 3:
            outStrCalcValues = f"{outStrCalcValues} ⊕ "
            outStrCalc = f"{outStrCalc} ⊕ "
        outStrCalcValues = f"{outStrCalcValues}{i}"
        outStrCalc = f"{outStrCalc}i{index}"
        if change:
            change = not change
            index += 1
        else:
            change = not change
            index += 3
    outStrCalc = f"{outStrCalc} = {outStrCalcValues} = {k2}"
    return (k2, outStrCalc)


def calc_k4(number_bin_lst, label):
    # Not flexible (only for 16-bit numbers)
    outStrCalcValues = ""
    outStrCalc = f"{label}4  = "
    k4 = 0
    for index in range(5, 8):
        i = number_bin_lst[index-1]
        k4 ^= i
        if index != 5:
            outStrCalcValues = f"{outStrCalcValues} ⊕ "
            outStrCalc = f"{outStrCalc} ⊕ "
        outStrCalcValues = f"{outStrCalcValues}{i}"
        outStrCalc = f"{outStrCalc}i{index}"
    for index in range(12, 16):
        i = number_bin_lst[index-1]
        k4 ^= i
        outStrCalcValues = f"{outStrCalcValues} ⊕ {i}"
        outStrCalc = f"{outStrCalc} ⊕ i{index}"
    for index in range(20, 22):
        i = number_bin_lst[index-1]
        k4 ^= i
        outStrCalcValues = f"{outStrCalcValues} ⊕ {i}"
        outStrCalc = f"{outStrCalc} ⊕ i{index}"
    outStrCalc = f"{outStrCalc} = {outStrCalcValues} = {k4}"
    return (k4, outStrCalc)


def calc_k8(number_bin_lst, label):
    # Not flexible (only for 16-bit numbers)
    outStrCalcValues = ""
    outStrCalc = f"{label}8  = "
    k8 = 0
    for index in range(9, 16):
        i = number_bin_lst[index-1]
        k8 ^= i
        if index != 9:
            outStrCalcValues = f"{outStrCalcValues} ⊕ "
            outStrCalc = f"{outStrCalc} ⊕ "
        outStrCalcValues = f"{outStrCalcValues}{i}"
        outStrCalc = f"{outStrCalc}i{index}"
    outStrCalc = f"{outStrCalc} = {outStrCalcValues} = {k8}"
    return (k8, outStrCalc)


def calc_k16(number_bin_lst, label):
    # Not flexible (only for 16-bit numbers)
    outStrCalckValues = ""
    outStrCalc = f"{label}16 = "
    k16 = 0
    for index in range(17, 22):
        i = number_bin_lst[index-1]
        k16 ^= i
        if index != 17:
            outStrCalckValues = f"{outStrCalckValues} ⊕ "
            outStrCalc = f"{outStrCalc} ⊕ "
        outStrCalckValues = f"{outStrCalckValues}{i}"
        outStrCalc = f"{outStrCalc}i{index}"
    outStrCalc = f"{outStrCalc} = {outStrCalckValues} = {k16}"
    return (k16, outStrCalc)


def task1_5(ll, pn):
    print("\n\n1.5")
    splitter()
    
    numberHex = f"{pn[0][0]}{pn[0][1]}{pn[7][0]}{pn[7][1]}"
    numberBin = bin(int(numberHex, 16))[2:]
    numberBin = full_form_bin(numberBin, 16)
    
    print(f"{ll[0]}: {numberHex[0:2]}; {ll[7]}: {numberHex[2:4]}; {numberHex}={numberBin}\n")
    
    controlPositions = get_control_pos(numberBin)
    numberBinLst = convert_to_list(numberBin, controlPositions)
    numberLen = len(numberBinLst)
    
    # Binary indeces for check matrix
    binIndeces = []
    for i in range(1, numberLen+1):
        binIndeces.append(list(full_form_bin(bin(i)[2:], 5))) # remove constant "5"
    
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
    checkMatrix.append(numberBinLst.copy())
    
    # Calculate k1
    k1, outStrCalck1 = calc_k1(numberBinLst, 'k')
    # Calculate k2
    k2, outStrCalck2 = calc_k2(numberBinLst, 'k')
    # Calculate k4
    k4, outStrCalck4 = calc_k4(numberBinLst, 'k')
    # Calculate k8
    k8, outStrCalck8 = calc_k8(numberBinLst, 'k')
    # Calculate k16
    k16, outStrCalck16 = calc_k16(numberBinLst, 'k')

    checkMatrix[-1][0] = k1
    checkMatrix[-1][1] = k2
    checkMatrix[-1][3] = k4
    checkMatrix[-1][7] = k8
    checkMatrix[-1][15] = k16

    # Imitation of a failure bit
    posOfFailBit = random_fail_bit_pos(numberLen, controlPositions)
    numberBinLst[posOfFailBit-1] = int(not numberBinLst[posOfFailBit-1])

    # Calculate K1
    k1_, outStrCalcK1 = calc_k1(numberBinLst, 'K')
    # Calculate K2
    k2_, outStrCalcK2 = calc_k2(numberBinLst, 'K')
    # Calculate K4
    k4_, outStrCalcK4 = calc_k4(numberBinLst, 'K')
    # Calculate K8
    k8_, outStrCalcK8 = calc_k8(numberBinLst, 'K')
    # Calculate K16
    k16_, outStrCalcK16 = calc_k16(numberBinLst, 'K')
    
    # Find position of the failure bit
    posOfFailBit_ = f"{k16_^k16}{k8_^k8}{k4_^k4}{k2_^k2}{k1_^k1}"
    outStrCalcFailBitPos = "K ⊕ k = (K16 ⊕ k16)(K8 ⊕ k8)(K4 ⊕ k4)(K2 ⊕ k2)(K1 ⊕ k1) = " \
        f"({k16_} ⊕ {k16})({k8_} ⊕ {k8})({k4_} ⊕ {k4})({k2_} ⊕ {k2})({k1_} ⊕ {k1}) = {posOfFailBit_}"

    print_table(checkMatrix, posOfFailBit)
    print(outStrCalck1)
    print(outStrCalck2)
    print(outStrCalck4)
    print(outStrCalck8)
    print(outStrCalck16)
    print("")
    print(outStrCalcK1)
    print(outStrCalcK2)
    print(outStrCalcK4)
    print(outStrCalcK8)
    print(outStrCalcK16)
    print("")
    print(outStrCalcFailBitPos)
    print(f"Значення {posOfFailBit_} вказує на те, що помилка сталася в {int(posOfFailBit_, 2)} біті ({posOfFailBit_}={int(posOfFailBit_, 2)}).")


if __name__ == '__main__':
    personalNumbers, listedLetters = create_personal_numbers()
    print(f"Букви, отримані з вашого імені:\n{listedLetters}")
    print(f"Цифри, перетворені через конвертаційну таблицю з вибраних букв:\n{personalNumbers}")
    task1_5(listedLetters, personalNumbers)
    splitter()
