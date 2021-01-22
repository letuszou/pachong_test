# coding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import io
import re
import json
import time


# Use-Agent
# 糗事百科图片 爬取

def doIt():
    for page in range(1, 10):
        downloadPage(page)
        time.sleep(2)


def downloadPage(page):
    # "'https://www.qiushibaike.com/imgrank/page/1/'"
    url = "https://www.qiushibaike.com/imgrank/page/%d/" % page
    print (url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'
    }

    page_text = requests.get(url, headers=headers).text
    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    # text(源码字符串) content(二进制) json(对象)
    img_src_list = re.findall(ex, page_text, re.S)
    for src in img_src_list:
        src = 'https:' + src
        img_data = requests.get(url=src, headers=headers).content
        imgName = src.split('/')[-1]
        imgPath = './qiutulibs/' + imgName
        with open(imgPath, 'wb') as fp:
            fp.write(img_data)
            print (imgName.encode('utf-8'), 'download success!!!')


if __name__ == "__main__":
    doIt()
    print ("success")
