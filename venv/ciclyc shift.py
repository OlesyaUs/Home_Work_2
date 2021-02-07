def shift(lst, steps):
    if steps< 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())

numbers = [4, 5, 6, 7, 8, 9, 0]
print(numbers)

shift(numbers, -4)
print(numbers)

shift(numbers, 2)
print(numbers)
