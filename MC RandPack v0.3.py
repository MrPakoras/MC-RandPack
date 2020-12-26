import os, random, mimetypes, time, colorama
from PIL import Image as i
from PIL import ImageFilter, ImageOps, ImageDraw
from pathlib import Path
from colorama import Fore
colorama.init(autoreset=True)

rootdir = './1.16.4/assets/minecraft/textures/'
texdirs = ['block/','colormap/','item/','map/','mob_effect/','models/armor/','painting/','particle/'] # Texture directories

dt = time.strftime('-%d%m%y-%H%M%S')

# Excluded files
exclfiles = []

def rgbswap(imagepath, filename): # Swaps RGB value with each other
	img = i.open(imagepath)
	pixels = img.load()

	# create array of all colours in image and colours they should be mapped to
	pcdict = {} # Pixel colour dictionary
	
	for x in range(img.size[0]):
		for y in range(img.size[1]):
			try:
				p = pixels[x,y]

				# if type(p) == 'int':
				# 	rgba = (0,0,0,0)
				if len(p) == 3:
					r,g,b = p
					alpha = 0
					rgba = (r,g,b,alpha)
				elif len(p) == 4:
					rgba = p
				else:
					continue

				if rgba not in pcdict:
					newrgba = random.sample(rgba,3)
					newrgba.append(0) # Add alpha value of 0
					newrgba = tuple(newrgba)
					pcdict[rgba] = newrgba
					pixels[x,y] = newrgba
				else:
					pixels[x,y] = pcdict[rgba]
			except TypeError:
				pass
	img = img.convert('RGBA')
	img.save(f'{newdir}{filename}', format='PNG')

for folder in texdirs:
	newdir = f'./MCRandPack{dt}/assets/minecraft/textures/{folder}' 
	Path(newdir).mkdir(parents=True, exist_ok=True) # Make new directory for edited textures

	for dirName, subdirList, fileList in os.walk(f'{rootdir}{folder}'):
		for fname in enumerate(fileList, start=1):
			filename = f'{rootdir}{folder}{fname[1]}'
			if filename[-4:] == '.png':
				if filename in exclfiles:
					print(f'{Fore.CYAN}>> {fname[0]} - {Fore.RED}{fname[1]}')
				else:
					rgbswap(filename, fname[1])
					print(f'{Fore.CYAN}>> {fname[0]} - {Fore.GREEN}{fname[1]}')