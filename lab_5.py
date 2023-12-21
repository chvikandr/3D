from PIL import Image
import matplotlib.pyplot as plt
from math import sqrt


with Image.open("a.png") as image:
    new_image = Image.new('RGB', (image.width, image.height))
    pixel = list(image.getdata())
    for x in range(image.width - 1):
        for y in range(image.height - 1):
            Sx = [0] * 3
            Sy = [0] * 3
            rgb = [0] * 3
            for i in range(3):
                if x == 0 and y == 0:
                    Sx[i] += pixel[image.width * (y + 1) + x + 1][i] + 2 * pixel[image.width * y + x + 1][i]
                    Sy[i] -= 2 * pixel[image.width * (y + 1) + x][i] + pixel[image.width * (y + 1) + x + 1][i]
                elif x == 0 and y == image.height:
                    Sx[i] += 2 * pixel[image.width * y + x + 1][i] + pixel[image.width * (y - 1) + x + 1][i]
                    Sy[i] += 2 * pixel[image.width * (y - 1) + x][i] + pixel[image.width * (y - 1) + x + 1][i]
                elif x == image.width and y == 0:
                    Sx[i] -= pixel[image.width * (y + 1) + x - 1][i] + 2 * pixel[image.width * y + x - 1][i]
                    Sy[i] -= pixel[image.width * (y + 1) + x - 1][i] + 2 * pixel[image.width * (y + 1) + x][i]
                elif x == image.width and y == image.height:
                    Sx[i] -= 2 * pixel[image.width * y + x - 1][i] + pixel[image.width * (y - 1) + x - 1][i]
                    Sy[i] += pixel[image.width * (y - 1) + x - 1][i] + 2 * pixel[image.width * (y - 1) + x][i]
                else:
                    for Y in range(y - 1, y + 2):
                        if Y < 0 or Y >= image.height:
                            continue
                        if Y == y:
                            k = 2
                        else:
                            k = 1
                        Sx[i] += k * (pixel[image.width * Y + x + 1][i] - pixel[image.width * Y + x - 1][i])
                    for X in range(x - 1, x + 2):
                        if X < 0 or X >= image.width:
                            continue
                        if X == x:
                            k = 2
                        else:
                            k = 1
                        Sy[i] += k * (pixel[image.width * (y - 1) + X][i] - pixel[image.width * (y + 1) + X][i])
            for i in range(3):
                rgb[i] += int(sqrt(Sx[i] * Sx[i] + Sy[i] * Sy[i]))
                rgb[i] = 255 if (rgb[i] >= 255) else rgb[i]
            new_color = tuple([int(sum(rgb) / 3)] * 3)
            new_image.putpixel((x, y), new_color)
    new_image.save("b.png")
    plt.imshow(image)
    plt.show()
    plt.imshow(new_image)
    plt.show()
