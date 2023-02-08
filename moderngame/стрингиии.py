# name = str(input('Как вас зовут? '))
# surname = str(input('Как ваша фамилия? '))
# age = int(input('Сколько вам лет? '))
# name_minus_a = name.replace('А', '')
# surname_divide = '*'.join(surname)
# name_surname_age = (name_minus_a + surname_divide) * age

# print(name_minus_a)
# print(surname_divide)
# print(name_surname_age)
# name_surname = input('What is your name, surname and your age? ')
# list_name = name_surname.split(' ')
# name = list_name[0].lower().replace('a', '')
# surname = '*'.join(list_name[1])
# age = (name + surname) * int(list_name[2])
# print(age)

# new_string = input('Enter your string:   ').lower()
# letter_list = ['a', 'u', 'i', 'e', 'o', 'y']
# empty_list = []
# for i in letter_list:
#     n = new_string.count(i)
#     empty_list.append(n)
#     if n > 1 and n < 5:
#         print(f'Буква {i} встречается {n} разa.')
#     else:
#         print(f'Буква {i} встречается {n} раз.')
#
# print(f'Всего гласных букв {sum(empty_list)}')


username = input('Введите пожалуйста свой username одним словом:  ')
middle = username.swapcase().ljust(len(username) + 1, '$')
print(middle[:len(middle)//2], '&', middle[len(middle)//2:], sep='  ')
