from PIL import Image
im = Image.open("mex-hibiscus-2.jpg")
im = im.resize((40,40), Image.LANCZOS)
#im.show();
pixels = list(im.getdata())

file = open("MariaImageData.txt",'w')
for pixel in pixels:
	file.write( str(pixel[2] + (pixel[1]<<8) + (pixel[0]<<16)) + "\n")
file.close()
