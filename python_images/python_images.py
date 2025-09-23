# read official documentation at pillow.readthedocs.io

from PIL import Image 
mac = Image.open("example.jpg")
print(type(mac))
print(mac.show())
