import urllib3

http = urllib3.PoolManager()

img_url = 'http://tutorialspoint.com/robots.txt'


resp = http.request('GET', img_url)
print (resp.data)


print (resp.status)
