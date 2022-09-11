def check_and_exit(i):
    if i == '':
        input("Роботу програми завершено.\nДля виходу натисніть <ENTER> ще раз..")
        exit()

if __name__ == '__main__':
    while True:
        numbers = input("Введіть число: ")
        check_and_exit(numbers)
        firstNumber = bin(int(numbers[0], 16))[2:]
        secondNumber = bin(int(numbers[1], 16))[2:]
        for i in range(4):
            if len(str(firstNumber)) < 4:
                firstNumber = "0" + str(firstNumber)
            if len(str(secondNumber)) < 4:
                secondNumber = "0" + str(secondNumber)

        bothNumbers = str(firstNumber) + str(secondNumber)
        TZ2 = [[0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 1, 1, 0], [1, 0, 0, 0], [1, 0, 1, 0], [1, 1, 0, 0], [1, 1, 1, 0]]

        for i in range(8):
            TZ2[i][3] = int(str(bothNumbers)[7-i])

        monoTableArray = [[[0 for x in range(4)] for y in range(4)] for z in range(6)]


        for i in range(6):
            monoTableArray[i][0] = [TZ2[0][0], TZ2[0][1], TZ2[0][2], TZ2[0][3]]
        for i in range(2):
            monoTableArray[i][1] = [TZ2[1][0], TZ2[1][1], TZ2[1][2], TZ2[1][3]]
        for i in range(2):
            monoTableArray[i+2][1] = [TZ2[2][0], TZ2[2][1], TZ2[2][2], TZ2[2][3]]
        for i in range(2):
            monoTableArray[i+4][1] = [TZ2[4][0], TZ2[4][1], TZ2[4][2], TZ2[4][3]]
        monoTableArray[0][2] = [TZ2[3][0], TZ2[3][1], TZ2[3][2], TZ2[3][3]]
        monoTableArray[1][2] = [TZ2[5][0], TZ2[5][1], TZ2[5][2], TZ2[5][3]]
        monoTableArray[2][2] = [TZ2[3][0], TZ2[3][1], TZ2[3][2], TZ2[3][3]]
        monoTableArray[3][2] = [TZ2[6][0], TZ2[6][1], TZ2[6][2], TZ2[6][3]]
        monoTableArray[4][2] = [TZ2[5][0], TZ2[5][1], TZ2[5][2], TZ2[5][3]]
        monoTableArray[5][2] = [TZ2[6][0], TZ2[6][1], TZ2[6][2], TZ2[6][3]]
        for i in range(6):
            monoTableArray[i][3] = [TZ2[7][0], TZ2[7][1], TZ2[7][2], TZ2[7][3]]

        Monotonic = 0

        for i in range(6):
            tempValue = -1
            for j in range(4):
                if monoTableArray[i][j][3] == 0 and tempValue == 1:
                    internalTempValue = 0
                    tempValue = monoTableArray[i][j][3]
                    monoTableArray[i][j][3] = 9 #Код нуля для правильного формування таблиці при її виводі
                    monoTableArray[i][j-1][3] = 10 #Код одиниці для правильного формування таблиці при її виводі
                    for x in range(i):
                        internalTempValue = 0
                        for y in range(4):
                            for z in range(2):
                                if monoTableArray[x][y][0] == monoTableArray[i][j-z][0] and monoTableArray[x][y][1] == monoTableArray[i][j-z][1] and monoTableArray[x][y][2] == monoTableArray[i][j-z][2]:
                                    internalTempValue += 1
                        if internalTempValue == 2:
                            break
                    
                    if internalTempValue != 2:
                        Monotonic += 1
                else:
                    tempValue = monoTableArray[i][j][3]

        print("a b c | f    a b c | f    a b c | f    a b c | f    a b c | f    a b c | f")

        for i in range(4):
            for j in range(6):
                for k in range(4):
                    if k != 3:
                        print(monoTableArray[j][i][k], end=" ")
                    else:
                        if monoTableArray[j][i][k] == 9:
                            print("||o̲|", end="")
                        elif monoTableArray[j][i][k] == 10:
                            print("||̅₁|", end="")
                        else:
                            print("|", monoTableArray[j][i][k], end=" ")
                print(end="   ")
            print()
        
        print("Відповідь: ", Monotonic)