import requests  #To get image from the web'''
import shutil  #To save it locally'''
import urllib3
import os
import ast
import urllib.request as ulib
from tqdm import tqdm
from bs4 import BeautifulSoup as soup
from selenium import webdriver

def image_downloader():
    image_url = "https://cdn.pixabay.com/photo/2020/02/06/09/39/summer-4823612_960_720.jpg"
    filename = image_url.split("/")[-1]

    '''Streaming, so we can iterate over the response.'''
    r = requests.get(image_url, stream = True)

    '''Set decode_content value to True, otherwise the downloaded image
    file's size will be zero'''
    r.raw.decode_content = True

    ''' Total size in bytes.'''
    total_size = int(r.headers.get('content-length', 0))
    block_size = 1024 #1 kikibyte
    t=tqdm(total=total_size, unit='iB', unit_scale=True)

    ''' Open a local file with wb ( Write Binary ) premission.'''
    with open(filename,'wb') as f:
        for data in r.iter_content(block_size):
            t.update(len(data))
            f.write(data)
        shutil.copyfileobj(r.raw, f)

    '''Close Loading bar'''
    t.close()
    if total_size !=0 and t.n != total_size:
        print("Error, something went wrong")

def req_test():
    http = urllib3.PoolManager()
    img_url = "https://cdn.pixabay.com/photo/2020/02/06/09/39/summer-4823612_960_720.jpg"

    '''Request status code'''
    try:
        wait = input('Requesting URL....')
        resp = http.request('GET', img_url)
        print(resp.data)
        print(resp.status)
    except Exception as e:
        print(e)

def get_browser_image():
    '''Search the web for a category of images: ex Nic cage'''
    searchterm = input("Enter the search term for picture download: \n")
    driver = webdriver.Chrome("chromium.exe")
    url = "https://www.google.com/search?q="+ searchterm +"&sxsrf=ALeKk00EFUoVu7Ictc6MqzlQ1WqvGcIgng:1590772434462&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjo9f6OydnpAhVXQH0KHW4xAHMQ_AUoAXoECBkQAw&biw=2560&bih=937"
    driver.get(url)
    page = driver.page_source

    Soup = soup(page,'lxml')
    urls = Soup.find_all('div',{'class':'rg_i Q4LuWd tx8vtf'})

    all_urls = []

    for i in urls:
        link = i.text
        link = ast.literal_eval(link)['ou']
        all_urls.append(link)
        print(all_urls)
    return(all_urls)

get_browser_image()
#image_downloader()
#req_test()
