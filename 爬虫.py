import urllib
from urllib import error
from urllib import request
import requests
from bs4 import BeautifulSoup

def geturl(url):
    header= {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Mobile Safari/537.36 Edg/90.0.818.46'}
    html = ''
    try:
        req = urllib.request.Request(url, headers=header)
        response = urllib.request.urlopen(req)
        html = response.read().decode('gbk')
    except urllib.error.URLError as e:
        print(e.reason)
    return html
count = 0
for item in range(1,31):
    u = "https://pic.netbian.com/4kmeinv/" + 'index_' + str(item) + '.html'
    html = geturl(u)
    imgs = BeautifulSoup(html,'lxml')
    img_list = imgs.select('li > a > img')
    for i in img_list:
        count += 1
        print('第' + str(item) + '组' + '第' + str(count) + '张图片开始下载')
        img_src = 'https://pic.netbian.com/' + i['src']
        print('---------------------------------------------------------')
        print('第' + str(item) + '组' + '第' + str(count) + '张图片完成下载')
        urllib.request.urlretrieve(img_src,'./妹妹图/'+ str(count) +'.jpeg')

