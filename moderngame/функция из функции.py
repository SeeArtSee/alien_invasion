def cylinder():
    r = float(input())
    h = float(input())
    # площадь боковой поверхности цилиндра:
    side = 2 * 3.14 * r * h
    # площадь одного основания цилиндра:
    circle = 3.14 * r ** 2
    # полная площадь цилиндра:
    full = side + 2 * circle
    ful = full + 25
    return full, ful


def call_cylinder():
    full = cylinder()
    ful = cylinder()
    print(full, ful)


call_cylinder()