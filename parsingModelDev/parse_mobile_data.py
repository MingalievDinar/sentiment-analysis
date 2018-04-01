import requests
import bs4
from multiprocessing import Pool
import codecs
import time
import random

with open('parsing_results2.txt', 'r') as file:
    l = file.read()
short_links = l.split('\n')
url_list = ['http://irecommend.ru' + i for i in short_links]

hdr = {"User-Agent": "Mozilla/5.0",
       "Accept-Encoding":"gzip, deflate, sdch",
       "Accept-Language":"ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4"}

def parse_page(url):
    n = 0
    s = 0
    
    COND_ALLOW_PARS = True
    # sleep while banned
    while COND_ALLOW_PARS:
        text = requests.get(url, headers = hdr).text
        parser = bs4.BeautifulSoup(text, 'lxml')
        tag_h1 = parser.find('h1')
        COND_ALLOW_PARS = (tag_h1.get_text()[:28] == u'\u041d\u0430 \u0441\u0430\u0439\u0442\u0435 \u0432\u0435\u0434\u0443\u0442\u0441\u044f \u0442\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0435')
        print "trying to parse " + url
        print tag_h1
        print "COND_ALLOW_PARS :{}".format(COND_ALLOW_PARS)
        s += 5+n
        time.sleep(5+n)
        n += 1
        print "Sleep now: {} sec. Total sleep: {} sec".format(n+5, s)
    try:
        rating = float(parser.find('span', attrs={'class':'on rating', 'itemprop':'ratingValue'}).get_text())
    except:
        rating = -1
    try:
        text = parser.find('div', attrs={'class':'description hasinlineimage', 'itemprop':'reviewBody'}).get_text().replace('\n', "").replace('\t', '')
    except:
        try:
            # different class values
            text = parser.find('div', attrs={'class':'description', 'itemprop':'reviewBody'}).get_text().replace('\n', "").replace('\t', '')
        except:
            text = ""
    z = {'rating' : rating, 'feedback':text}
    print "parssed link" + url
    sleep_s = 5 + random.randint(0,10)/10.0
    print 'Sleep after parsing {} sec'.format(sleep_s)
    time.sleep(sleep_s)
    return z

data = list()
for url in url_list[:2]:
    res = parse_page(url)
    data.append(res)