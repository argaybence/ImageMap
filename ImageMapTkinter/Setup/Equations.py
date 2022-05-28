def two_point_equation(xy1: tuple, xy2: tuple, y):
    x1, y1 = xy1
    x2, y2 = xy2
    # (x2-x1)(y-y1) = (y2-y1)(x-x1)

    # ((x2-x1)*(y-y1) + (-(y2-y1) * (-x1))) / (y2 - y1)

    return round(((x2 - x1) * (y - y1) + (-(y2 - y1) * (-x1))) / (y2 - y1))


def quadratic_equation(b, c):
    #  (a) always equals to 1, because of (x - mid_x)^2 -> x^2 -> a = 1
    a = 1
    d = (b ** 2 - (4 * a * c))
    if d < 0:
        return None

    d = d ** (1/2)
    return round((b - d) / 2), round((b + d) / 2)


def circle_equation(mid_x, mid_y, y, r):
    #  (x - mid_x)^2 + (y - mid_y)^2 = r^2

    z = ((y - mid_y) ** 2) - (r ** 2)
    c = (mid_x ** 2) + z

    return quadratic_equation(mid_x, c)
