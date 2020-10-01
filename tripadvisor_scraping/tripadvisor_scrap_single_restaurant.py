from bs4 import BeautifulSoup
import requests
import re

s = requests.Session()


def get_soup(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'}
    r = s.get(url, headers=headers)
    if r.status_code != 200:
        print('status code:', r.status_code)
    else:
        return BeautifulSoup(r.text, 'html.parser')


def parse(url, response):
    if not response:
        print('no response:', url)
        return

    # get data


def parse_reviews(url, response):
    print('review:', url)

    if not response:
        print('no response:', url)
        return

    # get every review
    for idx, review in enumerate(response.find_all('div', class_='review-container')):
        item = {
            'hotel_name': response.find('h1', class_='heading_title').text,
            'review_title': review.find('span', class_='noQuotes').text,
            'review_body': review.find('p', class_='partial_entry').text,
            'review_date': review.find('span', class_='relativeDate')['title'],  # .text,#[idx],
            'num_reviews_reviewer': review.find('span', class_='badgetext').text,
            'reviewer_name': review.find('span', class_='scrname').text,
            'bubble_rating': review.select_one('div.reviewItemInline span.ui_bubble_rating')['class'][1][7:],
        }

        results.append(item)  # <--- add to global list


# --- main ---


start_urls = [
    'https://www.tripadvisor.com/Attraction_Review-g187323-d190710-Reviews-CHAMALEON_Theater-Berlin.html'
]

results = []  # <--- global list for items
#
# for url in start_urls:
#     parse(url, get_soup(url))
#
# # import pandas as pd
#
# df = pd.DataFrame(results)  # <--- convert list to DataFrame
# df.to_csv('output.csv')  # <--- save in file
