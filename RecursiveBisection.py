import lampsim


# def pop_lower_bit(x: int) -> int:
#     if 1 >= x >= -1:
#         return 0
#     return int(bin(x)[2:-1], base=2)


def cut(lamp: lampsim.LampScreen, x0, y0, x1, y1):
    if x0 >> 1 == x1 >> 1 and y0 >> 1 == y1 >> 1:
        lamp.draw_pixel(x0, y0)
        lamp.draw_pixel(x1, y1)
        return

    half_x, rx = divmod(x0 + x1, 2)  # 中點, remainder
    half_y, ry = divmod(y0 + y1, 2)  # 中點, remainder

    un_x = x0 > x1
    un_y = y0 > y1

    hx0 = half_x + (rx and un_x)
    hy0 = half_y + (ry and un_y)

    hx1 = half_x + (rx and (not un_x))
    hy1 = half_y + (ry and (not un_y))

    cut(lamp, x0, y0, hx0, hy0)
    cut(lamp, hx1, hy1, x1, y1)


lamp = lampsim.LampScreen(10, 10)

x0, y0, x1, y1 = (4, 10, 0, 0)
cut(lamp, x0, y0, x1, y1)
lamp.display()
