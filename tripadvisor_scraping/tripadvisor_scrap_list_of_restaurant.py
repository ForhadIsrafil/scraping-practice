from bs4 import BeautifulSoup
import requests
import re
import time
import pandas as pd

s = requests.Session()


def get_soup(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'}
    r = s.get(url, headers=headers)
    time.sleep(5)
    if r.status_code != 200:
        print('status code:', r.status_code)
    else:
        return BeautifulSoup(r.text, 'html.parser')


def get_restaurant_list():
    restaurant_link_list = []
    title_list = []
    soup = get_soup('https://www.tripadvisor.com/Attractions-g187323-Activities-c20-Berlin.html')
    # href=re.compile('/[[:<:]]Attraction_Review-')
    for link in soup.find_all('a'):

        if 'href' in link.attrs:
            if '/Attraction_Review-' in link.attrs['href'] and str(
                    link.attrs['href'][-5:]) == '.html' and 'class' in link.attrs:
                # print(link)
                if str(link.attrs['href']) not in restaurant_link_list:
                    restaurant_link_list.append(str(link.attrs['href']))
                    for title in link:
                        print(title.text)
                        title_list.append(str(title.text))

                    # restaurant_link_list.append(str(link.parent))
            # elif '.html#REVIEWS' in link.attrs['href']:

    print(len(restaurant_link_list))
    print(len(title_list))
    data = {'Links': restaurant_link_list, 'Titles': title_list}
    df = pd.DataFrame(data, columns=['Links', 'Titles'])
    df.to_excel('restaurant_link.xlsx', index=False)


get_restaurant_list()
# def parse(url, response):
#     if not response:
#         print('no response:', url)
#         return
#
#     # get data
#
#
# def parse_reviews(url, response):
#     print('review:', url)
#
#     if not response:
#         print('no response:', url)
#         return
#
#     # get every review
#     results = []
#     for idx, review in enumerate(response.find_all('div', class_='review-container')):
#         item = {
#             'hotel_name': response.find('h1', class_='heading_title').text,
#             'review_title': review.find('span', class_='noQuotes').text,
#             'review_body': review.find('p', class_='partial_entry').text,
#             'review_date': review.find('span', class_='relativeDate')['title'],  # .text,#[idx],
#             'num_reviews_reviewer': review.find('span', class_='badgetext').text,
#             'reviewer_name': review.find('span', class_='scrname').text,
#             'bubble_rating': review.select_one('div.reviewItemInline span.ui_bubble_rating')['class'][1][7:],
#         }
#
#         results.append(item)  # <--- add to global list
