"""

Perform basic data augmentation on the training set

This file is meant to run on one folder only, so it is required to run
once per class

"""

from PIL import Image, ImageOps
from pathlib import Path
import sys
import os

# Get the folder
folder = sys.argv[1]

p = Path(folder)


# First round of augmentation: mirror
for f in p.iterdir():
    img = Image.open(f)

    # Mirror
    mirrored = ImageOps.mirror(img)

    # Get new name
    new_name = "mirrored-"+f.name

    mirrored.save(os.path.join(p, new_name))

# Seccond round of augmentation: flip
for f in p.iterdir():
    img = Image.open(f)

    # Mirror
    fliped = ImageOps.flip(img)

    # Get new name
    new_name = "fliped-"+f.name

    fliped.save(os.path.join(p, new_name))