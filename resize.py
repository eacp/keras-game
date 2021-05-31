from PIL import Image
from pathlib import Path
import sys
import os


# Get the folder
folder = sys.argv[1]

p = Path(folder)

new_folder = os.path.join("pre", p)

for i in p.iterdir():
	img = Image.open(i)

	img.thumbnail((100,100))

	print(os.path.join(new_folder, i.name))

	img.save(os.path.join(new_folder, i.name))