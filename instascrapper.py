import time
from bs4 import BeautifulSoup
import requests
import freesocietyscrapper as fs
from selenium import webdriver

brand = fs.product_brand
name = fs.product_name
product_link = fs.product_link
product_des = fs.product_des
product_price = fs.product_price
image_links = fs.valid_images

valid_name = ""
flag = False

for x in name:
    if x == " ":
        if flag is False:
            flag = True
        else:
            break
    else:
        valid_name += x.lower()

url = "https://www.instagram.com/explore/tags/" + valid_name + "/?hl=en"
instagram = "https://www.instagram.com/"

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

result = driver.get(url)
time.sleep(3)
soup = BeautifulSoup(driver.page_source, "html.parser")

images = []
for x in soup.find_all("img"):
    images.append(x.get("src"))

images = images[1:7]
print("Related trends on instagram")
for x in images:
    print(x)
driver.quit()

