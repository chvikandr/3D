from PIL import Image, ImageOps
import matplotlib.pyplot as plt


def on_click(event):
    global cid, dot
    if event.button == 3:
        dot = [int(event.xdata), int(event.ydata)]
        plt.disconnect(cid)


image = Image.open("a.png")
cid = plt.connect("button_press_event", on_click)
plt.imshow(image)
plt.show()
dot = [0] * 2
s = input("введите цвет в формате RGB черех пробелы:").split()
filler = tuple(int(val) for val in s)
if len(filler) != 3:
    print("Неверное число параметров")
s_ = input("введите цвет границы в формате RGB через пробелы: ").split()
edge = tuple(int(val) for val in s_)
if len(edge) != 3:
    print("Неверное число параметров")
global image
stack = []
stack.append((dot[0], dot[1]))
while len(stack) != 0:
    pixels = list(image.getdata())
    current = stack.pop(0)
    Xn = current[0]
    Yn = current[1]
    if (Xn < 0 or Xn > image.width) or (Yn < 0 or Yn > image.height):
        continue
    elif pixels[image.width * Yn + Xn] == filler:
        continue
    elif pixels[image.width * Yn + Xn] == edge:
        continue
    image.putpixel((Xn, Yn), filler)
    stack.append((Xn + 1, Yn))
    stack.append((Xn, Yn + 1))
    stack.append((Xn - 1, Yn))
    stack.append((Xn, Yn - 1))
plt.imshow(image)
plt.show()
image.save("b.png")
image.close()
