import random


def zad1():
    lst1 = [random.randint(1, 10) for i in range(10)]
    print(lst1)
    for i in lst1:
        if lst1.count(i) == 1:
            print(i)
    pass


def zad2():
    lst2 = [random.randint(1, 10) for i in range(10)]
    pair_counter = 0
    print(lst2)
    for i in lst2:
        for j in lst2[i::]:
            if i == j:
                pair_counter += 1
    print(pair_counter)


def zad3():
    c_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
    c_2 = (45, 21, 124, 76, 5, 23, 91, 234)
    sum_1 = 0
    sum_2 = 0
    min_1 = c_1[0]
    min_2 = c_2[0]
    max_1 = c_1[0]
    max_2 = c_2[0]
    for i in c_1:
        sum_1 += i
        if min_1 > i:
            min_1 = i
        if max_1 < i:
            max_1 = i

    for i in c_2:
        sum_2 += i
        if min_2 > i:
            min_2 = i
        if max_2 < i:
            max_2 = i

    if sum_1 > sum_2:
        print(f'{sum_1} > {sum_2}')
    else:
        print(f'{sum_1} < {sum_2}')
    print(min_1, max_1, min_2, max_2)


def zad4():
    aim_str = "An apple a day keeps the doctor away".replace(' ', '')
    dct = {}
    for i in aim_str:
        dct[str(i)] = aim_str.count(i)
    print(dct)


def zad5():
    condit = {'cake':
              {'descript': 'cake description',
                   'price for 100 gramm': 100,
                   'values for 100 gramm': 1000},
              'cupcake':
                  {'descript': 'cupcake description',
                   'price for 100 gramm': 200,
                   'values for 100 gramm': 1000},
              'muffin':
                  {'descript': 'muffin description',
                   'price for 100 gramm': 300,
                   'values for 100 gramm': 1000},
              }
    user_choose = 0
    time_choose = 0
    prod_choose = ''
    while user_choose != 6:

        user_choose = int(input('Выберите пункт меню:\n1. Посмотреть описание.\
        \n2. Посмотреть цену.\
        \n3. Посмотреть количество.\
        \n4. Вся информация.\
        \n5. Приступить к покупке\
        \n6. До свидания\n'))

        if user_choose == 1:
            for key in condit.keys():
                print(f'{key}-{condit[key]["descript"]}')

        if user_choose == 2:
            for key in condit.keys():
                print(f'{key} - {condit[key]["price for 100 gramm"]}')
        if user_choose == 3:
            for key in condit.keys():
                print(f'{key} - {condit[key]["values for 100 gramm"]}')
        if user_choose == 4:
            for key in condit.keys():
                print(f'{key} - {condit[key]["descript"]},{condit[key]["price for 100 gramm"]},\
                    {condit[key]["values for 100 gramm"]}')
        if user_choose == 5:
            number_of = 0
            time_choose = input('Выбери продукт:\n1.Торт.\n2.Пирожное.\n3.Маффин.\n')
            number_of = input('Сколько?: ')
            if number_of == 'n':
                break
            if int(time_choose) == 1:
                prod_choose = 'cake'
            elif int(time_choose) == 2:
                prod_choose = 'cupcake'
            elif int(time_choose) == 3:
                prod_choose == 'muffin'
            elif time_choose == 'n' or number_of == 'n':
                break
            else:
                print('Ошибка выбора продукта')
                break
            if int(number_of) > condit[prod_choose]["values for 100 gramm"]:
                print(f'Слишком много, на складе:{condit[prod_choose]["values for 100 gramm"]}')
            else:
                print(f'Стоимость заказа: {int(number_of) * condit[prod_choose]["price for 100 gramm"]}')
                condit[prod_choose]["values for 100 gramm"] -= int(number_of)
                print(f'Товара осталось:{condit[prod_choose]["values for 100 gramm"]}')


def zad6():
    lst1 = set(random.randint(0, 10) for i in range(random.randint(0, 10)))
    lst2 = set(random.randint(0, 10) for i in range(random.randint(0, 10)))
    counter = 0
    print(lst1)
    print(lst2)
    for i in lst1:
        if i in lst2:
            counter += 1
    print(counter)


def zad7():
    try:
        1/0
    except ZeroDivisionError:
        print('ZeroDivisionError')
    finally:
        print('Finally')


def zad8():
    with open('Test.txt', 'r', encoding='utf-8') as file:
        certain_number = 0
        col_vo = 0
        print_text = []
        for i in file:
            print_text = i.strip().split(' ')
            certain_number += int(print_text[2])
            col_vo += 1
            if int(print_text[2]) < 3:
                print("Students with mark below 3: ", ' '.join(print_text[:2]))
        certain_number /= col_vo
        print(f'Middle value: {certain_number}')


task_choose = 0
while task_choose < 9:
    task_choose = int(input('choose task: '))
    if task_choose == 1:
        print("1. Дан список. Выведите те его элементы, которые встречаются в списке только один раз."
                "Элементы нужно выводить в том порядке, в котором они встречаются в списке")
        zad1()
    elif task_choose == 2:
        print("2. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу."
                "Считается, что любые два элемента, равные друг другу образуют одну пару,"
                "которую необходимо посчитать.")
        zad2()
    elif task_choose == 3:
        print("3. Даны два кортежа:\n"
        "C_1 = (35, 78,21,37, 2,98, 6, 100, 231)\n"
        "C_2 = (45, 21,124,76,5,23,91,234)\n"
        "Необходимо определить:\n"
        "1) Сумма элементов какого из кортежей больше и вывести соответствующее"
        "сообщение на экран (Сумма больше в кортеже - ..)\n"
        "2) Вывести на экран порядковые номера минимальных и максимальных элементов"
        "этих кортежей")
        zad3()
    elif task_choose == 4:
        print("4.Создайте словарь из строки ' An apple a day keeps the doctor away' следующим"
                "образом: в качестве ключей возьмите символы строки, а значениями пусть будут"
                "числа, соответствующие количеству вхождений данной буквы в строку.")
        zad4()
    elif task_choose == 5:
        print("5.Клиент приходит в кондитерскую. Он хочет приобрести один или несколько видов продукции,"
              "а также узнать её состав. Реализуйте кондитерскую. У вас есть словарь,"
              "где ключ – название продукции (торт, пирожное, маффин и т.д.)."
              "Значение – список, который содержит состав, цену (за 100гр) и кол-во (в граммах).\n"
              "Предложите выбор:\n"
              "1. Если человек хочет посмотреть описание: название – описание\n"
              "2. Если человек хочет посмотреть цену: название – цена.\n"
              "3. Если человек хочет посмотреть количество: название – количество.\n"
              "4. Всю информацию.\n"
              "5. Приступить к покупке:\n"
              "С клавиатуры вводите название торта и его кол-во. n – выход из программы."
              "Посчитать цену выбранных товаров и сколько товаров осталось в изначальном"
              "списке\n"
              "6. До свидания")
        zad5()
    elif task_choose == 6:
        print("6.Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке,"
                "так и во втором.")
        zad6()
    elif task_choose == 7:
        print("7. Напишите программу, демонстрирующую работу try\ except\ finally")
        zad7()
    elif task_choose == 8:
        print("8. В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную."
                "Вывести на экран всех учащихся, чья оценка меньше 3 баллов и посчитать средний балл по классу")
        zad8()
