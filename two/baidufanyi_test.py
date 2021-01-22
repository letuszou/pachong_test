# coding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import io
import json

# Use-Agent
url = "https://fanyi.baidu.com/sug"


def doIt():
    # 百度翻译API
    # UA 伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36'
    }
    kw = raw_input("enter a word：")
    data = {
        "kw": kw
    }
    response = requests.post(url, data=data, headers=headers)
    call_json = response.json()
    print unicode(str(call_json), 'unicode_escape')


if __name__ == "__main__":
    doIt()
    print ("success")
