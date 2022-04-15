#  Помічник для викладача V2.0


from random import randint
from translate import Translator
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import webbrowser as web
import turtle


#  Зміна кольору текста
print('\033[36m{}'.format(''))


main_menu = ('[1].  Нотатки', '[2].  Перекладач', '[3].  Операції над масивами', '[4].  Побудова графів', '[5].  Журнал оцінок', '[6].  Системи числення', 
             '[7].  Пошук в інтернеті', '[8].  Time_Killer', '[9].  Навчальний матеріал', '[10]. Про програму', '[0].  Вихід(Х)')
dopmenu_1 = ('[1]. Внести зміни до журнала', '[2]. Переглянути журнал', '[0]. Повернутися назад')
operations_with_array = ('[1]. Пошук мінімального та максимального елемента', '[2]. Середнє арифметичне', '[3]. Впорядкування масива', '[0]. Повернутися назад')
choose_array = ('[1]. Одновимірний масив', '[2]. Двовимірний масив', '[3]. Трьохвимірний масив', '[0]. Повернутися назад')
convert_operations = ('[1]. Двійкова система числення', '[2]. Вісімкова система числення', '[3]. Шістнадцяткова система числення', '[0]. Повернутися назад')
literature = ('1. Пол Бэрри «Изучаем программирование на Python»', '2. Марк Лутц «Изучаем Python»', '3. Марк Лутц «Программирование на Python»', '4. Дэвид Бизли, Брайан К. Джонс «Python. Книга рецептов»', 
              '5. Лучано Рамальо «Python. К вершинам  мастерства»', '6. Зед Шоу «Легкий способ выучить Python 3»', '7. Майк МакГрат «Python. Программирование для начинающих»', 
              '8. Эрик Мэтиз «Изучаем Python»', '9. Аллен Б. Дауни «Основы Python. Научитесь думать как программист»', '10. Креневич А. П. «Python у прикладах і задачах»')
op_journal = {'Мельник Владислав': '',
              'Мельник Дар\'я': '',
              'Мисько Богдан': '',
              'Михайляк Марина': '',
              'Морозюк Анастасія': '',
              'Мудренко Артем': '',
              'Онищук Олена': '',
              'Первачук Роман': '',
              'Пересунько Катерина': '',
              'Петришин Віталій': '',
              'Підруцький Дмитро': '',
              'Поліщук Анна': '',
              'Поліщук Дмитро': ''
              }


#  Ф-ції програми
def start_program():
    def preview():
        print('''
  ____                _   _             _____         _    
 / ___|_ __ ___  __ _| |_(_)_   _____  |_   _|_ _ ___| | __
| |   | '__/ _ \/ _` | __| \ \ / / _ \   | |/ _` / __| |/ /
| |___| | |  __/ (_| | |_| |\ V /  __/   | | (_| \__ \   < 
 \____|_|  \___|\__,_|\__|_| \_/ \___|   |_|\__,_|___/_|\_\\

============================================================
                      by: Bohdan Mysko
============================================================
            ''')

    def notes():
        print('Введіть, що хочете занотувати(quitN - вихід):')
        while True:
            with open('notebook.txt', 'a', encoding = 'utf-8') as f:
                note = input('>> ')
                if note == 'quitN':
                    break
                else:
                    f.write(f'{note}\n')
        print()
        dop_menu_1()

    def translator():
        translator = Translator(from_lang = input('Введіть мову, з якої хочете перекласти(Англійською): '), to_lang = input('Введіть мову, на яку хочете перекласти(Англійською): '))
        text = input('Що Ви хочете перекласти: ')
        translation = translator.translate(text)
        print(f'\nРезультат: {translation}')
        dop_menu_2()

    def search_max_and_min():
        for i in range(len(choose_array)):
            print(choose_array[i])
        print()
        choice = int(input('Виберіть пункт >> '))
        print()
        if choice == 1:
            length_of_array = int(input('Введіть довжину масиву: '))
            f_number = int(input('Введіть початок діапазону: '))
            s_number = int(input('Введіть кінець діапазону: '))
            array = [randint(f_number, s_number) for i in range(length_of_array)]
            if len(array) == 0:
                print('Розмір масива = 0\n')
                array_operations()
            print(f'Одновимірний масив: {array}')
            min_elem = max_elem = array[0]
            for i in range(len(array)):
                if array[i] < min_elem:
                    min_elem = array[i]
                elif array[i] > max_elem:
                    max_elem = array[i]
            print(f'Мінімальний елемент масива: {min_elem}\nМаксимальний елемент масива: {max_elem}')
        elif choice == 2:
            m = int(input('Кількість рядків: '))
            n = int(input('Кількість стовпців: '))
            f_number = int(input('Введіть початок діапазону: '))
            s_number = int(input('Введіть кінець діапазону: '))
            array = [[randint(f_number, s_number) for i in range(m)] for j in range(n)]
            if m == 0 or n == 0:
                print('Розмір масива = 0\n')
                array_operations()
            print('Двовимірний масив:')
            for i in array:
                print(' ' * 17, i)
            min_elem = max_elem = array[0][0]
            for i in range(len(array)):
                for j in range(len(array[i])):
                    if array[i][j] < min_elem:
                        min_elem = array[i][j]
                    elif array[i][j] > max_elem:
                        max_elem = array[i][j]
            print(f'Мінімальний елемент масива: {min_elem}\nМаксимальний елемент масива: {max_elem}')
        elif choice == 3:
            l = int(input('Введіть довжину: '))
            w = int(input('Введіть ширину: '))
            h = int(input('Введіть висоту: '))
            f_number = int(input('Введіть початок діапазону: '))
            s_number = int(input('Введіть кінець діапазону: '))
            array = [[[randint(f_number, s_number) for i in range(l)] for j in range(w)] for k in range(h)]
            if l == 0 or w == 0 or h == 0:
                print('Розмір масива = 0\n')
                array_operations()
            print('Трьохвимірний масив:')
            for i in array:
                print(' ' * 19, i)
            min_elem = max_elem = array[0][0][0]
            for i in range(len(array)):
                for j in range(len(array[i])):
                    for k in range(len(array[i][j])):
                        if array[i][j][k] < min_elem:
                            min_elem = array[i][j][k]
                        elif array[i][j][k] > max_elem:
                            max_elem = array[i][j][k]
            print(f'Мінімальний елемент масива: {min_elem}\nМаксимальний елемент масива: {max_elem}')
        elif choice == 0:
            array_operations()
        print()
        array_operations()

    def average_number():
        for i in range(len(choose_array)):
            print(choose_array[i])
        print()
        choice = int(input('Виберіть пункт >> '))
        print()
        if choice == 1:
            length_of_array = int(input('Введіть довжину масиву: '))
            f_number = int(input('Введіть початок діапазону: '))
            s_number = int(input('Введіть кінець діапазону: '))
            array = [randint(f_number, s_number) for i in range(length_of_array)]
            if len(array) == 0:
                print('Розмір масива = 0\n')
                array_operations()
            print(f'Одновимірний масив: {array}')
            sum_of_elements = 0
            count = 0
            for i in range(len(array)):
                sum_of_elements += array[i]
                count += 1
            result = sum_of_elements / count
            print(f'Середнє арифметичне = {result}')
        elif choice == 2:
            m = int(input('Кількість рядків: '))
            n = int(input('Кількість стовпців: '))
            f_number = int(input('Введіть початок діапазону: '))
            s_number = int(input('Введіть кінець діапазону: '))
            array = [[randint(f_number, s_number) for i in range(m)] for j in range(n)]
            if m == 0 or n == 0:
                print('Розмір масива = 0\n')
                array_operations()
            print('Двовимірний масив:')
            for i in array:
                print(' ' * 17, i)
            sum_of_elements = 0
            count = m * n
            for i in range(len(array)):
                for j in range(len(array[i])):
                    sum_of_elements += array[i][j]
            result = sum_of_elements / count
            print(f'Середнє арифметичне = {result}')
        elif choice == 3:
            l = int(input('Введіть довжину: '))
            w = int(input('Введіть ширину: '))
            h = int(input('Введіть висоту: '))
            f_number = int(input('Введіть початок діапазону: '))
            s_number = int(input('Введіть кінець діапазону: '))
            array = [[[randint(f_number, s_number) for i in range(l)] for j in range(w)] for k in range(h)]
            if l == 0 or w == 0 or h == 0:
                print('Розмір масива = 0\n')
                array_operations()
            print('Трьохвимірний масив:')
            for i in array:
                print(' ' * 19, i)
            sum_of_elements = 0
            count = l * w * h
            for i in range(len(array)):
                for j in range(len(array[i])):
                    for k in range(len(array[i][j])):
                        sum_of_elements += array[i][j][k]
            result = sum_of_elements / count
            print(f'Середнє арифметичне = {result}')
        elif choice == 0:
            array_operations()
        print()
        array_operations()

    def array_sorting():
        for i in range(len(choose_array)):
            print(choose_array[i])
        print()
        choice = int(input('Виберіть пункт >> '))
        print()
        if choice == 1:
            length_of_array = int(input('Введіть довжину масиву: '))
            f_number = int(input('Введіть початок діапазону: '))
            s_number = int(input('Введіть кінець діапазону: '))
            array = [randint(f_number, s_number) for i in range(length_of_array)]
            if len(array) == 0:
                print('Розмір масива = 0\n')
                array_operations()
            print(f'Одновимірний масив: {array}')
            array.sort()
            print(f'Відсортований масив: {array}')
        elif choice == 2:
            m = int(input('Кількість рядків: '))
            n = int(input('Кількість стовпців: '))
            f_number = int(input('Введіть початок діапазону: '))
            s_number = int(input('Введіть кінець діапазону: '))
            array = [[randint(f_number, s_number) for i in range(m)] for j in range(n)]
            if m == 0 or n == 0:
                print('Розмір масива = 0\n')
                array_operations()
            print('Двовимірний масив:')
            for i in array:
                print(' ' * 17, i)
            for i in range(len(array)):
                array[i].sort()
            print('\nВідсортований масив:')
            for i in array:
                print(' ' * 19, i)
        elif choice == 3:
            l = int(input('Введіть довжину: '))
            w = int(input('Введіть ширину: '))
            h = int(input('Введіть висоту: '))
            f_number = int(input('Введіть початок діапазону: '))
            s_number = int(input('Введіть кінець діапазону: '))
            array = [[[randint(f_number, s_number) for i in range(l)] for j in range(w)] for k in range(h)]
            if l == 0 or w == 0 or h == 0:
                print('Розмір масива = 0\n')
                array_operations()
            print('Трьохвимірний масив:')
            for i in array:
                print(' ' * 19, i)
            for i in range(len(array)):
                for j in range(len(array[i])):
                    array[i][j].sort()
            print('\nВідсортований масив:')
            for i in array:
                print(' ' * 19, i)
        elif choice == 0:
            array_operations()
        print()
        array_operations()

    def array_operations():
        print('Операції над масивами:')
        for i in range(len(operations_with_array)):
            print(operations_with_array[i])
        print()
        choice = int(input('Виберіть пункт >> '))
        print()
        if choice == 1:
            search_max_and_min()
        elif choice == 2:
            average_number()
        elif choice == 3:
            array_sorting()
        elif choice == 0:
            menu()

    def graph_creator():
        try:
            matrix_1 = []
            i = 0
            print('Для того, щоб заповнити квадратну матрицю, введіть через пробіл 0 або 1(end - Вихід): ')
            while True:
                numbers = input()
                if numbers == 'end':
                    break
                matrix_1.append(numbers.split())
                for j in range(len(matrix_1[i])):
                    matrix_1[i][j] = int(matrix_1[i][j])
                i += 1
            print('\nМатриця суміжностей:', *matrix_1, sep = '\n')
            question = input('\nЗобразити орієнтований граф(Y - так, N - ні)? ')
            if question == 'Y' or question == 'y':
                G = nx.DiGraph(np.matrix(matrix_1))
                nx.draw(G, with_labels = True, node_size = 300, arrows = True)
                plt.show()
            elif question == 'N' or question == 'n':
                G = nx.DiGraph(np.matrix(matrix_1))
                nx.draw(G, with_labels = True, node_size = 300, arrows = False)
                plt.show()
        except:
            print('Не можливо згенерувати граф!!!')
        dop_menu_8()

    def journal():
        with open('journal.txt', 'w', encoding = 'utf-8') as f:
            f.write('Журнал оцінок:\n\n')
            for k, v in op_journal.items():
                f.write(f'{k} - {v}\n')
        with open('journal.txt', 'r', encoding = 'utf-8') as f:
            print(f.read())
        dop_menu_3()

    def convertor(x: int) -> int:
        print()
        for i in range(len(convert_operations)):
            print(convert_operations[i])
        print()
        choice = int(input('Виберіть пункт >> '))
        print()
        if choice == 1:
            return f'Число {x} = {bin(x)[2:]}'
        elif choice == 2:
            return f'Число {x} = {oct(x)[2:]}'
        elif choice == 3:
            return f'Число {x} = {hex(x)[2:]}'
        elif choice == 0:
            menu()

    def web_searcher(what: str) -> str:
        result = web.open_new_tab(f'https://www.google.com.ua/search?q={what}')
        input('\nНатисніть будь-яку клавішу...')
        dop_menu_5()

    def education():
        print('Список літератури:')
        for i in range(len(literature)):
            print(literature[i])
        input('\nНатисніть будь-яку клавішу...')
        menu()

    def time_killer():
        print('[1]. Гра\n[2]. Прікалюшка\n[0]. Повернутися назад\n')
        choice = int(input('Виберіть пункт >> '))
        if choice == 1:
            trys = int(input('Введіть кількість спроб: '))
            machine = randint(0, 20)
            for i in range(trys):
                user = int(input('Спробуйте вгадати число від 0 до 20 >> '))
                if user == machine:
                    print('Ви вгадали число!')
                elif user > machine:
                    print('Ви ввели завелике число!')
                else:
                    print('Ви ввели замале число!')
            print(f"\nЧисло загадане комп'ютером: {machine}")
        elif choice == 2:
            t = turtle.Turtle()
            s = turtle.Screen()
            s.bgcolor('black')
            t.width(2)
            t.speed(15)
            col = ('white', 'pink', 'cyan')
            for i in range(300):
                t.pencolor(col[i % 3])
                t.forward(i * 4)
                t.right(121)
        elif choice == 0:
            menu()
        input('\nНатисніть будь-яку клавішу...')
        dop_menu_7()

    def about():
        print('''
╔══════════════════════════════════════════╗
║                                          ║
║     Програма "Помічник для викладача"    ║
║         Розробив: Мисько Богдан          ║
║              група КН-21-А               ║
║                                          ║
╚══════════════════════════════════════════╝
            ''')
        input('Натисніть будь-яку клавішу...')
        menu()

    def dop_menu_1():
        print('[1]. Продовжити запис\n[2]. Прочитати нотатки\n[0]. Повернутися назад\n')
        choice = int(input('Виберіть пункт >> '))
        print()
        if choice == 1:
            notes()
        elif choice == 2:
            print('Нотатки:')
            with open('notebook.txt', 'r', encoding = 'utf-8') as f:
                print(f.read())
            dop_menu_1()
        elif choice == 0:
            menu()

    def dop_menu_2():
        print('\n[1]. Продовжити переклад\n[0]. Повернутися назад\n')
        choice = int(input('Виберіть пункт >> '))
        print()
        if choice == 1:
            translator()
        elif choice == 0:
            menu()

    def dop_menu_3():
        for i in range(len(dopmenu_1)):
            if dopmenu_1[i] == '[2]. Переглянути журнал':
                continue
            print(dopmenu_1[i])
        print()
        choice = int(input('Виберіть пункт >> '))
        print()
        if choice == 1:
            student = input('Введіть ім\'я студента або студентки: ')
            try:
                op_journal[student] += input('Введіть бали: ') + '  '
            except KeyError:
                print('У журналі немає такого студента!\n')
            with open('journal.txt', 'w', encoding = 'utf-8') as f:
                f.write('Журнал оцінок:\n\n')
                for k, v in op_journal.items():
                    f.write(f'{k} - {v}\n')
            input('\nНатисніть будь-яку кнопку...')
            dop_menu_4()
        elif choice == 0:
            menu()

    def dop_menu_4():
        print()
        for i in range(len(dopmenu_1)):
            print(dopmenu_1[i])
        print()
        choice = int(input('Виберіть пункт >> '))
        print()
        if choice == 1:
            student = input('Введіть ім\'я студента або студентки: ')
            try:
                op_journal[student] += input('Введіть бали: ') + '  '
            except KeyError:
                print('У журналі немає такого студента!\n')
            with open('journal.txt', 'w', encoding = 'utf-8') as f:
                f.write('Журнал оцінок:\n\n')
                for k, v in op_journal.items():
                    f.write(f'{k} - {v}\n')
            input('Натисніть будь-яку кнопку...')
            dop_menu_4()
        elif choice == 2:
            with open('journal.txt', 'r', encoding = 'utf-8') as f:
                print(f.read())
            dop_menu_4()
        elif choice == 0:
            menu()

    def dop_menu_5():
        print('\n[1]. Продовжити пошук в Інтернеті\n[0]. Повернутися назад\n')
        choice = int(input('Виберіть пункт >> '))
        print()
        if choice == 1:
            web_searcher(input("Введіть, що хочете знайти: "))
        elif choice == 0:
            menu()

    def dop_menu_6():
        print('\n[1]. Продовжити\n[0]. Повернутися назад\n')
        choice = int(input('Виберіть пункт >> '))
        print()
        if choice == 1:
            number = int(input('Введіть число: '))
            print(convertor(number))
            dop_menu_6()
        elif choice == 0:
            menu()

    def dop_menu_7():
        print('\n[1]. Продовжити гратися\n[0]. Повернутися назад\n')
        choice = int(input('Виберіть пункт >> '))
        print()
        if choice == 1:
            time_killer()
        elif choice == 0:
            menu()

    def dop_menu_8():
        print('\n[1]. Продовжити працювати із графами\n[0]. Повернутися назад\n')
        choice = int(input('Виберіть пункт >> '))
        print()
        if choice == 1:
            graph_creator()
        elif choice == 0:
            menu()

    def menu():
        preview()
        for i in range(len(main_menu)):
            print(main_menu[i])
        print()
        choice = int(input('Вкажіть пункт >> '))
        print()
        if choice == 1:
            notes()
        elif choice == 2:
            translator()
        elif choice == 3:
            array_operations()
        elif choice == 4:
            graph_creator()
        elif choice == 5:
            journal()
        elif choice == 6:
            number = int(input('Введіть число: '))
            print(convertor(number))
            dop_menu_6()
        elif choice == 7:
            web_searcher(input("Введіть, що хочете знайти: "))
        elif choice == 8:
            time_killer()
        elif choice == 9:
            education()
        elif choice == 10:
            about()
        elif choice == 0:
            print('Ви успішно вийшли!')
            quit()
    menu()


'''Перевірка чи файл не є імпортованим. Старт програми!!!'''
if __name__ == '__main__':
    start_program()