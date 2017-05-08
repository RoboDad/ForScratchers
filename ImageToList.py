from PIL import Image
im = Image.open("cairo.jpg")
im = im.resize((50,50), Image.LANCZOS).transpose(Image.FLIP_TOP_BOTTOM)
#im.show();
pixels = list(im.getdata())

file = open("MariaImageData.txt",'w')
for pixel in pixels:
	file.write( str(pixel[2] + (pixel[1]<<8) + (pixel[0]<<16)) + "\n")
file.close()
