from random import randint


m = 10
n = 10

array = [[randint(-1000, 1000) for i in range(m)] for j in range(n)]

if len(array) == 0:
    print('Розмір масиву = 0')
    quit()

print('Двовимірний масив:')
for i in range(len(array)):
    print(' ' * 17, array[i])


#  Завдання 1
sum_of_elements = 0
count = 0

for i in range(len(array)):
    for j in range(len(array[i])):
        sum_of_elements += array[i][j]
        count += 1

result = sum_of_elements / count
min_distance = abs(result - array[0][0])

for i in range(len(array)):
    for j in range(len(array[i])):
        if min_distance > abs(result - array[i][j]):
            pos = i, j
            min_distance = abs(result - array[i][j])

print(f'''\nСереднє арифметичне масиву: {result}
Мінімальна відстань від числа до середнього арифметичного: {min_distance}
Позиція елемента найближчого до середнього арифметичного: {pos}\n\n''')


#  Завдання 2
max_elem = array[0][0]

for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] > max_elem:
            max_elem = array[i][j]

print(f'Максимальний елемент: {max_elem}')

for i in range(len(array)):
    try:
        pos = array[i].index(max_elem)
        pos1 = i
    except ValueError:
        continue

for i in range(len(array)):
    for j in range(len(array[i])):
        if i != pos1 and j != pos:
            array[i][j] = -array[i][j]

print('Масив зі зміненими знаками:')
for i in range(len(array)):
    print(' ' * 26, array[i])