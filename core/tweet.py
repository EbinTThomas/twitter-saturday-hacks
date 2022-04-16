from PIL import Image, ImageDraw, ImageFont
import os

def quote_to_image(input_image, quote):
  img = Image.open(input_image)
  width, height = img.size
  
  newsize = (1920, 1920)
  oimg = img.resize(newsize)
  oimg.show()
  d1 = ImageDraw.Draw(oimg)
  myFont = ImageFont.defaultFont()
  d1.text((65, 170), quote, fill=(0, 0, 0), font=myFont)
  
  oimg.save("results.jpeg")
  return oimg