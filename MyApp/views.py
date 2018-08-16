#!/usr/bin/python3
# encoding:utf-8
from __future__ import unicode_literals

import configparser
from django.shortcuts import render
from django.http import HttpResponseRedirect
from threading import Thread
import os
import csv
from .crawler.zhaopin_list import search_result
# from urllib.parse import quote
import time
import math


def run_search_person_crawler(in_num):
    try:
        # 646a6bf9d3fb4bd9b1b68ef58b4711e3
        ini_path = '/Users/lichen/Documents/PycharmProjects/home_web/MyApp/config.ini'
        config = configparser.ConfigParser()
        config.read(ini_path)
        for x in range(0, int(math.ceil(int(in_num)/30))):
            config.set("conf", "start_page", str(x))
            config.write(open(ini_path, "w"))
            time.sleep(1)
            search_result()
    except Exception as e:
        print(e)


def run_search_ddwr_crawler():
    os.system(
        'python3 /Users/lichen/Documents/PycharmProjects/home_web/MyApp/crawler/company_search_people.py ' + input_name2 + ' ' + input_num2 +
        ' ' + input_code2)
    # 646a6bf9d3fb4bd9b1b68ef58b4711e3


def home_page(request):
    if 'pc_username' in request.COOKIES:
        global config, ini_path
        try:
            input_num = request.POST['input_num']
            input_code = request.POST['input_code']
            select_radio = request.POST['radio_group']
            ini_path = '/Users/lichen/Documents/PycharmProjects/home_web/MyApp/config.ini'
            config = configparser.ConfigParser()
            config.read(ini_path)
            config.set("conf", "at_code", str(input_code))
            config.set("conf", "person_number", str(input_num))
            if select_radio == 'qc':
                config.set("conf", "choose_num", str(1))
                config.write(open(ini_path, "w"))
                run_search_person_crawler(in_num=input_num)
                # t = Thread(target=run_search_person_crawler, args=(input_num, input_code, input_select))
                # t.start()
            elif select_radio == 'qa':
                config.set("conf", "choose_num", str(2))
                config.write(open(ini_path, "w"))
                run_search_person_crawler(in_num=input_num)
                # t = Thread(target=run_search_person_crawler, args=(input_num, input_code, input_select))
                # t.start()
        except:
            pass

        return render(request, 'home_page.html')
    else:
        return HttpResponseRedirect('/login/')


def ddwr(request):
    if 'pc_username' in request.COOKIES:
        global input_name2, input_num2, input_code2
        try:
            input_name2 = request.POST['input_name']
            input_num2 = request.POST['input_num']
            input_code2 = request.POST['input_code']
            t = Thread(target=run_search_ddwr_crawler)
            t.start()
        except:
            pass
        return render(request, 'ddwr.html')
    else:
        return HttpResponseRedirect('/login/')


def working_data_download(request):
    if 'pc_username' in request.COOKIES:
        return render(request, 'download_working_data.html')
    else:
        return HttpResponseRedirect('/login/')
