from tabulate import tabulate

from main import create_personal_numbers, pause
from utils.task1_utils import *
from utils.task2_utils import *


def testPause():
    program_pause = input("Press the <ENTER> key to continue...")


KARNAUGH_MAP_2X = {
    '0': ['1', '4', '8', '2', '10'],
    '1': ['0', '3', '9', '5', '11'],
    '3': ['1', '2', '7', 'B', '13'],
    '2': ['3', '0', 'A', '6', '12'],

    '4': ['0', 'C', '5', '6', '14'],
    '5': ['1', 'D', '4', '7', '15'],
    '7': ['3', 'F', '5', '6', '17'],
    '6': ['2', 'E', '7', '4', '16'],

    'C': ['4', '8', 'E', 'D', '1C'],
    'D': ['C', 'F', '5', '9', '1D'],
    'F': ['7', 'B', 'D', 'E', '1F'],
    'E': ['C', 'F', '6', 'A', '1E'],

    '8': ['A', '9', '0', 'C', '18'],
    '9': ['8', 'B', '1', 'D', '19'],
    'B': ['9', 'A', '3', 'F', '1B'],
    'A': ['E', '2', 'B', '8', '1A'],


    '10': ['11', '14', '18', '12', '0'],
    '11': ['10', '13', '19', '15', '1'],
    '13': ['11', '12', '17', '1B', '3'],
    '12': ['13', '10', '1A', '16', '2'],

    '14': ['10', '1C', '15', '16', '4'],
    '15': ['11', '1D', '14', '17', '5'],
    '17': ['13', '1F', '15', '16', '7'],
    '16': ['12', '1E', '17', '14', '6'],

    '1C': ['14', '18', '1E', '1D', 'C'],
    '1D': ['1C', '1F', '15', '19', 'D'],
    '1F': ['17', '1B', '1D', '1E', 'F'],
    '1E': ['1C', '1F', '16', '1A', 'E'],

    '18': ['1A', '19', '10', '1C', '8'],
    '19': ['18', '1B', '11', '1D', '9'],
    '1B': ['19', '1A', '13', '1F', 'B'],
    '1A': ['1E', '12', '1B', '18', 'A']
}


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


def task2_3(pn, ll, internetMode = False):
    print('\n\n2.3')

    TRUTH_TABLE, F0 = generate_starting_tables(pn)
    tableHeaders = ['№', 'edcba', 'f']
    tabulatedTable = tabulate(TRUTH_TABLE, tablefmt="grid", headers=tableHeaders)

    print(tabulatedTable)

    if internetMode == False:
        #k = Graph(KARNAUGH_MAP_2X)
        pass
    else:
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options
        from webdriver_manager.chrome import ChromeDriverManager

        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.common.by import By


        SUBMIT = '/html/body/form/table/tbody/tr[1]/th[1]/input'


        opts = Options()
        opts.add_argument("--start-maximized")
        opts.add_experimental_option("excludeSwitches", ["enable-automation"])
        opts.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)

        driver.get('http://www.32x8.com/var5.html')

        submitButton = WebDriverWait(driver, 15).until(lambda x: x.find_element(By.XPATH, SUBMIT))

        for i in range(32):
            if F0[i] == '1':
                button = f"/html/body/form/table/tbody/tr[{i+3}]/td[8]/input"
                driver.find_element(By.XPATH, button).click()
            elif F0[i] == 'x':
                button = f"/html/body/form/table/tbody/tr[{i+3}]/td[9]/input"
                driver.find_element(By.XPATH, button).click()

        submitButton.click()
        #/html/body/div/div/div[4]/table
        #/html/body/div[2]/div/div[2]/table/tbody/tr[4]/td[4]
        #/html/body/div[2]/div/div[3]/table/tbody/tr[6]/td[3]
        #/html/body/div[2]/div/div[4]/table/tbody/tr[1]/td[1]
        l = driver.find_element(By.XPATH, '/html/body/div/div/div[4]/table/tbody/tr')
        print(l)
        for table in driver.find_element(By.XPATH, '/html/body/div/div/div[4]/table'):
            data = [item.text for item in table.find_element(By.XPATH, ".//*[self::td or self::th]")]
            print(data)
        testPause()
        driver.quit()


if __name__ == '__main__':
    #personalNumbers, listedLetters = create_personal_numbers()
    personalNumbers, listedLetters = [[4, 5], [4, 6], [1, 1], [5, 3], [1, 3], [3, 1], [2, 1], [3, 8]], ['Х', 'А', 'Л', 'У', 'С', 'М', 'К', 'И']
    print(f"Букви, отримані з вашого імені:\n{listedLetters}")
    print(f"Цифри, перетворені через конвертаційну таблицю з вибраних букв:\n{personalNumbers}")
    task2_3(personalNumbers, listedLetters, internetMode=True)
    pause()