print('введите число number1=')
number1 = int(input())
print('введите число number2=')
number2 = int(input())
operation = input("Введите операцию: ")

if operation == "+":
    print('Сумма ' + str(number1) + " + "+ str(number2) + " = " + str(number1+number2))
elif operation == "-":
    print('Разность number1-number2', number1-number2)
elif operation == "/":
    print('Результат деления number1/number2',number1/number2)
elif operation == "*":
    print('Результат умножения number1*number2',number1*number2)