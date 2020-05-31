import requests  #To get image from the web'''
import shutil  #To save it locally'''
import urllib3
import os
import ast
import urllib.request as ulib
from tqdm import tqdm
from bs4 import BeautifulSoup as soup
from selenium import webdriver
import re
import concurrent.futures
import random


imgsrc = []
'''Search the web for a category of images: ex Nic cage'''
searchterm = input("Enter the search term for picture download: ")
url = "https://www.google.com/search?q="+ searchterm +"&sxsrf=ALeKk00EFUoVu7Ictc6MqzlQ1WqvGcIgng:1590772434462&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjo9f6OydnpAhVXQH0KHW4xAHMQ_AUoAXoECBkQAw&biw=2560&bih=937"
r = requests.get(url)
html = r.text
Soup = soup(html, 'lxml')
#links = Soup.find_all('img')
for a in Soup.find_all('a'):
    if a.img:
        print(a.img['src'],a.img['alt'])
        im = (a.img['src'],a.img['alt'])
        imgsrc.append(im)
imgsrc.pop(0)
print(imgsrc)
