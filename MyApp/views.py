#!/usr/bin/python3
# encoding:utf-8
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect


def home_page(request):
    pass
    return render(request, 'home_page.html')


def working_data_download(request):
    return render(request, 'download_working_data.html')