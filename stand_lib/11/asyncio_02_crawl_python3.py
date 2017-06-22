from bs4 import BeautifulSoup
import requests
import gevent
from gevent import monkey, pool
monkey.patch_all()
from lxml import html

jobs = []
links = []
p = pool.Pool(10)

urls = [
    'http://cn.bing.com',
    # another 100 urls
]


def get_links(url):
    r = requests.get(url)
    if r.status_code == 200:
        #soup = BeautifulSoup(r.text)
        soup = BeautifulSoup(r.text, "html.parser")
        print(soup)
        links + soup.find_all('b')
        # 看不懂,待后期完善

for url in urls:
    jobs.append(p.spawn(get_links, url))

gevent.joinall(jobs)
