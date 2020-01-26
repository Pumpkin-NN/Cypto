from PIL import Image
import io
from bitstring import BitArray


f = ""
with open("/Users/home/github/Cypto/Reversible_Data_Hiding/original_img.png", "rb") as image:
  f = image.read()
  f = f+f
print(f)

image = Image.open(io.BytesIO(f))
print("I am an image")
image.show()