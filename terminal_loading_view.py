from time import sleep

import requests
from tqdm.auto import tqdm
from pprint import pprint

r = requests.get('https://api.github.com/events')
data = r.json()

# pip install tqdm
# loop = tqdm(total=5000, position=0, leave=False)
# for d in range(5000):
#     loop.set_description('Loading....'.format(d))
#     loop.update()

for d in tqdm(data, desc='Loading.....'):
    print('', end='\r')
    sleep(.1)
    # print(d)

# loop.close()
# pprint([data[d]['type'] for d in range(10)])
# import json
#
#
# with open('Demo.json', ) as f:
#     data = json.loads(f)
#     print(data)
