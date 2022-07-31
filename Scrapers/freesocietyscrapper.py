from bs4 import BeautifulSoup
import requests
import random

url = "https://freesociety.in/collections/sneakers-2"

result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")

links = []
for x in soup.find_all("a"):
    links.append(x.get("href"))

valid_links = []
for link in links:
    if "/products/" in link:
        valid_links.append(url + link)

product_link = random.choice(valid_links)
result = requests.get(product_link)
soup = BeautifulSoup(result.text, "html.parser")

product_brand = soup.find("p", {"class" : "product-single__vendor"}).string
product_name = soup.find("h1").string
product_des = soup.find("span", {"data-mce-fragment":"1"})
product_price = soup.find("span", {"id":"ProductPrice-product-template"}).string.strip()

if product_des:
    product_des = product_des.string.strip()

else:
    product_des = "No Description"

images = []
for x in soup.find_all("a"):
    images.append(x.get("href"))

valid_images = []
for image in images:
    if "cdn.shopify.com" in image and "1024x1024" in image:
        valid_images.append("https:" + image)

print("Brand", product_brand)
print("Name", product_name)
print("Link", product_link)
print("Description", product_des)
print("Price", product_price)
print("Product Images")

for x in valid_images:
    print(x)
