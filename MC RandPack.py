# Colourises all textures in MC to a random colour for cool texture pack effects

import os
from PIL import Image as i
from PIL import ImageFilter, ImageOps, ImageDraw

texfolds = ['blocks'] # Texture folders

flist = []
rootDir = './videos'
nth = 1
for folder in texfolds:
	for dirName, subdirList, fileList in os.walk(f'{rootDir}/{folder}'):
	    for fname in fileList:
	        print('>> '+str(nth)+' - '+fname)
	        flist.append(fname)
	        nth += 1

sr = sr.convert('L') # Convert to greyscale
sr = ImageOps.colorize(sr, black=cmblack, white=cmwhite) # colour map