import os, time
from pathlib import Path


rootdir = './textures/block'

dt = time.strftime('-%d%m%y-%H%M%S')
newdir = f'./textures{dt}/block'
Path(newdir).mkdir(parents=True, exist_ok=True)