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
colfiles = ['lava_flow.png','lava_still.png','redstone_block.png','end_portal.png','bedrock.png','stone.png','nether_portal.png','fire_0.png','fire_1.png','soul_fire_0.png','soul_fire_1.png']


def cfg(imagepath, filename): # Colourise from greyscale 
	try:
		img = i.open(imagepath)

		cb, cw = tuple([random.randint(0,255) for loop in range(3)]), tuple([random.randint(0,255) for loop in range(3)])
		img = img.convert('L') # Convert to greyscale
		img = ImageOps.colorize(img, black=cb, white=cw) # colour map

		img.save(f'{newdir}{filename}', format='PNG')

	except FileNotFoundError:
		pass

def rgbswap(imagepath, filename): # Swaps RGB value with each other
	try:
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
							newrgba.append(rgba[3]) # Add alpha value
							newrgba = tuple(newrgba)
							pcdict[rgba] = newrgba
							pixels[x,y] = newrgba

						else:
							pixels[x,y] = pcdict[rgba]

				except TypeError:
					pass
		# img = img.convert('RGBA')
		img.save(f'{newsubdir}{filename}', format='PNG')

	except FileNotFoundError:
		pass

## Choosing Operation

while True:
	try:
		randmode = int(input(f'''Enter the number of the operation youd like to perform:
>> 1 - Radomise texture colours
>> 2 - Randomise textures
>> '''))
		break
	except:
		print(f'>> Error. Please try again.\n')

## Iterating through dirs
for folder in texdirs:
	newdir = f'./MCRandPack{dt}/assets/minecraft/textures/{folder}' 
	#Path(newdir).mkdir(parents=True, exist_ok=True) # Make new directory for edited textures

	for dirname, subdirlist, filelist in os.walk(f'{rootdir}{folder}'):
		newsubdir = f'{newdir}{dirname.replace(rootdir+folder,"")}'
		Path(newsubdir).mkdir(parents=True, exist_ok=True)

		allfiles = [] # All texture files

		for fname in enumerate(filelist, start=1):
			filename = f'{rootdir}{folder}{fname[1]}'
			fileext = os.path.splitext(filename)[1]
			allfiles.append(fname[1])

			# print(filename)
			# print(dirname)
			# print('\n')

			if randmode == 1:
				if fileext == '.png':
					if fname[1] in exclfiles:
						print(f'{Fore.CYAN}>> {fname[0]} - UNCHANGED: {Fore.RED}{fname[1]}')
					elif fname[1] in colfiles:
						cfg(filename, fname[1])
						print(f'{Fore.CYAN}>> {fname[0]} - {Fore.YELLOW}{fname[1]}')
					else:
						rgbswap(filename, fname[1])
						print(f'{Fore.CYAN}>> {fname[0]} - {Fore.GREEN}{fname[1]}')

			elif randmode == 2:
				allfiles.append(fname[1])
				# print(allfiles)

if randmode == 2:
	randfiles = random.sample(allfiles,len(allfiles))

	for dirname2, subdirlist2, filelist2 in os.walk(dirname):
		for fname in enumerate(filelist2, start=1):
			filename = f'{dirname2}{fname[1]}'
			fileext = os.path.splitext(filename)[1]

			nameswap = random.choice(randfiles)
			randfiles.remove(nameswap)
			os.rename(filename,f'{newsubdir}{nameswap}')


			# if fileext == '.mcmeta':
			# 	try:
			# 		copy2(f'{dirname}/{fname[1]}',f'{newsubdir}/{fname[1]}')
			# 		print(f'{Fore.CYAN}>> {fname[0]} - MOVED: {Fore.MAGENTA}{fname[1]}')
			# 	except FileNotFoundError:
			# 		print(f'{Fore.RED}>> FILE ERROR {newsubdir}/{fname[1]}')

copy2('./pack.mcmeta',f'./MCRandPack{dt}/') # Copies .mcmeta file to new directory