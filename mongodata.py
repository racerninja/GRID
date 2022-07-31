import pymongo
from pymongo import MongoClient
import flipkartsearch as fl

cluster = MongoClient("mongodb+srv://manavgrover:sexaddict69@cluster0.nxg7w.mongodb.net/?retryWrites=true&w=majority")

db = cluster["Matrix"]
collection = db["sneakers"]

d = {"product_brand" : fl.BRAND,
 "product_name" : fl.NAME,
 "product_link" : fl.PRODUCT_LINK,
 "product_des" : fl.PRODUCT_DES,
 "price" : fl.PRODUCT_PRICE,
 "image_links" : fl.IMAGE_LINKS,
 "insta_links" : fl.INSTA_LINKS,
 "flipkart_link":fl.FLIPKART_LINK,
 "color":fl.COLOR}

collection.insert_one(d)
