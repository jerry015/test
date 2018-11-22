import urllib2
import ssl
import time
from bs4 import BeautifulSoup
import cookielib

auto_atk_url = 'https://club.autohome.com.cn/bbs/thread/da7fd1e39664037e/77347159-1.html#pvareaid=102410'


# request.add_header('User-Agent', 'Mozilla/5.0')
# request.add_header('Host', 'club.autohome.com.cn')
# request.add_header('Connection', 'keep-alive')
# request.add_header('Accept-Language', 'zh-CN,zh;q=0.9,en;q=0.8')
# request.add_header('Cookie', 'sessionid=6D7AB08D-3FC4-A8D7-FCE1-AA715A46C055%7C%7C2015-11-28+18%3A02%3A11.685%7C%7C0; tagid=9FB13E3B-CDEE-410E-5EBD-6FB92B1F5AAC; fvlid=1484443726344jIR2BkA4; __utma=1.97715377.1448704926.1471261225.1484443731.8; __ah_uuid=6DFFDAC8-38E9-41D3-8F57-1B44D5CA6EAF; sessionip=123.185.61.231; sessionvid=0BD38AAA-1090-4495-AAB9-6CA6182B5D04; area=210203; ahpau=1; sessionuid=6D7AB08D-3FC4-A8D7-FCE1-AA715A46C055%7C%7C2015-11-28+18%3A02%3A11.685%7C%7C0; papopclub=2767926F557307AFEFE3F72C04B371BD; pbcpopclub=41ab843a-e71b-40d1-af95-e79d005ab989; pepopclub=667F624E6A791CC40B6386C371BDF79A; pvidchain=3311254,2341162,102410,102410,102410,102410,102410,102410,102410,102410; ahpvno=14; ref=0%7C0%7C0%7C0%7C2018-11-21+18%3A39%3A20.736%7C2018-11-21+18%3A23%3A06.442; ahrlid=1542796755160esw6W5NFDA-1542797143425')

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
request = urllib2.Request(auto_atk_url)
request.add_header('User-Agent', 'Mozilla/5.0')
request.add_header('Host', 'club.autohome.com.cn')
request.add_header('Connection', 'keep-alive')
request.add_header('Accept-Language', 'zh-CN,zh;q=0.9,en;q=0.8')
html = opener.open(request)

soup = BeautifulSoup(html.read())
img = soup.find_all('img')

print img