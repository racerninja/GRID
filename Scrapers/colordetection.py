import io
from PIL import Image
import requests
import freesocietyscrapper as fs

img = fs.valid_images[0]
img = requests.get(img).content
img = io.BytesIO(img)

im = Image.open(img)

file_path = "sneakers/test.jpg"
with open(file_path, "wb") as f:
    im.save(f, "png")

im = Image.open('sneakers/test.jpg')
im = im.crop((300, 200, 400, 300))
im.show()

pixels = list(im.convert('RGBA').getdata())
n = len(pixels)
r, g, b, a = pixels[n // 2]
color = [r, g, b]
print(color)
