#!/usr/bin/python3
# encoding:utf-8
import requests


def wechat_warnning(text, desp):
    url = "https://pushbear.ftqq.com/sub?sendkey=5193-01ba5463c07c33c916fb6f1118a12369&text=" + text + "&desp=" + desp
    requests.get(url=url)