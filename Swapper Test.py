import os, random, mimetypes, time, colorama
from pathlib import Path
from shutil import copyfile, copy2

rootdir = './1.16.4/assets/minecraft/textures/'
texdirs = ['block/','entity/','item/','map/','mob_effect/','models/armor/','painting/','particle/'] # Texture directories

dt = time.strftime('-%d%m%y-%H%M%S')

# Excluded files
exclfiles = ['water_flow.png', 'water_overlay.png', 'water_still.png']
# Coloursed files
colfiles = ['lava_flow.png','lava_still.png','redstone_block.png','end_portal.png','bedrock.png','stone.png','nether_portal.png','fire_0.png','fire_1.png','soul_fire_0.png','soul_fire_1.png']

for folder in texdirs:
	newdir = f'./MCRandPack{dt}/assets/minecraft/textures/{folder}' 
	#Path(newdir).mkdir(parents=True, exist_ok=True) # Make new directory for edited textures

	for dirname, subdirlist, filelist in os.walk(f'{rootdir}{folder}'):
		newsubdir = f'{newdir}{dirname.replace(rootdir+folder,"")}'
		Path(newsubdir).mkdir(parents=True, exist_ok=True)
		# print(dirname)

		allfiles = [] # All texture files

		for fname in enumerate(filelist, start=1):
			filename = f'{rootdir}{folder}{fname[1]}'
			filename2 = f'{dirname}{fname[1]}'			
			fileext = os.path.splitext(filename)[1]

			allfiles.append(fname[1])

		print(allfiles)

print(f'\n\n\n>> {filename}')
print(f'>> {filename2}')