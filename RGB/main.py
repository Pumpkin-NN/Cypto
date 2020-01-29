from pre_processing import pre_processing
from PIL import Image
import os

'''
Main Function
'''
if __name__ == "__main__":
    
    # Get the orignal image path
    root_dir = os.path.dirname(os.getcwd())
    im_path = os.path.join(root_dir, 'Reversible_Data_Hiding/misc/4.2.07.tiff')
    
    # Save the original image
    original_img = Image.open(im_path)
    original_img.save("original_img.png")
    
    # Pre-processing image
    pre_processing(im_path)
    
    