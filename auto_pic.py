import urllib
import urllib3
import ssl
import time
from bs4 import BeautifulSoup
from http import cookiejar
import os




def download_auto_ark(auto_atk_url, folder):
    # auto_atk_url = 'https://club.autohome.com.cn/bbs/thread/da7fd1e39664037e/77347159-1.html#pvareaid=102410'

    cj = cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    request = urllib.request.Request(auto_atk_url)
    request.add_header('User-Agent', 'Mozilla/5.0')
    request.add_header('Host', 'club.autohome.com.cn')
    request.add_header('Connection', 'keep-alive')
    request.add_header('Accept-Language', 'zh-CN,zh;q=0.9,en;q=0.8')
    try:
        html = opener.open(request)
    except:
        return
    

    soup = BeautifulSoup(html.read(),'html.parser')
    img = soup.find_all('img')

    def pic_herf(y):
        return y.get('src9')

    img_src = list(map(pic_herf,img))


    def pic_img(x):
        return 'userphotos' in x
    def check_none(z):
        return z
    img_filter1 = list(filter(check_none,img_src))
    img_filter2 = list(filter(pic_img, img_filter1))

    def add_https(a):
        return "https:" + a

    img_filter3 = list(map(add_https,img_filter2))


    for x in img_filter3:
        # cj2 = cookiejar.CookieJar()
        # opener2 = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj2))
        print("processing " + str(img_filter3.index(x) + 1) + '/' + str(len(img_filter3)) + ' pic')
        request = urllib.request.Request(x)
        request.add_header('User-Agent', 'Mozilla/5.0')
        # request.add_header('Host', 'club.autohome.com.cn')
        request.add_header('Connection', 'keep-alive')
        request.add_header('Accept-Language', 'zh-CN,zh;q=0.9,en;q=0.8')
        request.add_header('Referer','https://club.autohome.com.cn/bbs/thread/49a735c3cf5dff09/77253048-1.html')
        # opener.open(request)

        # request2 = urllib.request.Request(pic_url)
        # print(pic_url)
        # request2.add_header('User-Agent', 'Mozilla/5.0')
        # request2.add_header('Host', 'club.autohome.com.cn')
        # request2.add_header('Connection', 'keep-alive')
        # request2.add_header('Accept-Language', 'zh-CN,zh;q=0.9,en;q=0.8')

        try:
            html = urllib.request.urlopen(request,timeout=60)
        except:
            continue
        # html = urllib.request.urlopen(request)

        file_name = folder + str(time.time()).split('.')[0] + '.' + x.split('.')[-1]

        if os.path.exists(folder) == False:
            os.makedirs(folder)

        with open(file_name, 'wb') as file:
            file.write(html.read())
            file.flush()
            file.close()
        
        time.sleep(1)


folder = '../photo/' + str(time.time()).split('.')[0] + '/'

ch_etk_url = 'https://club.autohome.com.cn/jingxuan/104/'

cj = cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
request = urllib.request.Request(ch_etk_url)
request.add_header('User-Agent', 'Mozilla/5.0')
request.add_header('Host', 'club.autohome.com.cn')
request.add_header('Connection', 'keep-alive')
request.add_header('Accept-Language', 'zh-CN,zh;q=0.9,en;q=0.8')
html = opener.open(request)

soup = BeautifulSoup(html.read(),'html.parser')
img = soup.find_all('a')

def pic_herf(y):
    return y.get('href')

img_src = list(map(pic_herf,img))


def pic_img(x):
    return 'bbs' in x
def check_none(z):
    return z
img_filter1 = list(filter(check_none,img_src))
img_filter2 = list(filter(pic_img, img_filter1))

def add_https(a):
    return "https:" + a

img_filter3 = list(map(add_https,img_filter2))
img_filter3 = img_filter3[5:]
img_filter3 = list(set(img_filter3))

for x in img_filter3:
    print("processing " + str(img_filter3.index(x) + 1) + '/' + str(len(img_filter3)) + ' url')
    download_auto_ark(x,folder)
