from math import modf, log10, ceil, floor          #ver 0.0.11
from random import choice


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
    return (log10(x) / log10(2))


def is_power_of_2(n):
	return (ceil(log2(n)) == floor(log2(n)))


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
    return choice(l)


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