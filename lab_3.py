import math

from PIL import Image

def line (x0, y0, x1, y1):
    if x0 > x1:
        a = x0
        x0 = x1
        x1 = a
        b = y0
        y0 = y1
        y1 = b
    if x1 == x0:
        if y0>y1:
            b = y0
            y0 = y1
            y1 = b
        for i in range(y0, y1):
            image.putpixel((x1, i), (0, 0, 255))
    else:
        k = abs((y1 - y0) / (x1 - x0))
        e = 0
        if k <= 1:
            y = y0
            if y1 >= y0:
                for x in range(x0, (x1 + 1)):
                    if e > (x1 - x0):
                        y += 1
                        e -= 2 * (x1 - x0)
                    e += 2 * (y1 - y0)
                    image.putpixel((x, y), (0, 0, 255))
            else:
                for x in range(x0, (x1 + 1)):
                    if e > (x1 - x0):
                        y -= 1
                        e -= 2 * (x1 - x0)
                    e += 2 * (y0 - y1)
                    image.putpixel((x, y), (0, 0, 255))
        else:
            x = x0
            if y1 >= y0:
                for y in range(y0, (y1 + 1)):
                    if e > (y1 - y0):
                        x += 1
                        e += 2 * (y1 - y0)
                    e += 2 * (x1 - x0)
                    image.putpixel((x, y), (0, 0, 255))
            else:
                for y in range(y0, (y1 + 1), -1):
                    if e > (y0 - y1):
                        x += 1
                        e -= 2 * (y0 - y1)
                    e += 2 * (x1 - x0)
                    image.putpixel((x, y), (0, 0, 255))


image = Image.new('RGB', (100,100))
print("Введите количество вершин выпуклого многоугольника")
n=int(input())
print("Введите последовательно вершины многоугольника.Вершины вводятся по часовой стрелке.Координаты Х и Y через enter")
verx=[None]*n
very=[None]*n
for i in range(0, n):
    print("Введите вершину")
    verx[i]=int(input())
    very[i]=int(input())
print("Вевдите отрезок, который должен отсечь многоугольник")
print("Введите координаты первой точки")
xa=int(input())
ya=int(input())
print("Введите координаты второй точки")
xb=int(input())
yb=int(input())
kolmin = 0
tmin = []
tmax = []
for i in range(0, n):
    if i == n-1:
        x0 = verx[i]
        y0 = very[i]
        x1 = verx[0]
        y1 = very[0]
    else:
        x0 = verx[i]
        y0 = very[i]
        x1 = verx[i+1]
        y1 = very[i+1]
    if (x0 == x1) and (xa == xb):
        pass
    elif (y0 == y1) and (ya == yb):
        pass
    elif (x0 == x1):
        if y1 > y0:
            xn = -1
        else:
            xn = 1
        yn = 0
        t = (x0 - xa) / (xb - xa)
        if xn * (xb - xa) + yn * (yb - ya) > 0:
            tmax.append(t)
        else:
            tmin.append(t)
            kolmin += 1
    elif (y0 == y1):
        if x1 > x0:
            yn = 1
        else:
            yn = -1
        xn = 0
        t = (y0 - ya) / (yb - ya)
        if xn * (xb - xa) + yn * (yb - ya) > 0:
            tmax.append(t)
        else:
            tmin.append(t)
            kolmin += 1
    else:
        if ((x1 > x0) and (y1 > y0)) or ((x1 < x0) and (y1 < y0)):
            xn = x0 - x1
            yn = y1 - y0
        elif ((x1 > x0) and (y1 < y0)) or ((x1 < x0) and (y1 > y0)):
            xn = x1 - x0
            yn = y0 - y1
        t = (xn * (x0 - xa) + yn * (y0 - ya)) / (xn * (xb - xa) + yn * (yb - ya))
        if xn * (xb - xa) + yn * (yb - ya) > 0:
            tmax.append(t)
        else:
            tmin.append(t)
            kolmin += 1
    line(x0, y0, x1, y1)
tmin.sort()
tmax.sort()
if xa<xb:
    line (xa, ya, xa+math.ceil((xb-xa)*tmin[kolmin-1]), ya+math.ceil((yb-ya)*tmin[kolmin-1]))
    line (xa + math.ceil(xb*tmax[0]), math.ceil(yb*tmax[0]), xb, yb)
else:
    line(xb, yb, math.ceil(xb * tmin[kolmin-1]), math.ceil(yb * tmin[kolmin-1]))
    line(math.ceil(xa * tmax[0]), math.ceil(ya * tmax[0]), xa, ya)
image.save("a.png")