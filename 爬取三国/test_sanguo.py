# coding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import io
import re
import json
import time
import requests

from bs4 import BeautifulSoup


def doIt():
    url = 'https://www.shicimingju.com/book/shuihuzhuan.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36',
    }
    page_text = requests.get(url=url, headers=headers).content
    soup = BeautifulSoup(page_text, 'lxml')
    mulu_list = soup.select('.book-mulu > ul > li')
    fp = open('./sanguo.txt', 'w')
    for mulu in mulu_list:
        time.sleep(1)
        title = mulu.a.text
        fp.write(title)
        detail_url = 'https://www.shicimingju.com' + mulu.a['href']
        detail_page_text = requests.get(url=detail_url, headers=headers).content
        detail_soup = BeautifulSoup(detail_page_text, 'lxml')
        div_tag = detail_soup.find('div', class_='chapter_content')
        content = div_tag.text.decode('utf-8')
        fp.write(title + content + "\n")
        print (title)


if __name__ == "__main__":
    doIt()
    print ("success")
