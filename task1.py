from math import modf, log      #ver 0.0.8


CONVERSION_TABLE={10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F",
"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15,
"000": 0, "001": 1, "010": 2, "011": 3, "100": 4, "101": 5, "110": 6, "111": 7}


def splitter():
    print("<---------->")


def letters_to_numbers(n):
    a = n
    for i in range(len(a)):
        match a[i]:
            case "A":
                print(f"{a[i]} -> {CONVERSION_TABLE['A']}")
                a[i] = CONVERSION_TABLE["A"]
            case "B":
                print(f"{a[i]} -> {CONVERSION_TABLE['B']}")
                a[i] = CONVERSION_TABLE["B"]
            case "C":
                print(f"{a[i]} -> {CONVERSION_TABLE['C']}")
                a[i] = CONVERSION_TABLE["C"]
            case "D":
                print(f"{a[i]} -> {CONVERSION_TABLE['D']}")
                a[i] = CONVERSION_TABLE["D"]
            case "E":
                print(f"{a[i]} -> {CONVERSION_TABLE['E']}")
                a[i] = CONVERSION_TABLE["E"]
            case "F":
                print(f"{a[i]} -> {CONVERSION_TABLE['F']}")
                a[i] = CONVERSION_TABLE["F"]
            case _:
                print("...")
    return a


def decimal_to_binary(d):
    dec = d
    c=""
    while dec > 0 :
        a = dec % 2
        print(f"{dec} / 2 = {dec / 2}[{dec % 2}]")
        c += str(int(a))
        dec //= 2
    c = c[::-1]
    print(f"Результат перед трансформацією в чотиризначне число - {c}")
    return c

def decimal_to_hexadecimal_bd(d):
    dec = d
    c=""
    while dec > 0 :
        a = dec % 16
        print(f"{dec} / 16 = {dec / 16}[{dec % 16}]")
        if a <= 15 and a > 9 :
            c += str(CONVERSION_TABLE[a])
            print(f"Оскільки остача дорівнює {dec % 16}, ми заміняємо її на літеру {CONVERSION_TABLE[a]}")
        else :
            c += str(int(a))
        dec //= 16
    return c[::-1]


def decimal_to_hexadecimal_ad(d):
    dec = float(f"0.{d}")
    c = ""
    for i in range(3):
        frac, whole = modf(dec * 16)
        whole = int(whole)
        frac = round(frac, 5)
        print(f"{dec} * 16 = [{whole}]{str(frac).lstrip('0')}")
        a = whole
        if a <= 15 and a > 9 :
            c += str(CONVERSION_TABLE[a])
            print(f"Оскільки ціла частина дорівнює {whole}, ми заміняємо її на літеру {CONVERSION_TABLE[a]}")
        else :
            c += str(int(a))
        dec = frac
    return c


def hexadecimal_to_binary(bd, ad):
    a = [x for x in bd]
    b = [x for x in ad]
    print("Переведемо букви в обох частинах числа в цифри.")
    print("Перед комою: ")
    a = letters_to_numbers(a)
    print(f"Тобто, переведене число перед комою складається з цифр\n{a}")
    print("Після коми: ")
    b = letters_to_numbers(b)
    print(f"Тобто, переведене число після коми складається з цифр\n{b}")
    
    c = ""
    cbd = ""
    print("Переведемо кожну цифру шістнадцяткового числа у чотирьохзначне двійкове, та з'єднаємо їх.")
    print("***")
    for number in a:
        cbd += decimal_to_binary(int(number)).zfill(4)
        print("---")
    print(f"Тобто, з'єднане та трансформоване число перед комою дорівнює {cbd}")
    print("***")
    cad = ""
    for number in b:
        cad += decimal_to_binary(int(number)).zfill(4)
        print("---")
    print(f"Тобто, з'єднане та трансформоване число після коми дорівнює {cad}")

    cbd = cbd.lstrip(str(0))
    while len(cad) > 5:
        cad = cad[:-1]
    c = cbd + "." + cad
    return(cbd, cad, c)


def binary_to_octo(bd, ad):
    a = bd
    b = ad
    cbd = ""
    cad = ""
    print("Задля можливості використовувати метод трійок, додамо (при потребі) деяку кількість нулів на початку числа перед комою, і в кінці числа після коми.")
    while len(a) % 3 != 0:
        a = "0" + a
    print(f"Тепер число перед комою дорівнює {a};")
    while len(b) % 3 != 0:
        b = b + "0"
    print(f"а число після коми - {b}.")
    
    print("Переведемо кожну трійку двійкових чисел в одне вісімкове, та з'єднаємо їх.")
    print("***")
    index = 0
    for i in range(int(len(a) / 3)):
        cbd = cbd + str(CONVERSION_TABLE[a[index] + a[index + 1] + a[index + 2]])
        print(f"{a[index] + a[index + 1] + a[index + 2]} = {CONVERSION_TABLE[a[index] + a[index + 1] + a[index + 2]]}")
        index = index + 3
    print(f"Тобто, з'єднане число перед комою дорівнює {cbd}")
    print("***")
    index = 0
    for i in range(int(len(b) / 3)):
        cad = cad + str(CONVERSION_TABLE[b[index] + b[index + 1] + b[index + 2]])
        print(f"{b[index] + b[index + 1] + b[index + 2]} = {CONVERSION_TABLE[b[index] + b[index + 1] + b[index + 2]]}")
        index = index + 3
    print(f"Тобто, з'єднане число після коми дорівнює {cad}")

    cbd = cbd.lstrip("0")
    while len(cad) != 3:
        if len(cad) > 3:
            cad = cad[:-1]
        elif len(cad) < 3:
            cad = cad + "0"
    c = cbd + "." + cad
    return c, cbd, cad


def hexadecimal_to_decimal(bd, ad):
    a = [x for x in bd]
    b = [x for x in ad]

    print("Переведемо букви в обох частинах числа в цифри.")
    print("Перед комою: ")
    a = letters_to_numbers(a)
    print(f"Тобто, переведене число перед комою складається з цифр\n{a}")
    print("Після коми: ")
    b = letters_to_numbers(b)
    print(f"Тобто, переведене число після коми складається з цифр\n{b}")
    print("(Цей крок теоретично є важливим в переведенні, але через дану нам умову задачі є повністю нормальною ситуація, при якій число не зміниться.)")

    print("***")
    print("Для зручності виконання програми, реверсуємо число перед комою.")
    print("(На папері цей крок виконувати не обов'язково, відповідь не зміниться.)")
    a.reverse()
    print(f"Тепер реверсоване число перед комою виглядає як\n{a}")

    print("***")
    cbd, cad = 0, 0
    output1BD, output1AD = "A = ", "B = "
    output2BD, output2AD = "", ""
    for i in range(len(a)):
        output1BD = output1BD + f"{int(a[i])} * 16^{i} + "
        output2BD = output2BD + f"{int(a[i]) * (16 ** i)} + "
        cbd = cbd + int(a[i]) * (16 ** i)
    output1 = output1BD.rstrip("+ ") + " = " + output2BD.rstrip("+ ") + f" = {cbd}"
    print(output1)
    print("---")
    for i in range(len(b)):
            output1AD = output1AD + f"{int(b[i])} * 16^(-{i + 1}) + "
            output2AD = output2AD + f"{int(b[i]) * (16 ** -(i + 1))} + "
            cad = cad + int(b[i]) * (16 ** -(i + 1))
    output2 = output1AD.rstrip("+ ") + " = " + output2AD.rstrip("+ ") + f" = {cad}"
    print(output2)
    cbd = str(cbd)
    cad = str(cad)[2:]
    cbd = cbd.lstrip("0")
    while len(cad) != 3:
        if len(cad) > 3:
            cad = cad[:-1]
        elif len(cad) < 3:
            cad = cad + "0"
    c = cbd + "." + cad
    return c, cbd, cad


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


class  node :
    def __init__(self) -> None:
        # for storing symbol
        self.sym=''
        # for storing probability or frequency
        self.pro=0.0
        self.arr=[0]*20
        self.notEffectiveCode = 0
        self.top=0
        self.k = 0
p=[node() for _ in range(20)]


def shannon(l, h, p):
    pack1 = 0; pack2 = 0; diff1 = 0; diff2 = 0
    if ((l + 1) == h or l == h or l > h) :
        if (l == h or l > h):
            return
        p[h].top+=1
        p[h].arr[(p[h].top)] = 1
        p[l].top+=1
        p[l].arr[(p[l].top)] = 0
         
        return
     
    else :
        for i in range(l,h):
            pack1 = pack1 + p[i].pro
        pack2 = pack2 + p[h].pro
        diff1 = pack1 - pack2
        if (diff1 < 0):
            diff1 = diff1 * -1
        j = 2
        while (j != h - l + 1) :
            k = h - j
            pack1 = pack2 = 0
            for i in range(l, k+1):
                pack1 = pack1 + p[i].pro
            for i in range(h,k,-1):
                pack2 = pack2 + p[i].pro
            diff2 = pack1 - pack2
            if (diff2 < 0):
                diff2 = diff2 * -1
            if (diff2 >= diff1):
                break
            diff1 = diff2
            j+=1
         
        k+=1
        for i in range(l,k+1):
            p[i].top+=1
            p[i].arr[(p[i].top)] = 0
             
        for i in range(k + 1,h+1):
            p[i].top+=1
            p[i].arr[(p[i].top)] = 1
             
 
        # Invoke shannon function
        shannon(l, k, p)
        shannon(k + 1, h, p)


def sortByProbability(n, p, notEffective):
    temp=node()
    for j in range(1,n) :
        for i in range(n - 1) :
            if ((p[i].pro) > (p[i + 1].pro)) :
                temp.pro = p[i].pro
                temp.sym = p[i].sym
 
                p[i].pro = p[i + 1].pro
                p[i].sym = p[i + 1].sym
 
                p[i + 1].pro = temp.pro
                p[i + 1].sym = temp.sym
    for i in range(8):
        p[i].notEffectiveCode = notEffective[n-1-i]
 
  
def displayCalculated(n, p):
    print("\n\n\n\tСимвол\tІмовірність\tЕфективний код\tДовжина\tНе ефективний код\tДовжина",end='')
    for i in range(n - 1,-1,-1):
        k = 0
        print("\n\t", p[i].sym, "\t", p[i].pro,"\t\t",end='')
        for j in range(p[i].top+1):
            print(p[i].arr[j],end='')
            if(p[i].arr[j] == 1 or p[i].arr[j] == 0):
                k += 1
        print("\t\t", k, "\t\t",end='')
        print(p[i].notEffectiveCode,end='')
        print("\t\t", 3,end='')


def displayRaw(n, p):
    print("\n\n\n\tСимвол\tКількість\tІмовірність",end='')
    for i in range(n - 1,-1,-1):
        k = 0
        print("\n\t", p[n-1-i].sym, "\t", p[n-1-i].k, "\t\t", p[n-1-i].pro,"\t",end='')


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