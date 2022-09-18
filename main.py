from collections import OrderedDict

from task1 import task1
from task2 import task2


CODES = {
    'АПерша': 4,
    'БПерша': 2,
    'ВПерша': 1,
    'ГПерша': 3,
    'ДПерша': 5,
    'ЕПерша': 7,

    'ЄПерша': 4,
    'ЖПерша': 2,
    'ЗПерша': 1,
    'ИПерша': 3,
    'ІПерша': 5,
    'ЇПерша': 7,

    'ЙПерша': 4,
    'КПерша': 2,
    'ЛПерша': 1,
    'МПерша': 3,
    'НПерша': 5,
    'ОПерша': 7,

    'ППерша': 4,
    'РПерша': 2,
    'СПерша': 1,
    'ТПерша': 3,
    'УПерша': 5,
    'ФПерша': 7,

    'ХПерша': 4,
    'ЦПерша': 2,
    'ЧПерша': 1,
    'ШПерша': 3,
    'ЩПерша': 5,
    'ЮПерша': 7,

    'ЯПерша': 4,
    'ЬПерша': 2,

    #<-------------------------------->

    'АДруга': 6,
    'ЄДруга': 8,
    'ЙДруга': 1,
    'ПДруга': 3,
    'ХДруга': 5,
    'ЯДруга': 7,

    'БДруга': 6,
    'ЖДруга': 8,
    'КДруга': 1,
    'РДруга': 3,
    'ЦДруга': 5,
    'ЬДруга': 7,

    'ВДруга': 6,
    'ЗДруга': 8,
    'ЛДруга': 1,
    'СДруга': 3,
    'ЧДруга': 5,

    'ГДруга': 6,
    'ИДруга': 8,
    'МДруга': 1,
    'ТДруга': 3,
    'ШДруга': 5,

    'ДДруга': 6,
    'ІДруга': 8,
    'НДруга': 1,
    'УДруга': 3,
    'ЩДруга': 5,

    'ЕДруга': 6,
    'ЇДруга': 8,
    'ОДруга': 1,
    'ФДруга': 3,
    'ЮДруга': 5,
}


def pause():
    programPause = input("Натисніть <ENTER> для виходу з програми...")


def remove_duplicated_letters(str):
    return "".join(OrderedDict.fromkeys(str))


def create_personal_numbers():
    joinedLetters = remove_duplicated_letters(input("Введіть ваше прізвище, ім'я та побатькові: ").upper().replace(" ", ""))
    listedLetters = [x for x in joinedLetters]
    while len(listedLetters) != 8:
        del listedLetters[-1]
    numbers = []
    for letter in listedLetters:
        try:
            numbers.append([CODES[letter + 'Перша'],CODES[letter + 'Друга']])
        except:
            print(f"Літери {letter} немає у виданому коді.")
            pause()
            exit()

    return numbers, listedLetters


if __name__ == '__main__':              #ver 0.1.3
    personalNumbers, listedLetters = create_personal_numbers()
    print(f"Букви, отримані з вашого імені:\n{listedLetters}")
    print(f"Цифри, перетворені через конвертаційну таблицю з вибраних букв:\n{personalNumbers}")
    task1(personalNumbers, listedLetters)
    task2(personalNumbers, listedLetters)
    pause()
    