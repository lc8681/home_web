#!/usr/bin/python3
# encoding:utf-8
from __future__ import unicode_literals
from django.shortcuts import render
import time
from threading import Thread
import os
from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect


def run_crawler():
    os.system('python E:\PycharmProjects\home_web\MyApp\crawler\zhaopin_list.py ' + input_select + ' ' + input_num +
              ' ' + input_code)


def home_page(request):
    global input_select, input_num, input_code
    try:
        select_radio = request.POST['radio_group']
        if select_radio == 'qc':
            input_select = str(1)
        elif select_radio == 'qa':
            input_select = str(2)
        input_num = request.POST['input_num']
        input_code = request.POST['input_code']
        # t = Thread(target=run_crawler)
        # t.start()
    except:
        pass
    return render(request, 'home_page.html')


def ddwr(request):
    try:
        input_name = request.POST['input_name']
        input_num = request.POST['input_num']
        input_code = request.POST['input_code']
        print(input_name, input_num, input_code)
    except:
        pass
    return render(request, 'ddwr.html')


def working_data_download(request):
    return render(request, 'download_working_data.html')