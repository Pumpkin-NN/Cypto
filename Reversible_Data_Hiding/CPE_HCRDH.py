from AES_CBC import image_aes_cbc, image_aes_decrypted 
from PRE_PROCESSING import pre_processing
from MSB_LSB import image_msb_lsb
from PIL import Image
import os

'''
Main Function
'''
if __name__ == "__main__":
    
    # Get the original image path
    root_dir = os.path.dirname(os.getcwd())
    im_path = os.path.join(root_dir, 'Reversible_Data_Hiding/misc/5.2.09.tiff')
    
    # Save the original image
    original_img = Image.open(im_path)
    original_img.save("original_img.png")
    
    # Save the pre-processed image
    pre_processing_img = pre_processing(im_path)
    pre_processing_img.save("pre_processed_img.png")
    
    # Get the pre-processed image path
    pre_processed_img_path = os.path.join(root_dir, 'Reversible_Data_Hiding/pre_processed_img.png')
    
    ############################################MSB/LSB############################################
    
    # Save the MSB/LSB encrypted image
    msb_encrypted_img = image_msb_lsb(pre_processed_img_path)
    msb_encrypted_img.save('msb_encrypted_img.png')

    # Get the MSB/LSB encrypted image path
    encrypted_img_path = os.path.join(root_dir, 'Reversible_Data_Hiding/msb_encrypted_img.png')
    
    # Save the MSB/LSB decrypted image
    msb_decrypted_img = image_msb_lsb(encrypted_img_path)
    msb_decrypted_img.save('msb_decrypted_img.png')
    
    ############################################AES###############################################
    
    # Save the AES encrypted pre-processing image
    aes_encrypted_img, key, IV= image_aes_cbc(pre_processed_img_path)
    aes_encrypted_img.save('aes_encrypted_img.png')
    
    # Get the source file
    # Save the AES decrypted pre-processing image
    root_dir = os.path.dirname(os.getcwd())
    aes_image = os.path.join(root_dir, 'Reversible_Data_Hiding/aes_image.pickle')
    aes_decrypted_img = image_aes_decrypted(aes_image, key, IV)
    
    aes_decrypted_img.save('aes_decrypted_img.png')
    
    ######################################Image Recover###########################################
    
    # Get the AES decrypted pre-processing image path
    aes_decrypted_img_path = os.path.join(root_dir, 'Reversible_Data_Hiding/aes_decrypted_img.png')
    
    # Save the decrypted image
    recover_image = image_msb_lsb(aes_decrypted_img_path)
    recover_image.save('recover_image.png')
