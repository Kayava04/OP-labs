#  Завдання 1


try:
    with open('array.txt', 'r', encoding = 'utf-8') as file:
        f = file.readlines()
        y = len(f)
        array = [[0]] * y
        maxlen = []
        for i in range(y):
            array[i] = f[i].split()
            maxlen.append(len(array[i]))
        x = max(maxlen)
        for i in range(y):
            for j in range(x - len(array[i])):
                array[i].append(0)

    sum_of_elements = 0
    count = 0

    for i in range(len(array)):
        for j in range(len(array[i])):
            sum_of_elements += int(array[i][j])
            count += 1

    result = sum_of_elements / count
    min_distance = abs(result - int(array[0][0]))
    posit = 0, 0

    for i in range(len(array)):
        for j in range(len(array[i])):
            if min_distance > abs(result - int(array[i][j])):
                posit = i, j
                min_distance = abs(result - int(array[i][j]))

    with open('result.txt', 'w', encoding = 'utf-8') as f:
        f.write('Двовимірний масив:\n')
        for i in range(len(array)):
            f.write(str(array[i]) + '\n')
        f.write(f'''\nСереднє арифметичне масиву: {result}
Мінімальна відстань від числа до середнього арифметичного: {min_distance}
Позиція елемента найближчого до середнього арифметичного: {posit}\n\n''')

except:
    print('Не можливо згенерувати масив!')