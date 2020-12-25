# Colourises all textures in MC to a random colour for cool texture pack effects
# Add function where if the name starts with the same word, its colourised with the same effect
# Eg. Dark oak door and dark oak boat will have the same colour effect

import os, random
from PIL import Image as i
from PIL import ImageFilter, ImageOps, ImageDraw


# def cfg(image): # Colourise from greyscale
# 	sr = sr.convert('L') # Convert to greyscale
# 	sr = ImageOps.colorize(sr, black=cmblack, white=cmwhite) # colour map


def rgbswap(image): # Swaps RGB value with each other
	img = i.open(image)
	img = img.convert('RGB')
	pixels = img.load()

	for x in range(img.size[0]):
		for y in range(img.size[1]):
			rgb = pixels[x,y]
			print(rgb)
			pixels[x,y] = tuple(random.sample(rgb,3))

			#pix = img.getpixel((1,1))
			#print(pix)

	img.save(image)



# rootDir = 'H:/Python/MC RandPack/1.16.4/assets/minecraft/textures/'
# texDirs = ['block','colormap','item'] # Texture directories

rootDir = './textures/'
texDirs = ['block/'] # Texture directories

for folder in texDirs:
	for dirName, subdirList, fileList in os.walk(f'{rootDir}{folder}'):
		for fname in enumerate(fileList, start=1):
			rgbswap(f'{rootDir}{folder}{fname[1]}')
			print(f'>> {fname[0]} - {fname[1]}')
