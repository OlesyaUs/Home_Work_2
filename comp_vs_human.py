
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
win_numbers = {1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {3, 5, 7}, {1, 5, 9}

def bot():
    player_numbers = []
    for i in slovar:
        if slovar[str(i)] == 'X':
            print(i)
            player_numbers.append(str(i))
    print(player_numbers)
    hod_set = {}
    for j in win_numbers:
        set_player = set(player_numbers)
        hod_set = j - set_player
        print(hod_set)
        if len(hod_set) == 1:
            hod_list = list(hod_set)
            print(hod_list[0])
            return hod_list[0]
    if slovar['5'] ==" ":
        return 5
    list_state = [1, 3, 7, 9]
    for h in list_state:
        if slovar [str(h)] ==' ':
        return h
    for g in slovar


while True:
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
         -----  -----  -----
'''
    print(n)








