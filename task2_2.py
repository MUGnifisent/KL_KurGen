from utils.task1_utils import *

def CreateTableOfBinNum(LstOfBinNum, pn):
    for i in range(8):
        for j in range(2):
            print(pn[i][j], end='   ')
    print()
    for i in range(4):
        for j in range(16):
            print(LstOfBinNum[j][i], end='   ')
        print()

def FindPosXInF(LstOfBinNum):
    if LstOfBinNum[0][0] == '1':
            StartPosXInF0 = 2
            StartPosXInF1 = 0
            StartPosXInF2 = 1
    else:
            for i in range(1, 4):
                if LstOfBinNum[0][i] == '1':
                    StartPosXInF0 = i-1
                    StartPosXInF1 = i
                    StartPosXInF2 = i+1
                    break
    if LstOfBinNum[8][0] == '1':
        StartPosXInF3 = 2
        StartPosXInF4 = 1
    else:
        for i in range(1, 4):
            if LstOfBinNum[8][i] == '1':
                StartPosXInF3 = i-1
                StartPosXInF4 = i
                break
    return StartPosXInF0, StartPosXInF1, StartPosXInF2, StartPosXInF3, StartPosXInF4

def FillFOfX(StartPosXInF, LstOfBinNum, letter, index):
    if index == StartPosXInF:
             print(f'({LstOfBinNum[letter][index%4]})x',end='\t')
             StartPosXInF += 3
    else:
        print(LstOfBinNum[letter][index%4], end='\t')
    return StartPosXInF

def MergerBinNum(bin1, bin2):
    count = 0
    index = 0
    for i in range(5):
        if bin1[i] != bin2[i]:
            count += 1
            index = i 
        if count == 2:
            return -1
    return bin1[:index] + '_' + bin1[index + 1:]
    
def SortInDictBy1(ListOfNum, abc):
    SortDict = {}
    for index in range(ListOfNum[-1].count('1')+1):
        if list(filter(lambda x: x.count('1') == index, ListOfNum)) != []:
            SortDict.update({chr(abc + index):list(filter(lambda x: x.count('1') == index, ListOfNum))})
        else:
            abc -= 1
    return SortDict

def ConvertDictToList(SortDict):
    List = []
    for key in SortDict.keys():
        for index in range(len(SortDict[key])):
            List.append([SortDict[key][index], f'{key}{index}', '-'])
    return List

def CreateListOfMerges(SortDictF0):
    LstMerges = []
    LstNameMerges = []
    List1 = ConvertDictToList(SortDictF0)
    for key in SortDictF0.keys():
        scndkey = chr(ord(key) + 1)
        if scndkey in SortDictF0.keys():
            for item1 in range(len(SortDictF0[key])):
                for item2 in range(len(SortDictF0[scndkey])):
                    tempMerge = MergerBinNum(SortDictF0[key][item1], SortDictF0[scndkey][item2])
                    if tempMerge != -1:
                        if [SortDictF0[key][item1], f'{key}{item1}','-'] in List1:
                            List1[List1.index([SortDictF0[key][item1], f'{key}{item1}', '-'])][2] = '+'
                        if [SortDictF0[scndkey][item2], f'{scndkey}{item2}','-'] in List1:
                            List1[List1.index([SortDictF0[scndkey][item2], f'{scndkey}{item2}','-'])][2] = '+'
                        LstMerges.append(tempMerge)
                        LstNameMerges.append([f'{key}{item1}{scndkey}{item2}'])
    return LstMerges, List1, LstNameMerges

def CheckEqualityNums(num1, num2):
    for i in range(len(num2)):
        if num2[i] =='_':
            num1 = num1[:i] + '_' + num1[i + 1:]
    if num1 == num2:
        return True
    else:
        return False
    
def BinaryToLetters(Bin):
    #List0 = ['ā','b̅','c̄','đ','ē']
    #List0 = ['ā','b̅', 'c̄','d̅','ē']
    letters = '' 
    #List0 = ['ā','ᵬ','c̄','đ','ē']
    #List0 = ['ā','ᵬ','ꞇ','đ','ē']
    List0 = ['ē', 'đ', 'č', 'ƀ', 'ā']
    List1 = ['e', 'd', 'c', 'b', 'a']
    for i in range(len(Bin)):
        if Bin[i] != '_':
            if Bin[i] == '1':
                letters += List1[i]
            else:
                letters += List0[i]
    return letters

def PrintFunctionAmplicants(ListsWithAplicant, v, x):
    for item in ListsWithAplicant:
        if len(item) > 1:
            print(f'({v.join([i for i in item])})', end='')
        else:
            print(item[0], end=' ')
        if ListsWithAplicant.index(item) != len(ListsWithAplicant) - 1:
            print(x,end='')

def DelIdenticalInList(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n

def MultiplyAmplicants(ListAmplicants, DictLetters):
    while len(ListAmplicants) != 1:
        TempList = []
        for multpy1 in ListAmplicants[0]:
            for multpy2 in ListAmplicants[1]:  
                tempSet0 = set()
                if not isinstance(multpy1, set):
                    tempSet0 = set([multpy1])
                else:      
                    tempSet0 = set(multpy1)
                tempSet = tempSet0
                tempSet.add(multpy2)
                TempList.append(tempSet)
        '''
        ListOfSize = []
        for item in TempList:
            Size = 0
            for mult in item:
                Size += DictLetters[mult]
            ListOfSize.append(Size)
        print(TempList, end = ' = ')
        MinSize = min(ListOfSize)
        n = 0
        for apSize in range(len(ListOfSize)):
            if ListOfSize[apSize - n] > MinSize:
                del TempList[apSize - n]
                del ListOfSize[apSize - n]
                n += 1
        print(TempList)
        '''
        del ListAmplicants[0]
        del ListAmplicants[0]
        ListAmplicants.insert(0,TempList)
    #print(f'\n{len(*ListAmplicants)}')
    ListOfSize = []
    for item in ListAmplicants[0]:
        Size = 0
        for mult in item:
            Size += DictLetters[mult]
        ListOfSize.append(Size)
    MinSize = min(ListOfSize)

    n = 0
    for apSize in range(len(ListOfSize)):
        if ListOfSize[apSize - n] > MinSize:
            del ListAmplicants[0][apSize - n]
            del ListOfSize[apSize - n]
            n += 1
    return DelIdenticalInList(ListAmplicants[0])

def SimplifyingExpression(DictLetters, ListAplicants):
    Result = [set(item) for item in ListAplicants]

    for List in Result:
        TempList = set()
        MinLen = min([DictLetters[i] for i in List])
        for index in List:
            if DictLetters[index] == MinLen:
                TempList.add(index)
        Result[Result.index(List)] = TempList
    
    for item1 in Result:
        for item2 in Result:
            if item1.issubset(item2) and item1!=item2:
                del Result[Result.index(item2)]

    ListOneAplicant = set()
    ListAmlicants = []
    for i in Result:
        if len(i) == 1:
            ListOneAplicant.update(i)
        else:
            ListAmlicants.append(i)
    CopyList = list(ListAmlicants)
    ListResult = MultiplyAmplicants(CopyList, DictLetters)
    return ListOneAplicant, ListAmlicants, ListResult
    

if __name__ == '__main__':
    listedLetters = ['Х', 'А', 'Л', 'У', 'С', 'М', 'К', 'И']
    pn = [[4, 7], [5, 3], [2, 7], [6, 4], [1, 8], [5, 5], [3, 8], [4, 6]]

    print('2.2')

    LstOfBinNum = []
    for i in range(8):
        Num1Bin = bin(pn[i][0])[2:]
        LstOfBinNum.append(Num1Bin.zfill(4))
        Num2Bin = bin(pn[i][1])[2:]
        LstOfBinNum.append(Num2Bin.zfill(4))

    print(' ', end=' ')
    print(*listedLetters, sep=' '*7)
    CreateTableOfBinNum(LstOfBinNum, pn)

    print('\n\n')
    print('Зміщення першого\nневизначеного\t   \t-S\tS\t+S\t-S\tS\nзначення')
    print('№ набору e d c b a\tf0\tf1\tf2\tf3\tf4')
    BinNum0to31 = []
    NumF0 = []
    letter = -1
    SetsForF0 = []
    StartPosXInF0, StartPosXInF1, StartPosXInF2, StartPosXInF3, StartPosXInF4 = FindPosXInF(LstOfBinNum)
    for i in range(32):
        print(i,end='\t ')
        BinNum0to31.append(bin(i)[2:].zfill(5))
        for number in BinNum0to31[i]:
            print(number, end=' ')
        
        if i%4 == 0:
            letter += 1
        print(end='\t')
        if i == StartPosXInF0:
             NumF0.append('x')
             print(f'({LstOfBinNum[letter][i%4]})x',end='\t')
             StartPosXInF0 += 3
        else:
            NumF0.append(LstOfBinNum[letter][i%4])
            print(LstOfBinNum[letter][i%4], end='\t')
        d = letter + 8
        StartPosXInF1 = FillFOfX(StartPosXInF1, LstOfBinNum, letter, i)
        StartPosXInF2 = FillFOfX(StartPosXInF2, LstOfBinNum, letter, i)
        StartPosXInF3 = FillFOfX(StartPosXInF3, LstOfBinNum, d, i)
        StartPosXInF4 = FillFOfX(StartPosXInF4, LstOfBinNum, d, i)
         
        if NumF0[i] == '1' or NumF0[i] == 'x':
            SetsForF0.append(BinNum0to31[i])
        print()

    print('\n\n')
    abc = 97
    SortDict = SortInDictBy1(SetsForF0, abc)
    ListMerge, list1, listname = CreateListOfMerges(SortDict)
    AllDataForTable = []
    AllDataForTable.append(list1)
    AllDataForTable.append(listname)
    print('К\tП\tУ', end='\t')
    while True:
        if list(filter(lambda x: x[2] == '+', list1)) == []:
            break
        print('С\tК\tП\tУ', end='\t')
        abc += len(SortDict)
        SortDict = SortInDictBy1(ListMerge, abc)
        ListMerge, list1, listname = CreateListOfMerges(SortDict)
        AllDataForTable.append(list1)
        AllDataForTable.append(listname)
    print()
    MaxLen = len(max(AllDataForTable, key = lambda x: len(x)))
    for index in range(MaxLen):
        for table in AllDataForTable:
            if index < len(table):
                print(*table[index], sep='\t', end='\t')
            else:
                print('\t\t', end='\t')
        print()
    
    print('\n\n')
    AllNegative = []
    for i in range(0,len(AllDataForTable), 2):
        TempNegative = list(filter(lambda x: x[2] == '-', AllDataForTable[i]))
        for item in TempNegative:
            if item[0] not in AllNegative:
                AllNegative.append(item[0])
    
    print('Прості імпліканти:')
    print(*AllNegative, sep = ', ', end='.\n\n')
    ListCountLetter = [len(x.replace('_','')) for x in AllNegative]
    LstF0Only1 = [BinNum0to31[i] for i in range(32) if NumF0[i] == '1']
    ListsWithAplicant = []
    ListOfLetters = {f'I{i+1}':BinaryToLetters(AllNegative[i]) for i in range(len(AllNegative))}
    print('Одиничні', end='\t')
    print(*[item.ljust(5) for item in ListOfLetters.keys()], sep='\t')
    print('набори', end='\t\t')
    print(*[item.ljust(5) for item in ListOfLetters.values()], sep='\t')
    print('edcba', end='\t\t')
    print(*AllNegative, sep='\t')
    for Set in LstF0Only1:
        print(Set, end='\t\t')
        TempList = []
        for merge in range(len(AllNegative)):
            if CheckEqualityNums(Set,AllNegative[merge]):
                print('V', end = '\t')
                TempList.append(f'I{merge + 1}')
            else:
                print('-', end = '\t')
        ListsWithAplicant.append(TempList)
        print('\n')
    print('Літер в\nімплакації', end='\t')
    print(*ListCountLetter, sep='\t')

    print('\n\n')
    DictOfCountLetters = {f'I{index + 1}':ListCountLetter[index] for index in range(len(ListCountLetter))}
    print('Отримаємо функцію F:\nF =',end=' ')
    PrintFunctionAmplicants(ListsWithAplicant, ' v ', ' ')
    print('\nСпрощення:\nF =', end = ' ')

    ListOneAmplicant, ListAmplicants, ListResults = SimplifyingExpression(DictOfCountLetters, ListsWithAplicant)
    ListOneAmplicant = [''.join(i)  for i in ListOneAmplicant]
    for i in ListResults:
        i.update(ListOneAmplicant)
    ListOneAmplicant = sorted(ListOneAmplicant, key = lambda x: int(x[1:]))
    ListAmplicants = [sorted(list(i), key = lambda x: int(x[1:])) for i in ListAmplicants]
    ListResults = [sorted(list(i), key = lambda x: int(x[1:])) for i in ListResults]
    print(*ListOneAmplicant, sep=' ', end='')
    PrintFunctionAmplicants(ListAmplicants, ' v ', ' ')
    print(' = ', end='')
    PrintFunctionAmplicants(ListResults, ' ', ' v ')
    print(f'\n\nОтже, дана функція F має {len(ListResults)} мінімальні ДНФ:')
    for i, dnf in enumerate(ListResults, 1):
        print(f'{i}) F = ', end ='')
        print(*[item.ljust(3) for item in dnf], sep=' v ', end =' = ')
        print(*[ListOfLetters[item] for item in dnf], sep=' v ', end =';\n')






