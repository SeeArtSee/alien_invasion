import decimal
import math
#from math import pi
# year_birthday = int(input('Введите год своего рождения  '))
#month_birthday = int(input('Введите месяц своего рождения   '))
#day_of_birthday = int(input('Введите день своего рождения   '))
#s = year_birthday + month_birthday + day_of_birthday
#print(f'Итак вы родились {day_of_birthday} {month_birthday} {year_birthday} года.')
#print(f'Если сложить все числа вашего дня рождения, то получится {s}')

#print('Обучение на курсах Makers Bootcamp стоит 600$')
#course_price = 600
#discount = int(input('Введите процент вашей скидки за обучение '))
#discount_course_price = course_price - discount*6
#print(f'Итак ваша скидка за обучение составляет {discount*6}$\n'
#      f' значит вы должны заплатить {discount_course_price}$.')

#print('Давайте найдём площадь и длину круга.')
#radius = int(input('Введите пожалуйста радиус вашего круга '))
#area_of_a_circle = pi*radius**2
#circumference = 2*pi*radius
#print(f'Итак, площадь круга равна {round(area_of_a_circle,2)}\n '
#      f'Длина окружности равна {round(circumference,2)}')

print(dir(decimal))
print(dir(math))

print(math.sqrt(361))
print(bin(-1))
print(hex(-1))
print(oct(-100))
a = 'Сеньёр-разработчик Семёнов Артём Юрьевич'
c = ['1', '2', '3']
b = 'Я хочу тебя поздравить'
print(a[7:18])
print(a[::-1])
print(b[::1])
print(b.split(','))
print('*'.join(a))
#print(a.find('Семёнов'))
#print(a.replace('С', 'Х'))