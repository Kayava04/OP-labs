from random import randint


class Trademark:
    a1 = 2010
    a2 = 2008
    a3 = 8
    a4 = 2
    a5 = 300
    b1 = 3.5
    b2 = 5.2
    b3 = 1.5
    b4 = 2.7
    b5 = 4.1

n = 10
array = [Trademark()] * n

for i in range(len(array)):
    array[i].a1 = randint(1750, 2300)
    array[i].a2 = randint(2000, 30000) / 10
    array[i].a3 = randint(1, 53)
    array[i].a4 = randint(2, 10)
    array[i].a5 = randint(250, 400)
    array[i].b1 = randint(1, 10)
    array[i].b2 = randint(5, 25)
    array[i].b3 = randint(0, 33)
    array[i].b4 = randint(1, 9)
    array[i].b5 = randint(3, 8)
    print(f'| A{[i + 1]} | >>', array[i].a1, array[i].a2, array[i].a3, array[i].a4, array[i].a5,
          f'| B{[i + 1]} | >>', array[i].b1, array[i].b2, array[i].b3, array[i].b4, array[i].b5)

ekz = Trademark()
s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = s9 = s10 = 0

for i in range(len(array)):
    s1 += array[i].a1
    s2 += array[i].a2
    s3 += array[i].a3
    s4 += array[i].a4
    s5 += array[i].a5
    s6 += array[i].b1
    s7 += array[i].b2
    s8 += array[i].b3
    s9 += array[i].b4
    s10 += array[i].b5

s1 /= len(array)
s2 /= len(array)
s3 /= len(array)
s4 /= len(array)
s5 /= len(array)
s6 /= len(array)
s7 /= len(array)
s8 /= len(array)
s9 /= len(array)
s10 /= len(array)

ekz.a1 = s1
ekz.a2 = s2
ekz.a3 = s3
ekz.a4 = s4
ekz.a5 = s5
ekz.b1 = s6
ekz.b2 = s7
ekz.b3 = s8
ekz.b4 = s9
ekz.b5 = s10

print(f'\nСередні значення: {ekz.a1}, {ekz.a2}, {ekz.a3}, {ekz.a4}, {ekz.a5}, '
                            f'{ekz.b1}, {ekz.b2}, {ekz.b3}, {ekz.b4}, {ekz.b5}')