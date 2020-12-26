import os, random, mimetypes, time, colorama
from PIL import Image as i
from PIL import ImageFilter, ImageOps, ImageDraw
from pathlib import Path
from shutil import copyfile, copy2
from colorama import Fore
colorama.init(autoreset=True)

rootdir = './1.16.4/assets/minecraft/textures/'
texdirs = ['block/','entity/','item/','map/','mob_effect/','models/armor/','painting/','particle/'] # Texture directories

dt = time.strftime('-%d%m%y-%H%M%S')

# Excluded files
exclfiles = ['water_flow.png', 'water_overlay.png', 'water_still.png']
# Coloursed files
colfiles = ['lava_flow.png','lava_still.png','redstone_block.png']


def cfg(imagepath, filename): # Colourise from greyscale 
	img = i.open(imagepath)

	cb, cw = random.randint(0,125), random.randint(126,255)
	img = img.convert('L') # Convert to greyscale
	img = ImageOps.colorize(img, black=cb, white=cw) # colour map

	img.save(f'{newdir}{filename}', format='PNG')

def rgbswap(imagepath, filename): # Swaps RGB value with each other
	img = i.open(imagepath)
	pixels = img.load()

	# create array of all colours in image and colours they should be mapped to
	pcdict = {} # Pixel colour dictionary
	
	for x in range(img.size[0]):
		for y in range(img.size[1]):
			try:
				p = pixels[x,y]

				if len(p) == 4 and p[3] == 0:
					pass
				else:

					if len(p) == 3:
						r,g,b = p
						alpha = 255
						rgba = (r,g,b,alpha)
					elif len(p) == 4:
						rgba = p
					else:
						continue

					if rgba not in pcdict:
						newrgba = random.sample(rgba[:3],3)
						newrgba.append(255) # Add alpha value of 255
						newrgba = tuple(newrgba)
						pcdict[rgba] = newrgba
						pixels[x,y] = newrgba

					else:
						pixels[x,y] = pcdict[rgba]

			except TypeError:
				pass
	# img = img.convert('RGBA')
	img.save(f'{newdir}{filename}', format='PNG')

for folder in texdirs:
	newdir = f'./MCRandPack{dt}/assets/minecraft/textures/{folder}' 
	Path(newdir).mkdir(parents=True, exist_ok=True) # Make new directory for edited textures

	for dirName, subdirList, fileList in os.walk(f'{rootdir}{folder}'):
		for fname in enumerate(fileList, start=1):
			filename = f'{rootdir}{folder}{fname[1]}'
			if filename[-4:] == '.png':
				if fname[1] in exclfiles:
					print(f'{Fore.CYAN}>> {fname[0]} - {Fore.RED}{fname[1]}')
				elif fname[1] in colfiles:
					cfg(filename, fname[1])
				else:
					rgbswap(filename, fname[1])
					print(f'{Fore.CYAN}>> {fname[0]} - {Fore.GREEN}{fname[1]}')

copy2('./pack.mcmeta',f'./MCRandPack{dt}/') # Copies .mcmeta file to new directory