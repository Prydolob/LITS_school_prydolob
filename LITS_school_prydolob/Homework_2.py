print('1.')
# Зчитати з консолі число і вивести назад його варіанти різних
# представленнях : бінарному, вісімковому, шістнадцяткова - системи числення.

# systems_of_calculation = ('bin', 'oct', 'dec', 'hex')
# number = int(input('Input your number : '))
#
# if number <= 1000:
#     choice_format = input('Choice format of str: 1 - .format, 2 - f"" - ')
#     if choice_format == '1':
#
#         print("  bin\t\toct\t\tdec\t\thex\n{0:b}\t\t{0:o}\t\t{0:d}\t\t{0:x}".format(number))
#     elif choice_format == '2':
#         print(
#             f"  {systems_of_calculation[0]}\t\t{systems_of_calculation[1]}\t\t{systems_of_calculation[2]}\t\t{systems_of_calculation[3]}\n"
#             f"{number:b}\t\t{number:o}\t\t{number:d}\t\t{number:x} ")
# else:
#     print("Error. Your number is more than 1000!")

print('2.')
# Зчитати послідовно два рядки, які повинні відігравати роль електронної пошти
# та її підтвердження. У відповідь ваша програма повинна вивести повідомлення,
# що все ок або повідомлення про те, що пошти не співпадають.

email_1 = input('Enter your email       : ').strip().lower()
email_2 = input('Enter your email again : ').strip().lower()
if '@' in email_1 and '@' in email_2 and '.' in email_1 and '.' in email_2:
    if email_1 == email_2:
        print('Ok')
else:
    print('This is not EMAIL!!!')

    print(email_1, email_2)
