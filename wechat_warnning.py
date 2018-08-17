#!/usr/bin/python3
# encoding:utf-8
import requests


def wechat_warnning(text, desp):
    url = 'https://sc.ftqq.com/SCU27405Ta0734d924dc4507ef4dd54d4e32dd9855b12d1de9133c.send?text=' + text + '&desp=' + desp
    requests.get(url=url)