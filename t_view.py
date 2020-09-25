from time import sleep
import os
import requests
from tqdm.auto import tqdm
from pprint import pprint
import csv

r = requests.get('https://api.github.com/events')
data = r.json()

# pip install tqdm
# loop = tqdm(total=5000, position=0, leave=False)
# for d in range(5000):
#     loop.set_description('Loading....'.format(d))
#     loop.update()
with open('git_data.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    for d in tqdm(data, desc='Loading.....'):
        # pprint(d['id'])
        # pprint(d['actor']['url'])
        sleep(.3)
        spamwriter.writerow([d['id'], d['actor']['url']])
        # print(d)

    # loop.close()
    # pprint([data[d]['type'] for d in range(10)])
    # import json
    #
    #
    # with open('Demo.json', ) as f:
    #     data = json.loads(f)
    #     print(data)
