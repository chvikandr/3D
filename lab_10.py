from PIL import Image
import matplotlib.pyplot as plt
import random, time
from math import sin, cos, pi


class dot:
    def __init__(self, cordX: float, cordY: float, cordZ: float):
        self.x = cordX
        self.y = cordY
        self.z = cordZ

random.seed(time.time())

class figure:
    def __init__(self, dotA: dot, dotB: dot, dotC: dot, colour: tuple):
        self.dotA = dotA
        self.dotB = dotB
        self.dotC = dotC
        self.colour = colour

    def getZ(self, xi: int, yi: int):
        kA = (self.dotB.y - self.dotA.y) * (self.dotC.z - self.dotA.z) - (self.dotB.z - self.dotA.z) * (self.dotC.y - self.dotA.y)
        kB = (self.dotB.z - self.dotA.z) * (self.dotC.x - self.dotA.x) - (self.dotB.x - self.dotA.x) * (self.dotC.z - self.dotA.z)
        kC = (self.dotB.x - self.dotA.x) * (self.dotC.y - self.dotA.y) - (self.dotB.y - self.dotA.y) * (self.dotC.x - self.dotA.x)
        kD = -self.dotA.x * kA - self.dotA.y * kB - self.dotA.z * kC
        if kC != 0:
            return (-kA * xi - kB * yi - kD) / kC
        return -1

    def in_figure(self, xt: int, yt: int):
        abV = tuple([(self.dotB.x - self.dotA.x), (self.dotB.y - self.dotA.y)])
        bcV = tuple([(self.dotC.x - self.dotB.x), (self.dotC.y - self.dotB.y)])
        caV = tuple([(self.dotA.x - self.dotC.x), (self.dotA.y - self.dotC.y)])
        Nab = tuple([abV[1], -abV[0]])
        Nbc = tuple([bcV[1], -bcV[0]])
        Nca = tuple([caV[1], -caV[0]])
        atV = tuple([xt - self.dotA.x, yt - self.dotA.y])
        btV = tuple([xt - self.dotB.x, yt - self.dotB.y])
        ctV = tuple([xt - self.dotC.x, yt - self.dotC.y])
        if (((Nab[0] * atV[0] + Nab[1] * atV[1] >= 0) and (Nbc[0] * btV[0] + Nbc[1] * btV[1] >= 0) and  (Nca[0] * ctV[0] + Nca[1] * ctV[1] >= 0) or
                ((Nab[0] * atV[0] + Nab[1] * atV[1] < 0) and (Nbc[0] * btV[0] + Nbc[1] * btV[1] < 0) and (Nca[0] * ctV[0] + Nca[1] * ctV[1] < 0)))):
            return True
        return False


dots = []
figures = []
xmin = 100
xmax = 0
ymin = 100
ymax = 0
with open(input("Введите полный путь к файлу: ")) as file:
    info = file.read().split('\n')
    for line in info:
        if line.find("v") == 0:
            _, *line = line.split()
            line = list(float(dot) for dot in line)
            D = dot(line[0], line[1], line[2])
            dots.append(D)
        elif line.find("f") == 0:
            _, *line = line.split()
            figures.append(list(int(fig) for fig in line))
with Image.new("RGB", (100, 100)) as image:
    for x in range(0, image.width):
        for y in range(0, image.height):
            if x % 2 == y % 2:
                image.putpixel((x, y), (54, 54, 54))
    for i in range(len(dots)):
        list_ = [dot[i].x, dot[i].y, dot[i].z, 1]
        scale_matrix = [[40, 0, 0, 0], [0, 40, 0, 0], [0, 0, 40, 0], [0, 0, 0, 1]]
        new_vector = [0] * len(list_)
        for i in range(len(scale_matrix)):
            for j in range(len(list_)):
                new_vector[i] += scale_matrix[i][j] * list_[j]
        dots[i] = dot(new_vector[0], new_vector[1], new_vector[2])
        angle = (35 * pi) / 180
        rotate_Z = [[cos(angle), -sin(angle), 0, 0], [sin(angle), cos(angle), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        new_vector = [0] * len(list_)
        for i in range(len(rotate_Z)):
            for j in range(len(list_)):
                new_vector[i] += rotate_Z[i][j] * list_[j]
        dots[i] = dot(new_vector[0], new_vector[1], new_vector[2])
        angle = (55 * pi) / 180
        rotate_X = [[1, 0, 0, 0], [0, cos(angle), -sin(angle), 0], [0, sin(angle), cos(angle), 0], [0, 0, 0, 1]]
        new_vector = [0] * len(list_)
        for i in range(len(rotate_X)):
            for j in range(len(list_)):
                new_vector[i] += rotate_X[i][j] * list_[j]
        dots[i] = dot(new_vector[0], new_vector[1], new_vector[2])
        move_matrix = [[1, 0, 0, 50], [0, 1, 0, 50], [0, 0, 1, 0], [0, 0, 0, 1]]
        new_vector = [0] * len(list_)
        for i in range(len(move_matrix)):
            for j in range(len(list_)):
                new_vector[i] += move_matrix[i][j] * list_[j]
        dots[i] = dot(new_vector[0], new_vector[1], new_vector[2])
        xmin = int(min(xmin, dots[i].x))
        xmax = int(max(xmax, dots[i].x))
        ymin = int(min(ymin, dots[i].y))
        ymax = int(max(ymax, dots[i].y))
    for i in range(len(figures)):
        figures[i] = figure(dots[figures[i][0] - 1], dots[figures[i][1] - 1], dots[figures[i][2] - 1], tuple([random.randrange(255 + 1), random.randrange(255 + 1), random.randrange(255 + 1)]))
        print(str(i + 1) + " = " + str(figures[i].colour))
    for X in range(xmin, xmax + 1):
        for Y in range(ymin, ymax + 1):
            current_fig = None
            current_z = None
            for i in range(len(figures)):
                if figures[i].in_figure(X, Y):
                    fig_z = figures[i].getZ(X, Y)
                    if (current_fig is None) or (fig_z >= current_z):
                        current_fig = figures[i]
                        current_z = fig_z
            if current_fig is not None:
                image.putpixel((X, Y), current_fig.colour)
    plt.imshow(image)
    plt.show()