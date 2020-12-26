# Colourises all textures in MC to a random colour for cool texture pack effects
# Add function where if the name starts with the same word, its colourised with the same effect
# Eg. Dark oak door and dark oak boat will have the same colour effect

import os, random, mimetypes, time
from PIL import Image as i
from PIL import ImageFilter, ImageOps, ImageDraw


rootdir = 'H:/Python/MC RandPack/1.16.4'
subdir = '/assets/minecraft/textures/'
texdirs = ['block/','colormap/','item/','map/','mob_effect/','models/armor/','painting/','particle/'] # Texture directories

# rootdir = './textures/'
# subdir = ''
# texdirs = ['block/'] # Texture directories

# dt = time.strftime('-%d%m%y-%H%M%S')
# newrootdir = f'{rootdir[:-1]}{dt}/'
# os.mkdir(f'{newrootdir}')
# os.mkdir(f'{subdir}{texdirs[0]}')

# def cfg(image): # Colourise from greyscale
# 	sr = sr.convert('L') # Convert to greyscale
# 	sr = ImageOps.colorize(sr, black=cmblack, white=cmwhite) # colour map


def rgbswap(image): # Swaps RGB value with each other
	img = i.open(image)
	# img = img.convert('RGB')
	pixels = img.load()

	# create array of all colours in image and colours they should be mapped to
	pcdict = {} # Pixel colour dictionary
	
	for x in range(img.size[0]):
		for y in range(img.size[1]):
			p = pixels[x,y]

			if type(p) == 'int':
				rgba = (0,0,0,0)
			elif len(p) == 3:
				r,g,b = p
				alpha = 0
				rgba = (r,g,b,alpha)
			else:
				rgba = p

			if rgba not in pcdict:

				newrgba = random.sample(rgba,3)
				newrgba.append(0)
				newrgba = tuple(newrgba)
				pcdict[rgba] = newrgba
				pixels[x,y] = newrgba
			else:
				pixels[x,y] = pcdict[rgba]

			# print(rgb)
			# pixels[x,y] = tuple(random.sample(rgb,3)) # Turns all pixels into a random colour
			#pixels[x,y] = (rgb[2],rgb[0],rgb[1])

			#pix = img.getpixel((1,1))
			#print(pix)
	print(pcdict)

	img.save(image)




for folder in texdirs:
	for dirName, subdirList, fileList in os.walk(f'{rootdir}{subdir}{folder}'):
		for fname in enumerate(fileList, start=1):
			filename = f'{rootdir}{subdir}{folder}{fname[1]}'
			if filename[-4:] == '.png':
				rgbswap(filename)
				print(f'>> {fname[0]} - {fname[1]}')
