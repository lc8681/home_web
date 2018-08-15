#!/usr/bin/python3
# encoding:utf-8
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect
from threading import Thread
import os



def run_search_person_crawler():
    os.system(
        'python3 /Users/lichen/Documents/PycharmProjects/home_web/MyApp/crawler/zhaopin_list.py ' + input_select + ' ' + input_num +
        ' ' + input_code)


def run_search_ddwr_crawler():
    os.system(
        'python3 /Users/lichen/Documents/PycharmProjects/home_web/MyApp/crawler/company_search_people.py ' + input_name2 + ' ' + input_num2 +
        ' ' + input_code2)


def home_page(request):
    if 'pc_username' in request.COOKIES:
        global input_select, input_num, input_code
        try:
            select_radio = request.POST['radio_group']
            if select_radio == 'qc':
                input_select = str(1)
            elif select_radio == 'qa':
                input_select = str(2)
            input_num = request.POST['input_num']
            input_code = request.POST['input_code']
            t = Thread(target=run_search_person_crawler)
            t.start()
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
