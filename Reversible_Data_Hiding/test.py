from PIL import Image

import os

root_dir = os.path.dirname(os.getcwd())
im_path = os.path.join(root_dir, 'Reversible_Data_Hiding/misc/4.1.07.tiff')

im = Image.open(im_path) 

px = im.load()

for i, j in zip(range(0,256), range(0,256)):
    print (px[i, j])
    

