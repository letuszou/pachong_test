# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import io
# Use-Agent
# url = "https://www.sogou.com/"
url = "https://www.sogou.com/web"


def doIt():
    # UA 伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36'
    }
    _query = raw_input("enter a word：")
    param = {
        "query": _query
    }
    response = requests.get(url, params=param, headers=headers)
    page_text = response.text
    fileName = "%s.html" % _query
    with io.open(fileName, "w", encoding="utf-8") as fp:
        fp.write(page_text)
    print (fileName)


if __name__ == "__main__":
    doIt()
    print ("success")
