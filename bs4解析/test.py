# coding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import io
import re
import json
import time

from bs4 import BeautifulSoup


# Use-Agent
# 糗事百科图片 爬取

def doIt():
    fp = open('./test.html', 'r')
    soup = BeautifulSoup(fp, 'lxml')
    # soup.find(tagName) 等同于 soup.tagName 返回的是文档中第一个出现tagName的标签
    # print (soup.a)
    # print (soup.li)
    # print (soup.find('div', class_='form-group'))
    # 返回 所有标签的列表
    # print (soup.findAll('div', class_='form-group'))
    # 返回
    # print (soup.select('.container-fluid'))
    # print (soup.select('.container-fluid > div > label')[0].string)
    print (soup.select('nav > div > div > ul > li > a')[0]['href'])







if __name__ == "__main__":
    doIt()
    print ("success")
