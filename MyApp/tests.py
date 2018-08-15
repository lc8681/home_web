from django.test import TestCase
import requests

def get_zlzp_cookies():
    url = 'https://passport.zhaopin.com/org/login'
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #     'Accept-Encoding': 'gzip, deflate, br',
    #     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    #     'Content-Type': 'text/plain',
    #     'zp-route-meta': 'uid=695933625,orgid=27963463',
    #     'Origin': 'https://rd5.zhaopin.com',
    #
    # }
    res = requests.get(url=url)
    cookies = res.cookies.get_dict()
    print(cookies)


if __name__ == '__main__':
    get_zlzp_cookies()