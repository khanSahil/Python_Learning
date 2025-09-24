# read official documentation at pillow.readthedocs.io
from PIL import Image 

# Basic Image functionality

mac = Image.open("example.jpg")
print(type(mac))
#mac.show()
print(mac.size)
print(mac.filename)
print(mac.format_description)



# Cropping image now

crop_image = mac.crop((0,0,100,100))
#crop_image.show()

halfway = 1993/2
x = halfway - 200
w = halfway + 200

y = 800
h = 1257

crop_image = mac.crop((x,y,w,h))
#crop_image.show()

computer = mac.crop((x,y,w,h))
mac.paste(im=computer, box=(0,0))
#mac.show()

#mac.rotate(90).show()

mac_resize = mac.resize((3000,500))
#mac_resize.show()

pencils = Image.open("pencils.jpg")
#pencils.show()

print(pencils.size)

x = 0
y = 1100

w = 1950 / 3
h = 1300

crop_image = pencils.crop((x,y,w,h))
#crop_image.show()



# Color Transparency

red = Image.open('red_color.jpg')
red.show()
red.putalpha(128)
red.show()

blue = Image.open('blue_new.jpg')
blue.show()

blue.putalpha(0)
blue.show()


blue.putalpha(128)
blue.show()


blue.paste(im=red,box=(0,0),mask=red)
blue.show()

purple = Image.open("purple.png")
print(type(purple))
purple.show()

blue.save("purple.jpg")
purple = Image.open("purple.jpg")
print(type(purple))
purple.show()