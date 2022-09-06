from math import log      #ver 0.0.10

from utils.task1_utils import *


def task1_1(pn):
    print("\n\n1.1")
    splitter()
    number = float(f"{pn[0][0]}{pn[0][1]}{pn[1][0]}.{pn[1][1]}{pn[7][0]}{pn[7][1]}") # for output
    numberBD = int(f"{pn[0][0]}{pn[0][1]}{pn[1][0]}") # before dot
    numberAD = int(f"{pn[1][1]}{pn[7][0]}{pn[7][1]}") # after dot
    print(f"Десяткове число, трансформоване з персональних кодів - {number}")
    splitter()

    print("Проведемо перетворення з десяткового числа до шіснадцяткового.")
    numberBD = decimal_to_hexadecimal_bd(numberBD) 
    print(f"Число до коми дорівнює {numberBD}")
    numberAD = decimal_to_hexadecimal_ad(numberAD)
    print(f"Число після коми дорівнює {numberAD}")
    number = str(f"{numberBD}.{numberAD}")
    print(f"З'єднане число дорівнює {number}")
    splitter()

    print("Проведемо перетворення з шіснадцяткового числа до двійкового.")
    numberBD, numberAD, number = hexadecimal_to_binary(numberBD, numberAD)
    print(f"Після очищення від непотрібних нулів та скорочення, число дорівнює {number}")
    splitter()

    print("Проведемо перетворення з двійкового числа до вісімкового.")
    number, numberBD, numberAD = binary_to_octo(numberBD, numberAD)
    print(f"Після форматування, число дорівнює {number}")
    splitter()
    

def task1_2(pn):
    print("\n\n1.2")
    splitter()
    number = f"{pn[0][0]}{pn[0][1]}{pn[1][0]}.{pn[1][1]}{pn[7][0]}{pn[7][1]}"
    numberBD = f"{pn[0][0]}{pn[0][1]}{pn[1][0]}"
    numberAD = f"{pn[1][1]}{pn[7][0]}{pn[7][1]}"
    print(f"Шіснадцяткове число, трансформоване з персональних кодів - {number}")
    splitter()

    print("Проведемо перетворення з шіснадцяткового числа до десяткового.")
    number, numberBD, numberAD = hexadecimal_to_decimal(numberBD, numberAD)
    print(f"Число до коми дорівнює {numberBD}")
    print(f"Після проведеного округлення, число після коми дорівнює {numberAD}")
    print(f"З'єднане число дорівнює {number}")
    splitter()

    number = str(f"{pn[0][0]}{pn[0][1]}{pn[1][0]}.{pn[1][1]}{pn[7][0]}{pn[7][1]}")
    numberBD = str(f"{pn[0][0]}{pn[0][1]}{pn[1][0]}")
    numberAD = str(f"{pn[1][1]}{pn[7][0]}{pn[7][1]}")

    print("Проведемо перетворення з шіснадцяткового числа до двійкового.")
    numberBD, numberAD, number = hexadecimal_to_binary(numberBD, numberAD)
    print(f"Після очищення від непотрібних нулів та скорочення, число дорівнює {number}")
    splitter()

    print("Проведемо перетворення з двійкового числа до вісімкового.")
    number, numberBD, numberAD = binary_to_octo(numberBD, numberAD)
    print(f"Після форматування, число дорівнює {number}")
    splitter()



def task1_3(pn):
    print("\n\n1.3")
    number = int(f"{pn[0][0]}{pn[0][1]}{pn[1][0]}{pn[1][1]}{pn[7][0]}{pn[7][1]}")
    p = [2,3,5,7,11,13,17]
    P = 510510
    numberMod = []
    B = [0,0,0,0,0,0,0]
    sum = 0
    for i in range(7):
        print("p" + str(i+1) + " = " + str(p[i]))

    print("P = p1 * p2 * p3 * p4 * p5 * p6 * p7 = " + str(P))

    for i in range(7):
        numberMod.append(number % p[i])
        print(str(number) + " mod " + str(p[i]) + " = " + str(numberMod[i]))


    for i in range(7):
        x = 1
        while True:
            B[i] = int(x * (P/p[i]))
            print("B" + str(i+1) + " = " + str(x) + " * " + str(P) + "/" + str(p[i]) + " = " + str(B[i]) + " [" + str(int(B[i] % p[i])) + "]")
            x+=1
            if B[i] % p[i] == 1:
                break
    
    for i in range(7):
        sum += numberMod[i] * B[i]

    print("( " + str(numberMod[0]) + " * " + str(B[0]) + " + " + str(numberMod[1]) + " * " + str(B[1]) + " + " + str(numberMod[2]) + " * " + str(B[2]) + " + " + str(numberMod[3]) + " * " + str(B[3])
    + " + " + str(numberMod[4]) + " * " + str(B[4]) + " + " + str(numberMod[5]) + " * " + str(B[5]) + " + " + str(numberMod[6]) + " * " + str(B[6]) + ") = " + str(sum) + " mod " + str(P) + " = " + str(sum % P))


def task1_4(listedLetters, pn):
    print("\n\n1.4")
    n = 8 #number of symbols

    for i in range(8):
        p[i].sym = listedLetters[i]
        p[i].k = int(f"{pn[i][0]}{pn[i][1]}")

    totalK = 0
    
    for i in range(8):
        totalK += p[i].k

    totalPro = 1

    #p[0].pro = 0.3
    #p[1].pro = 0.19
    #p[2].pro = 0.12
    #p[3].pro = 0.11
    #p[4].pro = 0.1
    #p[5].pro = 0.08
    #p[6].pro = 0.06
    #p[7].pro = 0.04

    for i in range(8):
        p[i].pro = round(p[i].k / totalK,2);
        totalPro -= p[i].pro
        if i == 7:
            p[i].pro = round(p[i].pro + totalPro,2)

    displayRaw(n, p)
    print("\n\t\t", "Σ=" + str(totalK), "\t\t", 1,"\t",end='') #підсумовує деякі дані

    sortByProbability(n, p, ['000', '001', '010', '011', '100', '101', '110', '111'])
 
    for i in range(n):
        p[i].top = -1
 
    

    shannon(0, n - 1, p)
    displayCalculated(n, p)

    H = 0
    print("\n\nH = -(", end='')
    for i in range(8):
        H += p[n-1-i].pro * log(p[n-1-i].pro,2)
        if i != 7:
            print(str(p[n-1-i].pro) + " * log2(" + str(p[n-1-i].pro) + ") + ", end='')
        else:
            print(str(p[n-1-i].pro) + " * log2(" + str(p[n-1-i].pro) + "))=" + str(-H),end='')
    H = -H
    lEffective = 0
    print("\nL сер. не еф = 3")
    print("L сер. еф = ", end='')

    for i in range(8):
        k = 0
        for j in range(p[n-1-i].top+1):
            if(p[n-1-i].arr[j] == 1 or p[n-1-i].arr[j] == 0):
                k += 1
        lEffective += k * p[n-1-i].pro
        if i != 7:
            print(str(k) + " * " + str(p[n-1-i].pro) + " + ", end='')
        else:
            print(str(k) + " * " + str(p[n-1-i].pro) + " = " + str(lEffective), end='')
    
    if lEffective < H and H < 3:
        print("\n\nL сер. еф < H < L сер. не еф")
    elif lEffective > H and lEffective < 3:
         print("\n\nH < L сер. еф < L сер. не еф")
    elif lEffective > H and lEffective > 3:
         print("\n\nH < L сер. не еф < L сер. еф ")

    effectiveOutput = ""
    notEffectiveOutput = ""

    for i in range(8):
        for j in range(8):
            if listedLetters[i] == p[j].sym:
                for x in range(p[j].top+1):
                    effectiveOutput += str(p[j].arr[x])
                notEffectiveOutput += str(p[j].notEffectiveCode)
        effectiveOutput += " "
        notEffectiveOutput += " "
    print("\n\n")
    print(effectiveOutput + "  " + str(len(effectiveOutput) - effectiveOutput.count(' ')) + "біт")
    print(notEffectiveOutput + "  " + str(len(notEffectiveOutput) - notEffectiveOutput.count(' ')) + "біт")