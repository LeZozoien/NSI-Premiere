from PIL import Image
from matplotlib.pyplot import plot, show

img = Image.open('poisson.jpg')
img = img.convert("L")
img.show()

def histogramme(image:Image.Image):
    width, height = image.size
    hist = [0]*256
    for y in range(height):
        for x in range(width):
            hist[image.getpixel((x, y))] += 1
    return hist

plot(histogramme(img))
show()