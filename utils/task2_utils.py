def CreateTableOfBinNum(LstOfBinNum, pn):       #ver 0.1.3
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

    for item1 in Result:
        for item2 in Result:
            if item1.issubset(item2) and item1!=item2:
                del Result[Result.index(item2)]

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
    if len(CopyList) > 1:
        ListResult = MultiplyAmplicants(CopyList, DictLetters)
    else:
        ListResult = [set([i]) for i in CopyList[0]]
    return ListOneAplicant, ListAmlicants, ListResult