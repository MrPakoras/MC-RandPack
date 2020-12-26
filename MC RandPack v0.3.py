import os, random, mimetypes, time
from PIL import Image as i
from PIL import ImageFilter, ImageOps, ImageDraw
from pathlib import Path

rootdir = './1.16.4/assets/minecraft/textures/'
texdirs = ['block/','colormap/','item/','map/','mob_effect/','models/armor/','painting/','particle/'] # Texture directories

dt = time.strftime('-%d%m%y-%H%M%S')

def rgbswap(imagepath, filename): # Swaps RGB value with each other
	img = i.open(imagepath)
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
	img.save(f'{newdir}{filename}')

for folder in texdirs:
	newdir = f'./MCRandPack{dt}/assets/minecraft/textures/{folder}' 
	Path(newdir).mkdir(parents=True, exist_ok=True) # Make new directory for edited textures

	for dirName, subdirList, fileList in os.walk(f'{rootdir}{folder}'):
		for fname in enumerate(fileList, start=1):
			filename = f'{rootdir}{folder}{fname[1]}'
			if filename[-4:] == '.png':
				rgbswap(filename, fname[1])
				print(f'>> {fname[0]} - {fname[1]}')