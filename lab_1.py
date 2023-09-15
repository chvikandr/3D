from PIL import Image
#import matplotlib.pyplot as plt
image = Image.new('RGB', (100,100))
print("Введите значение x0")
x0=int(input())
print("Введите значение y0")
y0=int(input())
print("Введите значение x1")
x1=int(input())
print("Введите значение y1")
y1=int(input())
if x0>x1:
    a=x0
    x0=x1
    x1=a
    b=y0
    y0=y1
    y1=b
k=abs((y1-y0)/(x1-x0))
e=0
if k<=1:
    y=y0
    if y1>=y0:
        for x in range(x0, (x1+1)):
            if e>(x1-x0):
               y+=1
               e-=2*(x1-x0)
            e += 2*(y1 - y0)
            image.putpixel((x,y), (0, 0, 255))
    else:
        for x in range(x0, (x1+1)):
            if e>(x1-x0):
               y-=1
               e-=2*(x1-x0)
            e += 2*(y0 - y1)
            image.putpixel((x,y), (0, 0, 255))
else:
    x=x0
    if y1>=y0:
        for y in range(y0, (y1+1)):
            if e>(y1-y0):
               x+=1
               e+=2*(y1-y0)
            e += 2*(x1 - x0)
            image.putpixel((x,y), (0, 0, 255))
    else:
        for y in range(y0, (y1+1), -1):
            if e>(y0-y1):
               x+=1
               e-=2*(y0-y1)
            e += 2*(x1-x0)
            image.putpixel((x,y), (0, 0, 255))
image.save("a.png")
#plt.imshow(image)
#plt.show()