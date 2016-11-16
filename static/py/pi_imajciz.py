# -*- coding: utf-8 -*-

from PIL import Image
from random import seed, randint

width, height = 2000, 2000
background = 0

seed(42)
d = dict(((x, y), randint(0, 255)) for x in range(width) for y in range(height))

algorithm = 1
print('Algorithm', algorithm)

if algorithm == 0:
    im = Image.new('L', (width, height))
    for i in d:
        im.putpixel(i, d[i])
elif algorithm == 1:
    buff = bytearray((background for _ in xrange(width * height)))
    for (x,y), v in d.items():
        buff[y*width + x] = v
    im = Image.frombytes('L', (width,height), str(buff))
elif algorithm == 2:
    data = [background] * width * height
    for i in d:
        x, y = i
        data[x + y * width] = d[i]
    im = Image.new('L', (width, height))
    im.putdata(data)

#im.show()

fname = 'qrand%d.png' % algorithm
im.save(fname)
print(fname, 'saved')
