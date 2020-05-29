import requests  #To get image from the web'''
import shutil  #To save it locally'''
import urllib3
from tqdm import tqdm


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
        resp = http.request('GET', img_url)
        print(resp.data)
        print(resp.status)
    except Exception as e:
        print(e)

image_downloader()
req_test()
