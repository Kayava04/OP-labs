#  Завдання 2


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

    max_elem = int(array[0][0])

    for i in range(len(array)):
        for j in range(len(array[i])):
            if int(array[i][j]) > max_elem:
                max_elem = int(array[i][j])

    pos = 0
    pos1 = 0

    for i in range(len(array)):
        try:
            pos = array[i].index(max_elem)
            pos1 = i
        except ValueError:
            continue

    for i in range(len(array)):
        for j in range(len(array[i])):
            if i != pos1 and j != pos:
                array[i][j] = -int(array[i][j])

    with open('result.txt', 'w', encoding = 'utf-8') as f:
        f.write(f'''Максимальний елемент: {max_elem}\n
Масив зі зміненими знаками:\n''')
    for i in range(len(array)):
        f.write(str(array[i]) + '\n')

except:
    print('Не можливо згенерувати масив!')