# Определение кодов регионов

INSIDE = 0  # 0000

LEFT = 1  # 0001

RIGHT = 2  # 0010

BOTTOM = 4  # 0100

TOP = 8  # 1000

# Определение x_max, y_max и x_min, y_min для прямоугольника
# Так как диагональных точек достаточно, чтобы определить прямоугольник

x_max = 10.0

y_max = 8.0

x_min = 4.0

y_min = 4.0


# Функция для вычисления кода региона для точки (x, y)

def computeCode(x, y):
    if x < x_min:  # слева от прямоугольника
        return LEFT
    elif x > x_max:  # справа от прямоугольника
        return RIGHT
    if y < y_min:  # ниже прямоугольника
        return BOTTOM
    elif y > y_max:  # над прямоугольником
        return TOP
    return INSIDE

# Реализация алгоритма Коэна-Сазерленда

def cohen_sutherland_cut(x1, y1, x2, y2):
    # Вычислить коды регионов для P1, P2
    code1 = computeCode(x1, y1)
    code2 = computeCode(x2, y2)
    accept = False
    # y = kx + b
    k = (y1 - y2) / (x1 - x2)
    b = y1 - k * x1
    while True:
        # Если обе конечные точки лежат в прямоугольнике
        if code1 == 0 and code2 == 0:
            accept = True
            break
        # Если обе конечные точки находятся вне прямоугольника
        elif (code1 & code2) != 0:
            break
        # Некоторый сегмент лежит внутри прямоугольника
        else:
            x = 1.0
            y = 1.0
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2
            # Найти точку пересечения
            if code_out & TOP:
                # точка находится над прямоугольником клипа
                y = y_max
                x = (y - b) / k
            elif code_out & BOTTOM:
                # точка находится ниже прямоугольника клипа
                y = y_min
                x = (y - b) / k
            elif code_out & RIGHT:
                # точка находится справа от прямоугольника клипа
                x = x_max
                y = k * x + b
            elif code_out & LEFT:
                # точка находится слева от прямоугольника клипа
                x = x_min
                y = k * x + b
        # Теперь точка пересечения x, y найдена
        # Заменим точку за пределами отсечения прямоугольника
        # по точке пересечения
        if code_out == code1:
            x1 = x
            y1 = y
            code1 = computeCode(x1, y1)
        else:
            x2 = x
            y2 = y
            code2 = computeCode(x2, y2)
    if accept:
        print("Отрезок будет нарисован от %.2f,%.2f до %.2f,%.2f" % (x1, y1, x2, y2))
    else:
        print("Отрезок вне зоны видимости")


if __name__ == '__main__':
    # P11 = (5, 5), P12 = (7, 7)
    cohen_sutherland_cut(5, 5, 7, 7)

    # Второй отрезок
    # P21 = (7, 9), P22 = (11, 4)
    cohen_sutherland_cut(7, 9, 11, 4)
    
    # Третий линейный сегмент
    # P31 = (1, 5), P32 = (4, 1)
    cohen_sutherland_cut(1, 5, 4, 1)
