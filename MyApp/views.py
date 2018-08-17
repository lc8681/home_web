#!/usr/bin/python3
# encoding:utf-8
from __future__ import unicode_literals
from MyApp.main import path, qc_file_path, qa_file_path, ddwj_file_path
import configparser
from django.shortcuts import render
from django.http import HttpResponseRedirect
from threading import Thread
from django.utils.datastructures import MultiValueDictKeyError
import os
from .crawler.zhaopin_list import search_result
from .crawler.company_search_people import ddwj_search_result
from wechat_warnning import wechat_warnning
import time
import math


def run_search_person_crawler(in_num):
    ini_path = path
    config = configparser.ConfigParser()
    config.read(ini_path)
    try:
        start = time.time()
        for x in range(0, int(math.ceil(int(in_num)/30))):
            config.set("conf", "start_page", str(x))
            config.write(open(ini_path, "w"))
            time.sleep(0.5)
            search_result()
        end = time.time()
        run_time_s = end-start
        run_time_m = float(run_time_s) / 60
        wechat_warnning(text='智联-搜人成功，请前往"数据下载"页面查找报表', desp='用时：' + str(math.ceil(run_time_m)) + '分钟')
    except Exception as e:
        wechat_warnning(text='智联-搜人失败，请检查验证码是否正确', desp=str([e]))


def run_search_ddwr_crawler(in_num):
    ini_path = path
    config = configparser.ConfigParser()
    config.read(ini_path)
    try:
        start = time.time()
        for x in range(0, int(math.ceil(int(in_num) / 30))):
            config.set("conf_2", "start_page", str(x))
            config.write(open(ini_path, "w"))
            time.sleep(0.5)
            ddwj_search_result()
        end = time.time()
        run_time_s = end - start
        run_time_m = float(run_time_s) / 60
        wechat_warnning(text='智联定点挖掘成功，请前往"数据下载"页面查找报表', desp='用时：' + str(math.ceil(run_time_m)) + '分钟')
    except Exception as e:
        wechat_warnning(text='智联定点挖掘失败，请检查验证码是否正确', desp=str([e]))


def home_page(request):
    if 'pc_username' in request.COOKIES:
        global config, ini_path
        try:
            input_num = request.POST['input_num']
            input_code = request.POST['input_code']
            select_radio = request.POST['radio_group']
            ini_path = path
            config = configparser.ConfigParser()
            config.read(ini_path)
            config.set("conf", "at_code", str(input_code))
            config.set("conf", "person_number", str(input_num))
            if select_radio == 'qc':
                config.set("conf", "choose_num", str(1))
                config.write(open(ini_path, "w"))
                t = Thread(target=run_search_person_crawler, args=(input_num,))
                t.start()
            elif select_radio == 'qa':
                config.set("conf", "choose_num", str(2))
                config.write(open(ini_path, "w"))
                t = Thread(target=run_search_person_crawler, args=(input_num,))
                t.start()
        except:
            pass

        return render(request, 'home_page.html')
    else:
        return HttpResponseRedirect('/login/')


def ddwr(request):
    if 'pc_username' in request.COOKIES:
        global input_name2, input_num2, input_code2
        ini_path = path
        config = configparser.ConfigParser()
        config.read(ini_path)
        jd = config.get("conf_2", "jd")
        try:
            input_name2 = request.POST['input_name']
            input_num2 = request.POST['input_num']
            input_code2 = request.POST['input_code']
            ini_path = path
            config = configparser.ConfigParser()
            config.read(ini_path)
            config.set("conf_2", "company_name", str(input_name2))
            config.set("conf_2", "input_num", str(input_num2))
            config.set("conf_2", "at_code", str(input_code2))
            config.write(open(ini_path, "w"))
            t = Thread(target=run_search_ddwr_crawler, args=(input_num2,))
            t.start()
        except:
            pass
        return render(request, 'ddwr.html', {'jd': jd})
    else:
        return HttpResponseRedirect('/login/')


def qc_files():
    os.chdir(qc_file_path)
    getpath = os.getcwd()
    # 找出此路径下的所有文件
    filedir = os.listdir(getpath)
    # 对所有文件按名字升序排列
    filedir.sort(key=lambda fn: os.path.basename(getpath + '//' + fn))
    filedir.reverse()
    return filedir


def qa_files():
    os.chdir(qa_file_path)
    getpath = os.getcwd()
    # 找出此路径下的所有文件
    filedir = os.listdir(getpath)
    # 对所有文件按名字升序排列
    filedir.sort(key=lambda fn: os.path.basename(getpath + '//' + fn))
    filedir.reverse()
    return filedir


def ddwj_files():
    os.chdir(ddwj_file_path)
    getpath = os.getcwd()
    # 找出此路径下的所有文件
    filedir = os.listdir(getpath)
    # 对所有文件按名字升序排列
    filedir.sort(key=lambda fn: os.path.basename(getpath + '//' + fn))  # 按名称排序
    filedir.reverse()  # 倒序排列
    return filedir


def working_data_download(request):
    if 'pc_username' in request.COOKIES:
        try:
            qc_files()
            qa_files()
            ddwj_files()
            try:
                select_qc_files = request.POST["qc_files"]
                qc_files_url = "http://172.31.38.234:8000/android/beta/" + select_qc_files
                return HttpResponseRedirect(qc_files_url)
            except MultiValueDictKeyError:
                pass

            try:
                select_qa_files = request.POST["qa_files"]
                qa_files_url = "http://172.31.38.234:8000/android/offical/" + select_qa_files
                return HttpResponseRedirect(qa_files_url)
            except MultiValueDictKeyError:
                pass

            try:
                select_ddwj_files = request.POST["ddwj_files"]
                ddwj_files_url = "http://172.31.38.234:8000/ios/beta/" + select_ddwj_files
                return HttpResponseRedirect(ddwj_files_url)
            except MultiValueDictKeyError:
                pass
            return render(request, 'download_working_data.html',
                          {"qc_files_list": qc_files(), "qa_files_list": qa_files(), "ddwj_files_list": ddwj_files()})

        except MultiValueDictKeyError:
            pass
        return render(request, 'download_working_data.html',
                      {"qc_files_list": qc_files(), "qa_files_list": qa_files(), "ddwj_files_list": ddwj_files()})
    else:
        return HttpResponseRedirect('/login/')
