import random


def tasks_info(i1):
    task1 = '''
    Написати функцію, яка буде  приймати два аргументи
    (перший обов’язковий, інший буде мати значення за замовчуванням),
    перший це список, у якому буде проводитись пошук, другий - n (int) значень, які шукаються.
    Так от, задача у тому, щоб знайти n найбільших значень і повернути їх у новому спискові із функції.
    '''
    task2 = '''
    Написати функцію, яка буде приймати два аргументи(списки),
    а повертати новий список створений з елементів, які є одразу у двох списках.
    (Щось подібне до того, що ми робили на останньому занятті)
    '''
    task3 = '''
    Написати функцію, яка буде шукати всі прості числа менші за число,
    яке буде приймати функція у якості аргументу.
    '''
    task4 = '''
    Так як ключі у словнику відсортовані, то напишіть функцію,
    яка буде приймати у якості аргументу словник, а повертати новий словник з оберненою послідовністю ключів.
    '''
    task5 = '''
    Написати функцію, яка буде приймати рядок (str), а на виході буде повертати словник,
    у якому в якості ключів - символи, що зустрічаються, значення - їхня кількість y рядоку.
    (Великі та їх аналоги малі символи вважати за одні і ті ж)
    '''

    if i1 == 1:
        print(('-' * 50) + '  1  ' + ('-' * 50))
        print(task1)
    elif i1 == 2:
        print(('-' * 50) + '  2  ' + ('-' * 50))
        print(task2)
    elif i1 == 3:
        print(('-' * 50) + '  3  ' + ('-' * 50))
        print(task3)
    elif i1 == 4:
        print(('-' * 50) + '  4  ' + ('-' * 50))
        print(task4)
    elif i1 == 5:
        print(('-' * 50) + '  5  ' + ('-' * 50))
        print(task5)


def create_dict():
    _values = create_list()
    _keys = []
    for i in range(len(_values)):
        _keys.append(int(input('Enter number by index[' + str(i) + '] - ')))

    _dict = dict(zip(tuple(_keys), _values))
    print('Created dict: ' + str(_dict))
    return _dict


def create_list():
    _list = []
    length_list = int(input('Enter the length of list - '))
    choice = input(
        'Choice:\n1. Fill the list by yourself. Press 1 .\n2. Fill the list by random. Press 2 .\nYour choice is ')
    if choice:
        if choice == '1':
            for i in range(length_list):
                _list.append(int(input('Enter number by index[' + str(i) + '] - ')))
        elif choice == '2':
            for i in range(length_list):
                _list.append(random.randint(1, 40))

    print(_list)
    return _list


def first_task():
    def _amount_of_max(list_1, n):
        list_2 = []

        for element in range(n):
            _max = max(list_1)
            list_2.append(_max)
            list_1.remove(_max)
        print(list_2)

    _list = create_list()
    amount = int(input('Enter amount of max elements - '))

    _amount_of_max(_list, amount)


def second_task():
    def similar(list_1, list_2):
        list_3 = []
        for i in list_1:
            if i in list_2 and i not in list_3:
                list_3.append(i)
        if not list_3:
            print('There were not similar numbers in those lists!')
        else:
            print(list_3)

    _list_1 = create_list()
    _list_2 = create_list()

    similar(_list_1, _list_2)


def third_task():
    def find(_list, num):
        _result_list = []
        for i in _list:
            if i < num:
                _result_list.append(i)
        if not _result_list:
            print('There are not numbers which are less than ' + str(num))
        else:
            print(_result_list)

    print('')

    _list = create_list()
    number = int(input('Enter the number - '))

    find(_list, number)


def fourth_task():
    def _revers_dict(dict_1):
        dict_2_keys = []
        dict_2_values = []
        for key, value in _dict_1.items():
            dict_2_keys.append(key)
            dict_2_values.append(value)
        dict_2_keys.reverse()
        dict_2 = dict(zip(tuple(dict_2_keys), dict_2_values))
        print('\nReversed new dict' + str(dict_2) + '\n')

    _dict_1 = create_dict()
    _revers_dict(_dict_1)


def fifth_task():
    def _find(key):
        nonlocal _str
        return _str.count(key)

    _str = input("Enter sum symbols - ").lower()
    _values = []
    _key = _str.split()
    _key = ''.join(_key)
    _keys = set(_key)

    for i in _keys:
        _values.append(_find(i))
    print('')

    _dict = dict(zip(set(_keys), _values))
    print(_dict)
    print('-' * 105)


def main():
    for i in range(6):
        tasks_info(i)
        if i == 1:
            first_task()
        elif i == 2:
            second_task()
        elif i == 3:
            third_task()
        elif i == 4:
            fourth_task()
        elif i == 5:
            fifth_task()


if __name__ == '__main__':
    main()
