import random
# # print(type(4 < 3))
# a = 'You are Senior'
# b = int(input("Whats your favorite number ?  "))
# print(a if b > 10 else 'only junior')
# while True:
#     password = input('Введите пароль, который содержит только 3 цифр - ')
#     if len(password) > 3 or len(password) < 3:
#         print('Ваш пароль должен быть только в 3 символа')
#     elif password.isdigit():
#         print(f'У вас крутой {password} пароль сохранён ')
#         break
#     else:
#         print('В вашем пароле есть буквы')


# points = input('Введите количество баллов по трём предметам через запятую ').split(',')
# b = []
# # points_list = points.split(',')
# [b.append(int(i)) for i in points]
#
#         # Рассчитывается средний балл
# gpa = round(sum(b)/len(b), 1)
# print(f'Ваш срелний балл равен: {gpa}, а проходной 69 баллов')
# if gpa > 69:
#     print('Вы допушены к экзаменам, поздравляем!!!')
# else:
#     print(f'Вам не хватило {round(69-gpa,1)} балла, нужно ещё поработать.')
# print(len(b))
while True:
    words_for_play = ['Камень', 'Ножницы', 'Бумага']
    words_for_computer = random.choice(words_for_play)
    print('Давай поиграем с компьютером в игру: Камень,Ножницы,Бумага '
          'Если хотите выйти нажмите n' )
    word_of_player = input('Введите ваше слово: ')
    if words_for_computer == word_of_player:
        print(f'Твоё слово {word_of_player} и моё {words_for_computer} значит ничья.')
    elif words_for_computer == 'Ножницы' and word_of_player == 'Бумага':
        print('Ножницы режут бумагу, я победил')
    elif words_for_computer == 'Ножницы' and word_of_player == 'Камень':
        print('Камень бьёт ножницы, ты победил')
    elif words_for_computer == 'Камень' and word_of_player == 'Бумага':
        print('Камень бьёт бумагу, я победил')
    elif words_for_computer == 'Бумага' and word_of_player == 'Ножницы':
        print('Ножницы режут бумагу, ты победил')
    elif words_for_computer == 'Бумага' and word_of_player == 'Камень':
        print('Камень бьёт бумагу, ты победил')
    elif word_of_player == 'n':
        break

    print(words_for_computer)


