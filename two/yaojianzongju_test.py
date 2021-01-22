# coding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import io
import json
import codecs

# Use-Agent
url = "http://scxk.nmpa.gov.cn:81/xk/"


def doIt():
    # 百度翻译API
    # UA 伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36'
    }
    params = {
        '': ''
    }
    response = requests.get(url=url, params=params, headers=headers)
    call_str = response.text
    fileName = "huangzhuangpin.html"
    with codecs.open(fileName, "w", encoding='utf-8') as fp:
        fp.write(call_str)
    print (call_str)


if __name__ == "__main__":
    doIt()
    print ("success")
