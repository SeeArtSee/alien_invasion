class Person:
    def __init__(self, name, surname, place_of_birthday):
        self.name = name
        self.surname = surname
        self.place_of_birthday = place_of_birthday
        print("What is your name?")

    def get_name(self):
        nime = input("Введите ваше имя  ")
        print(f'Пока {nime}')

    def get_age(self, y):
        a = int(input("Введите год рождения "))
        x = y - a
        print(f"ваш возраст {x}")

    def print_of(self):
        print(F'Ваше имя {self.name}, фамилия {self.surname} ,место рождения {self.place_of_birthday}')


# p1 = Person("Albert", "Setenv", "Further")
# p2 = Person("Alberto", "Semyonov", "Funtoo")
# p3 = Person(34, 423, 345)
# p4 = Person(1, 1, 1)
# p1.print_of()
# p2.print_of()
# p1.get_age(2022)
# p2.get_age(2022)
# p3.print_of()
# p3.get_name()


class Circle:
    PI = 3.141592653589793238462643
    Q = 0

    def __init__(self, radius):
        self.radius = radius
        self.radius = int(input(f'Какой радиус вашей окружности? '))
        Circle.Q += 1

    def get_circumference(self):
        l = 2 * self.PI * self.radius
        print(f'Длина вашей окружности равна {l}')

    def get_area_of_circle(self):
        s = 2 * Circle.PI * self.radius ** 2
        print(f'Площадь вашего круга равна {s}')


# o1 = Circle(0)
# o2 = Circle(0)
# o1.get_circumference()
# o1.get_area_of_circle()
# o2.get_circumference()
# o2.get_area_of_circle()
# o3 = Circle(0)
# o3.get_circumference()
# o3.get_area_of_circle()
# o4 = Circle(0)
# o5 = Circle(0)
# print(Circle.Q)


class Soda:
    def __init__(self, ingredient):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def show_my_drink(self):
        if self.ingredient:
            print(f'Газировка и {self.ingredient}')
        else:
            print('Обычная газировка')


# Тесты
# drink1 = Soda(1)
# drink2 = Soda('малина')
# drink3 = Soda(5)
# drink1.show_my_drink()
# drink2.show_my_drink()
# drink3.show_my_drink()

class Numbers:
    # Класс Numbers выполняет разные операции с числами
    def __init__(self):
        self.x = None
        self.y = None
        self.z = None
        self.a = None
        self.l = None

    def convert(self):
        self.x = int(input("Сколько километров вы хотите перевести в мили  "))
        print(f'при переводе {self.x}км в мили получится {self.x * 1.609} миль')

    def area(self):
        self.y = int(input("Задайте высоту прямоугольника "))
        self.z = int(input("Задайте длину прямоугольника "))
        print(f'Площадь вашего прямоугольнитка равна {self.y * self.z}')

    def parity(self):
        self.a = int(input("Задайте любое число для проверки его чётности "))
        if self.a % 2 == 0:
            print(f'Ваше число {self.a} чётно')
        else:
            print(f'Ваше число {self.a} не чётно')

    def lists(self):
        self.l = [1, 'dfsdfsdf', 4, 6]
        for i in self.l:
            print(i)
        print(self.l)


# con = Numbers()
# are = Numbers()
# par = Numbers()
# con.convert()
# are.area()
# par.parity()
# con.lists()

# n = int(input("Задайте любое число от 0 до 20 "))
# print(f'Сейчас мы возведём в степень все числа от 0 до вашего числа {n}')
# k = int(input("Задайте степень в которую вы хотите возвести эти числа "))


def my_function(n, k):
    i = 0
    t = 0
    if n > 20:
        print(0)
    elif n % 2 == 0:
        for i in range(1, n+1):
            i = i ** k
            print(f'Если число {i ** (1./k) } возвести в степень {k} получится {i}')
        for t in range(n, i):
            t += t
    print(f'Сумма ваших чисел равна {t}')


# my_function(n, k)


# import pygame
# from pygame.draw import *
#
# pygame.init()
#
# FPS = 30
# screen = pygame.display.set_mode((900, 800))


# rect(screen, (255, 0, 255), (100, 100, 200, 200))
# rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
# polygon(screen, (255, 255, 0), [(100,100), (200,50),
#                                (300,100), (100,100)])
# polygon(screen, (0, 0, 255), [(100,100), (200,50),
#                                (300,100), (100,100)], 5)
# circle(screen, (0, 255, 0), (200, 175), 50)
# circle(screen, (255, 255, 255), (200, 175), 50, 5)

# for i in range(1, 300, 5):
#     # circle(screen, (255, 255, 255), (450, 450), i, 1)
#     circle(screen, (0, 255, 0), (i+200, i+200), i, 1)
#     polygon(screen, (0, 0, 255), [(100, 100), (200, 50),
#                                   (56, i), (i, 76)], 1)
#     polygon(screen, (255, 255, 0), [(100, 100), (200, 50),
#                                     (300, 100), (100, i)], 1)
#     rect(screen, (255, 0, 255), (i, 100, i, 200),2)
#     rect(screen, (0, 0, 255), (100, i, 200, i), 2)
#
# pygame.display.update()
# clock = pygame.time.Clock()
# finished = False
#
# while not finished:
#     clock.tick(FPS)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             finished = True
#
# pygame.quit()


print("\a")