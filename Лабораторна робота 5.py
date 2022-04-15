from random import randint


m = int(input('Введіть ширину: '))
n = int(input('Введіть довжину: '))
k = int(input('Введіть висоту: '))

array = [[[randint(0, 7) for i in range(m)] for j in range(n)] for h in range(k)]
print('\nТрьохвимірний масив:')
[print(' ' * 19, i) for i in array]

new_array = [[],[],[],[],[],[],[],[]]
results = []
length = m * n * k

for i in range(len(array)):
    for j in range(len(array[i])):
        for k in range(len(array[i][j])):
            for h in range(8):
                if array[i][j][k] == h:
                    new_array[h].append(array[i][j][k])

for i in range(len(new_array)):
    results.append(round((len(new_array[i]) / length) * 100, 1))

print(f'\nКількість елементів в масиві = {length}\n')
print('Масив із упорядкованими копалинами:', *new_array, sep = '\n')
print('\nВідсоток кожної корисної копалини від загальної кількості корисних копалин:')
[print(f'{i} %') for i in results]