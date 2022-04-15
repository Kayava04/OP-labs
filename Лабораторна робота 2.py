#  Варіант 3


#  Завдання 1

array = [0] * int(input("Введіть довжину масиву >> "))
print()

for i in range(len(array)):
    array[i] = int(input(f"Введіть елемент масиву номер {i+1} >> "))

array_max = max(array)
array_min = min(array)

for i in range(len(array)):
    if array[i] == array_max:
        max = i
        break

for i in range(len(array)):
    if array[i] == array_min:
        min = i

print()
print(f"Відстань = {abs(max - min) - 1}")
print()

#  Завдання 2

numbers = []
i = 1

print("Щоб закінчити ввід данних, напишіть 'end'")
print()

while True:
    x = input(f"Введіть x{i} >> ")
    i += 1
    if x == "end":
        break
    numbers.append(int(x))

print()
print(f"Невідсортований варіант >> {numbers}")
numbers.sort()
print(f"Відсортований варіант >> {numbers}")