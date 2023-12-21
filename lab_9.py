from PIL import Image
import matplotlib.pyplot as plt
from math import sin, cos, pi


def line(image, x0, y0, x1, y1):
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


dots = []
figures = []
with open(input("Введите полный путь к файлу: ")) as file:
    info = file.read().split('\n')
    for line in info:
        if line.find("v") == 0:
            _, *line = line.split()
            dots.append(list(float(dot) for dot in line))
        elif line.find("f") == 0:
            _, *line = line.split()
            figures.append(list(int(fig) for fig in line))
with Image.new("RGB", (26, 26)) as image:
    for x in range(0, image.width):
        for y in range(0, image.height):
            if(x%2 == y%2):
                image.putpixel((x, y), (54, 54, 54))

    for i in range(len(dots)):
        list_ = [dots[0], dots[1], dots[2], 1]
        scale_matrix = [[15, 0, 0, 0], [0, 15, 0, 0], [0, 0, 15, 0], [0, 0, 0, 1]]
        new_vector = [0] * len(list_)
        for i in range(len(scale_matrix)):
            for j in range(len(list_)):
                new_vector[i] += scale_matrix[i][j] * list_[j]
        dots[i] = new_vector[:-1]
        angle = (35 * pi) / 180
        rotate_Z = [[cos(angle), -sin(angle), 0, 0], [sin(angle), cos(angle), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        new_vector = [0] * len(list_)
        for i in range(len(rotate_Z)):
            for j in range(len(list_)):
                new_vector[i] += rotate_Z[i][j] * list_[j]
        dots[i] = new_vector[:-1]
        angle = (55 * pi) / 180
        rotate_X = [[1, 0, 0, 0], [0, cos(angle), -sin(angle), 0], [0, sin(angle), cos(angle), 0], [0, 0, 0, 1]]
        new_vector = [0] * len(list_)
        for i in range(len(rotate_X)):
            for j in range(len(list_)):
                new_vector[i] += rotate_X[i][j] * list_[j]
        dots[i] = new_vector[:-1]
        move_matrix = [[1, 0, 0, 13], [0, 1, 0, 13], [0, 0, 1, 0], [0, 0, 0, 1]]
        new_vector = [0] * len(list_)
        for i in range(len(move_matrix)):
            for j in range(len(list_)):
                new_vector[i] += move_matrix[i][j] * list_[j]
        dots[i] = new_vector[:-1]
    for i in range(len(figures)):
        fig = figures[i]
        xa, ya, za = dots[fig[0] - 1][0], dots[fig[0] - 1][1], dots[fig[0] - 1][2]
        xb, yb, zb = dots[fig[1] - 1][0], dots[fig[1] - 1][1], dots[fig[1] - 1][2]
        xc, yc, zc = dots[fig[2] - 1][0], dots[fig[2] - 1][1], dots[fig[2] - 1][2]
        C = (xb - xa) * (yc - ya) - (yb - ya) * (xc - xa)
        if not C < 0:
            for j in range(-1, len(fig)-1):
                line(image, int(dots[fig[j]-1][0]), int(dots[fig[j]-1][1]), int(dots[fig[j+1]-1][0]), int(dots[fig[j+1]-1][1]))
    plt.imshow(image)
    plt.show()