from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time
import instascrapper as insta
import colordetection as cd

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.flipkart.com/")

BRAND = insta.brand
NAME = insta.name
PRODUCT_LINK = insta.product_link
PRODUCT_DES = insta.product_des
PRODUCT_PRICE = insta.product_price
INSTA_LINKS = insta.images
IMAGE_LINKS = insta.image_links
COLOR = cd.color

search = driver.find_element_by_name("q")
search.send_keys(BRAND + " " + NAME)
search.send_keys(Keys.RETURN)

print("Flipkart Link for the product")
FLIPKART_LINK = driver.current_url
print(driver.current_url)

time.sleep(3)
driver.quit()
