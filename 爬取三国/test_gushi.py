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
    url = 'https://www.shicimingju.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36',
    }
    page_text = requests.get(url=url, headers=headers).content
    soup = BeautifulSoup(page_text, 'lxml')
    gushi_list = soup.select('.shici_card')
    fp = open('./gushi.txt', 'w')
    for gushi in gushi_list:
        title = gushi.h3.a.string
        writer = gushi.div.a.string
        div_tag = gushi.find('div', style=re.compile(r'display: none'))
        if div_tag:
            content = div_tag.text.strip()
            fp.write(title + "\n" + writer + "\n" + content + "\n")


if __name__ == "__main__":
    doIt()
    print ("success")
