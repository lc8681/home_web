#!/usr/bin/python3
# encoding:utf-8
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect


def home_page(request):
    try:
        select_radio = request.POST['radio_group']
        input_num = request.POST['input_num']
        input_code = request.POST['input_code']
        print(select_radio, input_num, input_code)
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