k = 1
slovar = {
    '1': " ",
    '2': " ",
    '3': " ",
    '4': " ",
    '5': " ",
    '6': " ",
    '7': " ",
    '8': " ",
    '9': " ",
}
while True:
    try:
        hod = ""
        if k % 2 == 0:
            hod = "0"
        else:
            hod = "X"

        number = int(input("Введите номер от 1 до 9 вы " + hod))
        if slovar[str(number)] != " ":
            print("Это клеточка занята!")
        else:
            k += 1
            slovar[str(number)] = hod

        n = f''' 
         _____  _____  _____
        |  {slovar['1']}   |   {slovar['2']}  |   {slovar['3']}  |
         _____  _____  _____
        |   {slovar['4']}  |   {slovar['5']}  |   {slovar['6']}  |
         _____ _____ _____
        |   {slovar['7']}  |  {slovar['8']}   |   {slovar['9']}  |
         -----  -----  -----'''

        print(n)
        win_numbers = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (3, 5, 7), (1, 5, 9))
        if slovar['1'] == slovar['2'] == slovar['3'] != ' ':
            print('Игра закончена, победитель:', hod)
            break
        elif slovar['4'] == slovar['5'] == slovar['6'] != ' ':
            print('Игра закончена, победитель:', hod)
            break
        elif slovar['7'] == slovar['8'] == slovar['9'] != ' ':
            print('Игра закончена, победитель:', hod)
            break
        elif slovar['1'] == slovar['4'] == slovar['7'] != ' ':
            print('Игра закончена, победитель:', hod)
            break
        elif slovar['2'] == slovar['5'] == slovar['8'] != ' ':
            print('Игра закончена, победитель:', hod)
            break
        elif slovar['3'] == slovar['6'] == slovar['9'] != ' ':
            print('Игра закончена, победитель:', hod)
            break
        elif slovar['3'] == slovar['5'] == slovar['7'] != ' ':
            print('Игра закончена, победитель:', hod)
            break
        elif slovar['1'] == slovar['5'] == slovar['9'] != ' ':
            print('Игра закончена, победитель:', hod)
            break




    except ValueError:
        print("Введите цифру а не букву!")

