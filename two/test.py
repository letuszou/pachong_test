# coding=utf-8
import requests
import io

url = 'https://tool.letuszou.top/'


def doIt():
    index = 10000
    for i in range(10000):
        print (str('index = %s' % (str(i))))
        import time
        time.sleep(1)
        get_page()


def get_page():
    response = requests.get(url)
    page_text = response.text
    # print (page_text)
    #     fp.write(page_text)


if __name__ == '__main__':
    doIt()
    print ('success')
