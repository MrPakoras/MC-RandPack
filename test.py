from PIL import Image as i
import os, re, random
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


# img = i.open('./glass.png')
# pixels = img.load()

# for x in range(img.size[0]):
# 	for y in range(img.size[1]):
# 		print(f'{x},{y} - {pixels[x,y]}')

# a = [r'water.*']
# b = 'water-01.png'

# if b in a:
# 	print('Yea')
# else:
# 	print('Na')

# def rgbswap(imagepath): # Swaps RGB value with each other
# 	img = i.open(imagepath)
# 	pixels = img.load()
# 	pcdict = {} # Pixel colour dictionary

# 	for x in range(img.size[0]):
# 		for y in range(img.size[1]):
# 			try:
# 				p = pixels[x,y]

# 				if len(p) == 4 and p[3] == 0:
# 					print(f'>> Passed - {p}')
# 					pass

# 				else:

# 					if len(p) == 3:
# 						r,g,b = p
# 						alpha = 255
# 						rgba = (r,g,b,alpha)
# 					elif len(p) == 4:
# 						rgba = p
# 					else:
# 						continue

# 					if rgba not in pcdict:
# 						newrgba = random.sample(rgba[:3],3)
# 						newrgba.append(rgba[3]) # Add alpha value of 1
# 						newrgba = tuple(newrgba)
# 						pcdict[rgba] = newrgba
# 						pixels[x,y] = newrgba
# 						print(f'>> {rgba} to {newrgba}')
# 					else:
# 						pixels[x,y] = pcdict[rgba]
# 						print(f'>> {rgba} to {newrgba}')

# 			except TypeError:
# 				print('>> TypeError')
# 	# img = img.convert('RGBA')
# 	img.save(imagepath)

# rgbswap('./glass.png')


# a = (0,1,2,3)
# print(random.sample(a[:3],3))


# rootdir = './1.16.4/assets/minecraft/textures/' 

# for dirname, subdirlist, filelist in os.walk(rootdir):
# 	print(dirname.replace(rootdir,''))
# 	# [print(x) for x in enumerate(subdirList)]


a = ['one','two','three','four','five']

# print(random.sample(a,len(a)))

# [print(random.sample(a,1)[0]) for loop in range(5)]

for loop in range(len(a)):
	b = random.choice(a)
	a.remove(b)
	print(b)