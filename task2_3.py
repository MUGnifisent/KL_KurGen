from tabulate import tabulate

from main import create_personal_numbers, pause
from utils.task1_utils import *
from utils.task2_utils import *
from utils.task2_image_utils import gen_karnaugh_map_image


def testPause():
    program_pause = input("Press the <ENTER> key to continue...")


IMP_CHECKER = {
    '-0': '0',
    '0-': '0',
    '1-': '1',
    '-1': '1',
    '10': 'x',
    '01': 'x',
    '00': '0',
    '11': '1',
    '--': '-'
}


LETTERS = ['e', 'd', 'c', 'b', 'a'] #going into main.py


LETTER_VARIANT = {
    'A': LETTERS[0],
    'B': LETTERS[1],
    'C': LETTERS[2],
    'D': LETTERS[3],
    'E': LETTERS[4]
}


#KARNAUGH_MAP_2X = {
#    '0': ['1', '4', '8', '2', '10'],
#    '1': ['0', '3', '9', '5', '11'],
#    '3': ['1', '2', '7', 'B', '13'],
#    '2': ['3', '0', 'A', '6', '12'],
#
#    '4': ['0', 'C', '5', '6', '14'],
#    '5': ['1', 'D', '4', '7', '15'],
#    '7': ['3', 'F', '5', '6', '17'],
#    '6': ['2', 'E', '7', '4', '16'],
#
#    'C': ['4', '8', 'E', 'D', '1C'],
#    'D': ['C', 'F', '5', '9', '1D'],
#    'F': ['7', 'B', 'D', 'E', '1F'],
#    'E': ['C', 'F', '6', 'A', '1E'],
#
#    '8': ['A', '9', '0', 'C', '18'],
#    '9': ['8', 'B', '1', 'D', '19'],
#    'B': ['9', 'A', '3', 'F', '1B'],
#    'A': ['E', '2', 'B', '8', '1A'],
#
#
#    '10': ['11', '14', '18', '12', '0'],
#    '11': ['10', '13', '19', '15', '1'],
#    '13': ['11', '12', '17', '1B', '3'],
#    '12': ['13', '10', '1A', '16', '2'],
#
#    '14': ['10', '1C', '15', '16', '4'],
#    '15': ['11', '1D', '14', '17', '5'],
#    '17': ['13', '1F', '15', '16', '7'],
#    '16': ['12', '1E', '17', '14', '6'],
#
#    '1C': ['14', '18', '1E', '1D', 'C'],
#    '1D': ['1C', '1F', '15', '19', 'D'],
#    '1F': ['17', '1B', '1D', '1E', 'F'],
#    '1E': ['1C', '1F', '16', '1A', 'E'],
#
#    '18': ['1A', '19', '10', '1C', '8'],
#    '19': ['18', '1B', '11', '1D', '9'],
#    '1B': ['19', '1A', '13', '1F', 'B'],
#    '1A': ['1E', '12', '1B', '18', 'A']
#}


def table_implicants(implicants):
    prep = []
    for i in range(len(implicants)):
            prep.append([f'i{i}' ,implicants[i]])
    tabeledImplicants = tabulate(prep, tablefmt="grid", headers=['Номер\nімпліканти',''.join(LETTERS)], stralign='center')
    return tabeledImplicants


#def table_compared_implicants(implicants, res, resT, term):
#    prep = []
#    for i in range(len(implicants)):
#            prep.append([f"i{i}", implicants[i]])
#    prep.append(['Результат', res])
#    prep.append(['Результат', resT])
#    prep.append(['Терм', term])
#    tabeledImplicants = tabulate(prep, tablefmt="grid", headers=['Порівнюються',''], stralign='center', numalign='center')
#    return tabeledImplicants


def table_results(res):
    prep, lct = [], []
    for i in range(len(res)):
        if res[i][2].count('x') == 1:
            prep.append([f"i{res[i][0]} i{res[i][1]}", f"{res[i][2]}({res[i][3]})", f"{res[i][4]}(+)"])
            lct.append(res[i][4])
        else:
            prep.append([f"i{res[i][0]} i{res[i][1]}", f"{res[i][2]}({res[i][3]})", "-"])
    table = tabulate(prep, tablefmt="grid", headers=['Порівнюються', 'Результат', 'Терм'], stralign='center', numalign='center')
    return table, lct

def generate_starting_tables(pn):
    tt, f = [], []
    for letter in range(4):
        for num in pn[letter]:
            f.extend(bin(num)[2:].zfill(4))
    
    if f[0] == '1':
        StartPosXInF0 = 2
    else:
        for i in range(1, 4):
            if f[i] == '1':
                StartPosXInF0 = i-1
                break

    for i in range(32):
        if StartPosXInF0 == i:
            StartPosXInF0+= 3
            f[i] = 'x'
        
        temp = bin(i).lstrip("0b").zfill(5)
        tt.append([hex(i)[2:].upper(),temp, f[i]])

    return tt, f

def create_implicant(letters):
    result = '-----'
    for i in range(len(letters)):
        l = letters[i].lstrip('/')
        if letters[i] != l:
            result = result[:LETTERS.index(l)] + '0' + result[LETTERS.index(l)+1:]
        else:
            result = result[:LETTERS.index(l)] + '1' + result[LETTERS.index(l)+1:]
    return result

def task2_3(pn, ll, internetMode = False):
    print('\n\n2.3')

    TRUTH_TABLE, F0 = generate_starting_tables(pn)
    F0Only1 = set([hex(i)[2:].upper() for i in range(len(F0)) if F0[i] == '1'])
    F0OnlyX = set([hex(i)[2:].upper() for i in range(len(F0)) if F0[i] == 'x'])
    tableHeaders = ['№', 'edcba', 'f']
    tabulatedTable = tabulate(TRUTH_TABLE, tablefmt="grid", headers=tableHeaders, numalign='center', stralign='center')

    print(tabulatedTable)

    if internetMode == False:
        print('UNDER DEVELOPMENT...')
        return NotImplemented

    else:
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.common.by import By

        from webdriver_manager.chrome import ChromeDriverManager

        #import pandas as pd

        from bs4 import BeautifulSoup

        import animation


        SUBMIT = '/html/body/form/table/tbody/tr[1]/th[1]/input'
        ASCII_opt = '/html/body/form/table/tbody/tr[7]/td[11]/input'
        TBODY = '/html/body/div/div/div[4]/table/tbody'

        anim = ('   ', '.  ', '.. ', '...', '.. ', '.  ')
        wait = animation.Wait(anim, text='Calculating')

        opts = Options()
        #opts.add_argument("--start-maximized")
        opts.add_argument('headless')
        opts.add_experimental_option("excludeSwitches", ["enable-automation"])
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        opts.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)

        wait.start()

        driver.get('http://www.32x8.com/var5.html')

        submitButton = WebDriverWait(driver, 15).until(lambda x: x.find_element(By.XPATH, SUBMIT))
        driver.find_element(By.XPATH, ASCII_opt).click()

        for i in range(32):
            if F0[i] == '1':
                button = f"/html/body/form/table/tbody/tr[{i+3}]/td[8]/input"
                driver.find_element(By.XPATH, button).click()
            elif F0[i] == 'x':
                button = f"/html/body/form/table/tbody/tr[{i+3}]/td[9]/input"
                driver.find_element(By.XPATH, button).click()
        submitButton.click()

        table = driver.find_element(By.XPATH, TBODY).get_attribute("outerHTML")
        #bodyHtml = driver.execute_script("return document.body.innerHTML;")
        #testPause()
        driver.quit()
        
        #tables = pd.read_html(bodyHtml)
        #print(tables[5])
        ##div[2]/div/div[4]

        soup = BeautifulSoup(table, 'lxml')
        #print(soup.prettify())
        res = []
        #table0 = soup.find("table", {'class': 'wikitable sortable'})
        for row in soup.find_all("tr"):
            #col = row.find_all("td")
            temp = []
            for col in row.find_all("td"):
                if len(col) > 0:
                    spans = col.find_all("span")
                    if len(spans) > 0:
                        listSpan = []
                        for span in spans:
                            listSpan.append(span)
                        temp.append(listSpan)
                    else:
                        d = col.contents[0]
                        try:
                            to_append=d.contents[0]
                        except:
                            to_append=d
                        temp.append(to_append)
            res.append(temp)
        #print(*res, sep='\n')
        for i in range(len(res)):
            res[i][0] = list(map(lambda x: hex(int(x))[2:].upper(), res[i][0].strip('()').split(',')))
            
            temp = []
            for element in res[i][1]:
                checkval = str(element)
                if 'text-decoration: overline;' in checkval:
                    temp.append(f"/{LETTER_VARIANT[element.contents[0]]}")
                else:
                    temp.append(f"{LETTER_VARIANT[element.contents[0]]}")
            res[i][1] = temp

        wait.stop()

        listTermXIn = set()
        listTermXOut = set(F0OnlyX)
        repeationDict = {}
        ResLetter = []
        for i, NumAndLet in enumerate(res):
            number, letter = NumAndLet
            ResLetter.append(letter)
            for num in number:
                repeationDict[num] = repeationDict.get(num, 0)  + 1
            SetNumber = set(number)
            print(f'{i+1}) Склеювання клітинок: {", ".join(number)}; результат: {"".join(letter)};')
            MinTerms = sorted(F0Only1.intersection(SetNumber), key= lambda x: int(x, 16))
            print(f'Мінімізуються набори: {", ".join(MinTerms)}')
            listTermXIn.update(F0OnlyX.intersection(SetNumber))
            listTermXOut.difference_update(SetNumber)
        listTermXIn = sorted(listTermXIn, key= lambda x: int(x, 16))
        listTermXOut = sorted(listTermXOut, key= lambda x: int(x, 16))
        print(f'Невизначені значення функції в клітинках {", ".join(listTermXIn)} довизначаємо як "1", оскільки вони беруть участь у склеюванні за "1".')
        print(f'Невизначені значення функції в клітинках {", ".join(listTermXOut)} довизначаємо як "0", оскільки вони не беруть участь у склеюванні за "1".')
        #print(F0Only1)
        for i in range(max(repeationDict.values())):
            TermsRepeatI = []
            for key, values in repeationDict.items():
                if values == i+1:
                    TermsRepeatI.append(key)
            if len(TermsRepeatI) != 0:
                TermsRepeatI = sorted(TermsRepeatI, key= lambda x: int(x, 16))
                if i == 0:
                    print(f'Набори {", ".join(TermsRepeatI)} беруть участь у {i+1} склеюванні.')
                else:
                    print(f'Набори {", ".join(TermsRepeatI)} беруть участь у {i+1} склеюваннях.')
        #print(*res, sep='\n')


        # Generating an image
        # Pass filename without extension
        gen_karnaugh_map_image(TRUTH_TABLE, res, "Завдання 2.3 - карта Карно")


        implicants = [create_implicant(let[1]) for let in res]
        
        #            implicants[i][ord(element) - 97] = '1'
        
        print(table_implicants(implicants))

        checker, idealChecker = [], []
        for i in range(len(implicants)):
            temp, idealTemp = '', ''
            for j in range(len(implicants)):
                idealTemp += '+'
                if i == j:
                    temp += '+'
                else:
                    temp += '-'
            checker.append(list(temp))
            idealChecker.append(list(idealTemp))

        impRes = []
        while True:
            if checker == idealChecker:
                break

            for i in range(len(implicants)):
                for j in range(len(implicants)):
                    if checker[i][j] == '+' and checker[j][i] == '+':
                        continue
                    lilImpRes = ''
                    for n in range(len(implicants[0])):
                        temp = implicants[i][n] + implicants[j][n]
                        lilImpRes += IMP_CHECKER[temp]

                    lilImpResTr = lilImpRes.replace('x', '-')

                    lilTerm = ''
                    for n in range(len(lilImpResTr)):
                        if lilImpResTr[n] == '0':
                            lilTerm += f"/{LETTERS[n]}"
                        elif lilImpResTr[n] == '1':
                            lilTerm += f"{LETTERS[n]}"

                    #print(table_compared_implicants([implicants[i], implicants[j]], lilImpRes, lilImpResTr, lilTerm))
                    
                    impRes.append([i, j, lilImpRes, lilImpResTr, lilTerm])

                    checker[i][j], checker[j][i] = '+', '+'
        tabres, LCT = table_results(impRes)
        print(tabres)
        
        print(f'Отже, сполучними термами є: {", ".join(LCT)}.')
        print('Кінцева функція:')
        print('f = ', end='')
        FullTerms = ResLetter + LCT
        for item in FullTerms:
            print(f'{"".join([i for i in item])}', end='')
            if FullTerms.index(item) != len(FullTerms) - 1:
                print(' v ',end='')


if __name__ == '__main__':
    personalNumbers, listedLetters = create_personal_numbers()
    #personalNumbers, listedLetters = [[4, 5], [4, 6], [1, 1], [5, 3], [1, 3], [3, 1], [2, 1], [3, 8]], ['Х', 'А', 'Л', 'У', 'С', 'М', 'К', 'И']
    print(f"Букви, отримані з вашого імені:\n{listedLetters}")
    print(f"Цифри, перетворені через конвертаційну таблицю з вибраних букв:\n{personalNumbers}")
    task2_3(personalNumbers, listedLetters, internetMode=True)
    #pause()