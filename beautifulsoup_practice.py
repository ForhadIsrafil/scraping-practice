import time
import re
import requests
from bs4 import BeautifulSoup


# --------------------
def getPage(url):
    """
    Utilty function used to get a Beautiful Soup object from a given URL
    """
    session = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    try:
        req = session.get(url, headers=headers)
    except requests.exceptions.RequestException:
        return None
    bs = BeautifulSoup(req.text, 'html.parser')
    return bs


# --------------------

html = requests.get('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.text, "html.parser")

nameList = bs.find_all('span', {'class': 'green'})
titles = bs.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
allText = bs.find_all('span', {'class': {'green', 'red'}})  # find all with a tag and multiple class name
name_list = bs.find_all(text='the prince')
title = bs.find_all(id='title', class_='text')  # find all with a id and  class name
for child in bs.find('table', {'id': 'giftList'}).children:
    print(child)

for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(sibling)

print(bs.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())

# ---------------------
images = bs.find_all('img', {'src': re.compile('\.\.\/img\/gifts/img.*\.jpg')})
for image in images:
    print(image['src'])
# ---------------------
bs.find_all(lambda tag: len(tag.attrs) == 2)
bs.find_all(lambda tag: tag.get_text() == 'Or maybe he\'s only resting?')
bs.find_all('', text='Or maybe he\'s only resting?')

for link in bs.find_all('a', limit=20):
    if 'href' in link.attrs:
        print(link.attrs['href'])

for link in bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])

print(bs.h1.get_text())
print(bs.find(id='mw-content-text').find_all('p')[0])
print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])
