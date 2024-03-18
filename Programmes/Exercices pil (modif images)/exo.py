from PIL import Image

img = Image.open("poisson.jpg")
img.show()
img = img.reduce(2)
img = img.rotate(90)
img = img.transpose(Image.FLIP_TOP_BOTTOM)
img.show()