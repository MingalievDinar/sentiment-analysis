import requests
import bs4
from multiprocessing import Pool
import codecs
import time
hdr = {"User-Agent": "Mozilla/5.0",
       "Accept-Encoding":"gzip, deflate, sdch",
       "Accept-Language":"ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4"}

def parse_page(url):
    n = 0
    s = 0
    COND_ALLOW_PARS = False
    while not COND_ALLOW_PARS:
        text = requests.get(url, headers = hdr).text
        parser = bs4.BeautifulSoup(text, 'lxml')
        tag_h1 = parser.find('h1')
        COND_ALLOW_PARS = (tag_h1.get_text()[:10] == u'\u041c\u043e\u0431\u0438\u043b\u044c\u043d\u044b\u0435 ')
        print "trying to parse " + url
        print tag_h1
        print "COND_ALLOW_PARS :{}".format(COND_ALLOW_PARS)
        s += 5+n
        time.sleep(5+n)
        n += 1
        print "Sleep now: {} sec. Total sleep: {} sec".format(n+5, s)
    x = parser.findAll('div', attrs={'class':'citate'})
    z = [item.find('a').get('href') for item in x]
    print "parssed link" + url
    time.sleep(5)
    return z

p = Pool(1)
url_list = ['http://irecommend.ru/category/mobilnye-telefony?page=' + str(n) for n in range(0, 162)]
    
if __name__ == '__main__':    
    map_results = p.map(parse_page, url_list)
    reduce_results = reduce(lambda x,y: x + y, map_results)
    with codecs.open('parsing_results2.txt', 'w', 'utf-8') as output_file:
        print >> output_file, u'\n'.join(reduce_results)