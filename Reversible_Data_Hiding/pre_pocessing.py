from PIL import Image
import os

def pre_processing(image_path):
    
    # Load pixels from image
    im = Image.open(image_path) 
    px = im.load()

    # Pre-Processing Algorithm
    processed_pxs = []
    for i in range(0,256):
        for j in range(0,256):
            inv = (px[i, j] + 128) % 256
            if i == 0 or j == 0:
                continue
            else:
                pred = ( px[i-1, j] + px[i, j-1] ) // 2
            
            dif = abs(pred - px[i, j])
            dif_inv = abs(pred - inv)
            
            if dif >= dif_inv:
                if px[i, j] > 128:
                    processed_px = pred - 63
                    processed_pxs.append(processed_px)
                else:
                    processed_px = pred + 63
                    processed_pxs.append(processed_px)
            else:
                processed_px = px[i, j]
                processed_pxs.append(processed_px)
    
    return processed_pxs
   






if __name__ == "__main__":
    # Get the image path
    root_dir = os.path.dirname(os.getcwd())
    im_path = os.path.join(root_dir, 'Reversible_Data_Hiding/misc/5.1.09.tiff')
     
    updated_pixels = pre_processing(im_path)
    print(updated_pixels)
    