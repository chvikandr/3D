from PIL import Image
import matplotlib.pyplot as plt


with Image.open("a.png") as image:
    new_image = Image.new('RGB', (image.width, image.height))
    pixel = list(image.getdata())
    for x in range(0, image.width - 1):
        for y in range(0, image.height - 1):
            rgb = [0] * 3
            for i in range(3):
                for X in range(x - 1, x + 1 + 1):
                    for Y in range(y - 1, y + 1 + 1):
                        if X < 0 or Y < 0 or X > image.width or Y > image.height:
                            continue
                        k = 1
                        if X == x and Y == y:
                            k *= 4
                        elif X == x or Y == y:
                            k *= 2
                        rgb[i] += k * pixel[image.width * Y + X][i]
                rgb[i] = int(rgb[i] / 16)
                if rgb[i] > 255:
                    rgb[i] = 255
            new_color = tuple([int(sum(rgb) / 3)] * 3)
            new_image.putpixel((x, y), new_color)
    new_image.save("b.png")
    plt.imshow(image)
    plt.show()
    plt.imshow(new_image)
    plt.show()
