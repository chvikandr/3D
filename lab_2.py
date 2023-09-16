from PIL import Image
image = Image.new('RGB', (100,100))
print('Введите радиус окружности')
r=int(input())
f0=-2*r+1
x = -1*r
ser=int((r//2**0.5)+1)
for y in range(ser):
    image.putpixel((x, y), (0, 0, 255))
    image.putpixel((-1*y-1, -1*x-1), (0, 0, 255))
    if f0<0:
        f0+=4*y+6
    else:
        f0+=4*x+4*y+10
        x+=1
image.save("a.png")