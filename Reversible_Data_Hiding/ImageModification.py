from PIL import Image
import numpy as np
# Convert decimal to binary
def decimalToBinary(dec):  
    return bin(dec).replace("0b", "").zfill(8)

# Convert binary to decimal
def binaryToDecimal(bi): 
    return int(bi,2)

def image_modification(image_path):
    
    # Load pixels from image
    im = Image.open(image_path)
    px = im.load()
    
    # Get the height and width from the original image
    height = im.height
    width = im.width
    
    # Pixel Modification
    modify_pixels = []
    for i in range(0,height):
        for j in range(0,width):
            bi = decimalToBinary(px[i,j])
            MSB = bi[:4]
            LSB = bi[4:]
            
            modify_pixel = LSB + MSB
            modify_pixel = binaryToDecimal(modify_pixel)
            modify_pixels.append(modify_pixel)
            
    # Reshape to 2D array
    modify_pixels = np.array(modify_pixels)
    modify_pixels = modify_pixels.reshape(height, width)
    
    # Create the encypted image
    img = Image.fromarray(np.uint8(modify_pixels * 255) , 'L')
    size = width, height
    img = img.resize(size)
    img = img.rotate(-90)
    
    # Return the modified image
    return img