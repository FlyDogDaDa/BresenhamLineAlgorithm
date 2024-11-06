import lampsim

lamp = lampsim.LampScreen(64, 64)

x0, y0, x1, y1 = 25, 48, 0, 0
vtcal = abs(y1 - y0) > abs(x1 - x0)
if vtcal:
    x0, y0 = y0, x0
    x1, y1 = y1, x1
if x0 > y1:
    x0, x1 = x1, x0
    y0, y1 = y1, y0
deltax = x1 - x0
deltay = abs(y1 - y0)
error = deltax / 2
y = y0
if y0 < y1:
    ystep = 1
else:
    ystep = -1

for x in range(x0, x1):
    if vtcal:
        lamp.draw_pixel(y, x)
    else:
        lamp.draw_pixel(x, y)
    error -= deltay
    if error < 0:
        y += ystep
        error += deltax
lamp.display()
