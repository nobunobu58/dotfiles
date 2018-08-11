#! /usr/bin/env python3
# downLoadXkcd.py

import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd',exist_ok=True)

while not url.endswith('#'):
    # ページをダウンロードする
    print('ページをダウンロード中{}....'.format(url))
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

print('完了')
