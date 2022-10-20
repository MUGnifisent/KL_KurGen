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

def fill_f_of_x(StartPosXInF, LstOfBinNum, letter, index):
    number = ''
    if index == StartPosXInF:
        number = 'x'
        StartPosXInF += 3
        #NumF0.append('x')
        #print(f'({LstOfBinNum[letter][index%4]})x',end='\t')
    else:
        number = LstOfBinNum[letter][index%4]
        #NumF0.append(LstOfBinNum[letter][index%4])
        #print(LstOfBinNum[letter][index%4], end='\t')
    return StartPosXInF, number

def generate_f(pn):
    LstOfBinNum = []
    for i in range(8):
        Num1Bin = bin(pn[i][0])[2:]
        LstOfBinNum.append(Num1Bin.zfill(4))
        Num2Bin = bin(pn[i][1])[2:]
        LstOfBinNum.append(Num2Bin.zfill(4))

    BinNum0to31 = []
    NumF = [[],[],[],[],[]]
    letter = -1
    StartPosXInF0, StartPosXInF1, StartPosXInF2, StartPosXInF3, StartPosXInF4 = FindPosXInF(LstOfBinNum)
    for i in range(32):
        print(i,end='\t ')
        BinNum0to31.append(bin(i)[2:].zfill(5))
        for number in BinNum0to31[i]:
            print(number, end=' ')
        
        if i%4 == 0:
            letter += 1
        StartPosXInF0, temp_number = fill_f_of_x(StartPosXInF0, LstOfBinNum, letter, i)
        NumF[0].append(temp_number)
        StartPosXInF1, temp_number = fill_f_of_x(StartPosXInF1, LstOfBinNum, letter, i)
        NumF[1].append(temp_number)
        StartPosXInF2, temp_number = fill_f_of_x(StartPosXInF2, LstOfBinNum, letter, i)
        NumF[2].append(temp_number)
        d = letter + 8
        StartPosXInF3, temp_number = fill_f_of_x(StartPosXInF3, LstOfBinNum, d, i)
        NumF[3].append(temp_number)
        StartPosXInF4, temp_number = fill_f_of_x(StartPosXInF4, LstOfBinNum, d, i)
        NumF[4].append(temp_number)
    return NumF