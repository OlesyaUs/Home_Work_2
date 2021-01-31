k = [1]
for i in k:
    print('введите число number1')
    number1 = int(input())
    print('ведите число number2')
    number2 = int(input())
    operation = input("Введите операцию: ")

    if operation == "+":
        print('Сумма ' + str(number1) + " + " + str(number2) + " = " + str(number1+number2))
    elif operation == "-":
        print('Разность number1-number2=', number1-number2)
    elif operation == "/":
        print('Результат деления number1/number2=', number1/number2)
    elif operation == "*":
        print('Результат умножения number1*number2=', number1*number2)
    elif operation == "//":
        print('Результат целочисленного деления number1//number2=', number1 // number2)
    elif operation == "%":
        print('Остаток от деления number1%number2=', number1 % number2)
    elif operation == "**":
        print('Возведение в степень number1**number2=', number1 ** number2)
    w_stop = input("Введите слово stop для выхода для продолжения нажмите enter")

    if w_stop == 'stop':
        break
    else:
        k.append(i)

