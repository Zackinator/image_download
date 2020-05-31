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
import sys




# Target dataset PATH
DATASET_PATH = "./dataset"
#Fake user agent for avoiding 503 Error
Headers = {'User-Agent': 'Mozilla/5.0(X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
#Advanced parameters
#Categories want to scrap
CATEGORIES = ['dog','cat']

#Page limit to search for images url
PAGE_FROM = 1
PAGE_TO = 2
#NUMBER of workers for downloading pages and images better and faster
WORKERS = 4

image_urls = []
timeout = 60 #Request timeout
checkfolder = input("Enter the name of the folder where you want to store images: ")


def image_downloader(img):
    image_url = img
    number = 1
    #checkfolder = str(input("Enter the name of the folder where you want to store images: "))
    #newpath = r"C:\Users\zacka\gitclone\image_download\image_download\\" + checkfolder + "\\"
    try:
        if os.path.exists(r"C:\Users\zacka\gitclone\image_download\image_download" + "\\" + checkfolder):
            print("\n \n DIRECTORY >" ,r"C:\Users\zacka\gitclone\image_download\image_download" + "\\" + checkfolder, " ALREADY EXISTS\n TRY A DIFFERENT NAME:\n")
            ex = input("Type exit to exit, or press enter to change directory name")
            if ex == "exit":
                sys.exit(0)
            else:
                new = input("Enter the name of the folder where you want to store images: ")
                os.mkdir(r"C:\Users\zacka\gitclone\image_download\image_download" + "\\" + new)
                print("Directory" ,r"C:\Users\zacka\gitclone\image_download\image_download" + "\\" + new, "Created ")
                os.chdir(r"C:\Users\zacka\gitclone\image_download\image_download" + "\\" + new)
        else:
            os.mkdir(r"C:\Users\zacka\gitclone\image_download\image_download" + "\\" + checkfolder)
            print("Directory" ,r"C:\Users\zacka\gitclone\image_download\image_download" + "\\" + checkfolder, "Created ")
            os.chdir(r"C:\Users\zacka\gitclone\image_download\image_download" + "\\" + checkfolder)
    except FileExistsError:
        print("Directory " , newpath, " already exists")
        sys.exit(0)
    for i in image_url:
        file = "i" + str(number) + '.jpg'
        number += 1
        print('filename: ','FILE>',number)
        print('URL: ',i)
        '''Streaming, so we can iterate over the response.'''
        r = requests.get(i, stream = True)
        r.raw.decode_content = True
        print(r)
        '''Set decode_content value to True, otherwise the downloaded image
        file's size will be zero'''

        ''' Total size in bytes.'''
        total_size = int(r.headers.get('content-length', 0))
        block_size = 1024 #1 kikibyte
        t=tqdm(total=total_size, unit='iB', unit_scale=True)

        ''' Open a local file with wb ( Write Binary ) premission.'''
        with open(file,'wb') as f:
            for data in r.iter_content(block_size):
                t.update(len(data))
                f.write(data)
            shutil.copyfileobj(r.raw, f)

            '''Close Loading bar'''
        t.close()
        if total_size !=0 and t.n != total_size:
            print("Error, something went wrong")



        http = urllib3.PoolManager()
        test = img

        '''Request status code'''
        try:
            resp = http.request('GET', test)
            print(resp.data)
            print(resp.status)
        except Exception as e:
            print(e)

def get_browser_image():
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
            imgsrc.append(a.img['src'])
    imgsrc.pop(0)
    return imgsrc

if __name__ == "__main__":
    imgli = get_browser_image()
    image_downloader(imgli)
