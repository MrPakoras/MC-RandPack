from PIL import Image as i
import os, re
from pathlib import Path

# f = 'hello.png'
# print(f[-4:])


# a = {'one':1,'two':2,'three':3}

# b = ['three','four']

# for x in b:
# 	if x not in a:
# 		a[x] = 4
# 		print(a[x])
# 	else:
# 		print(a[x])


# img = i.open('./Untitled.png')
# pixels = img.load()
# p = pixels[1,1]
# if len(p) == 3:
# 	r,g,b = p
# 	a = 1
# else:
# 	r,g,b,a = p
# print(r,g,b,a)
# print(img.getpixel((1,1)))


# a = [1,2,3,4]
# print(tuple(lambda a: a.append(5)))

# Path('./my/directory').mkdir(parents=True, exist_ok=True)

# addr = 'H:/Python/MC RandPack/1.16.4.png'

# print(re.findall(r'\/.*$',addr)[-1])


img = i.open(imagepath)
pixels = img.load()
