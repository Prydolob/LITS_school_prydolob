import random


def create_dict():
    _list = create_list()
    _tuple = []
    for i in range(len(_list)):
        _tuple.append(int(input('Enter number by index[' + str(i) + '] - ')))
    _dict = dict(zip(tuple(_tuple), _list))
    print(_dict)
    return _dict


def create_list():
    _list = []
    length_list = int(input('Enter the length of list - '))
    choice = input(
        'Choice:\n1. Fill the list by yourself. Press 1 .\n2. Fill the list by random. Press 2 .\nYour choice is ')
    if choice:
        if choice == '1':
            for i in range(length_list):
                _add_element = _list.append(int(input('Enter number by index[' + str(i) + '] - ')))
        elif choice == '2':
            for i in range(length_list):
                _add_element = _list.append(random.randint(1, 40))

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

    print(('-' * 50) + '  1  ' + ('-' * 50))
    _list = create_list()
    amount = int(input('Enter amount of max elements - '))

    _amount_of_max(_list, amount)


def second_task():
    def similar(list_1, list_2):
        list_3 = []
        for i in list_1:
            if i in list_2:
                list_3.append(i)
        print(list_3)

    print(('-' * 50) + '  2  ' + ('-' * 50))
    _list_1 = create_list()
    _list_2 = create_list()

    similar(_list_1, _list_2)


def third_task():
    def find(_list, num):
        for i in _list:
            if i < num:
                print(i, end=' ')

    print(('-' * 50) + '  3  ' + ('-' * 50))
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
        print(dict_2)

    # _dict_1 = {'1': 11, '2': 22, '3': 33}
    # print(_dict_1)
    _dict_1 = create_dict()
    _revers_dict(_dict_1)


def fifth_task():
    _str = "a b a b a a d , - -"  # 'a': 4, 'b': 2, 'd': 1, ',': 1, '-': 2


def main():
    # first_task()
    # second_task()
    # third_task()
    # fourth_task()
    pass


if __name__ == '__main__':
    main()
