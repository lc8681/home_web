# coding=utf-8
import configparser
import json
import requests
import csv
from tqdm import tqdm
from urllib.parse import quote
import time
from MyApp.main import path


def search_result():
    # url
    global res, filename, datalist
    ini_path = path
    config = configparser.ConfigParser()
    config.read(ini_path)
    start_page = config.get("conf", "start_page")
    at_code = config.get("conf", "at_code")
    choose = config.get("conf", "choose_num")
    person_number = config.get("conf", "person_number")
    url_qc = 'https://rdapi.zhaopin.com/custom/search/resumeListV2?_=1533638160529'
    url_qa = 'https://rdapi.zhaopin.com/custom/search/resumeListV2?_=1533543771973'
    # postdata部分
    data_qc = json.dumps({
        "start": int(start_page),
        "rows": 30,
        "S_DISCLOSURE_LEVEL": 2,
        "S_EXCLUSIVE_COMPANY": "天津红日康仁堂药品销售有限公司;北京康仁堂制药有限公司",
        "S_EDUCATION": "5,1",
        "S_BIRTH_YEAR": "1988,1998",
        "S_MAJOR_NAME_ALL": "药学;药物制剂;制药工程;中药学;中药资源与开发",
        "S_DATE_MODIFIED": "180507,180807",
        "S_DESIRED_SALARY": "0400106000;0600108000",
        "S_DESIRED_CITY": "530",
        "S_ENGLISH_RESUME": "1",
        "isrepeat": 1,
        "sort": "complex"
    })
    data_qa = json.dumps({
        "start": int(start_page),
        "rows": 30,
        "S_DISCLOSURE_LEVEL": 2,
        # "S_EXCLUSIVE_COMPANY": "天津红日康仁堂药品销售有限公司;北京康仁堂制药有限公司",
        "S_EDUCATION": "4,1",
        "S_GENDER": "1",
        "S_BIRTH_YEAR": "1988,1998",
        "S_MAJOR_NAME_ALL": "中药学",
        "S_DATE_MODIFIED": "180507,180807",
        "S_DESIRED_SALARY": "0400106000;0600108000",
        "S_DESIRED_CITY": "530",
        "S_ENGLISH_RESUME": "1",
        "isrepeat": 1,
        "sort": "complex"
    })
    # header部分的配置
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
        'Host': 'rdapi.zhaopin.com',
        'Referer': 'https://rd5.zhaopin.com/custom/searchv2/result',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Content-Type': 'text/plain',
        'zp-route-meta': 'uid=695933625,orgid=27963463',
        'Origin': 'https://rd5.zhaopin.com',

    }
    # cookies部分的配置
    Login_Data = {}
    Login_Data['at'] = str(at_code)
    if choose == str(1):
        filename = '[qc-' + str(person_number) + '人]' + time.strftime("%Y-%m-%d %H:%M", time.localtime()) + '.csv'
        out = open(filename, 'a+', newline='')
        csv_write = csv.writer(out, dialect='excel')
        csv_header = ['更新时间', '姓名', '工作年限', '年龄', '现居住地', '期望工作地点', '学历', '毕业学校', '专业', '期望月薪', '目前状况',
                      '期望从事职业', '最近所在公司', '最近所在公司职位', '最近工作描述', 'id', '链接']
        csv_write.writerow(csv_header)
        res = requests.post(url_qc, data_qc, headers, cookies=Login_Data)
        check_json = json.loads(res.text)
        datalist = tqdm(check_json['data']['dataList'])
        for x in datalist:
            try:
                username = x['userName']
            except:
                username = u'无'
            try:
                eduLevel = x['eduLevel']
            except:
                eduLevel = u'无'
            try:
                age = x['age']
            except:
                age = u'无'
            try:
                city = x['city']
            except:
                city = u'无'
            try:
                modifyDate = x['modifyDate']
            except:
                modifyDate = u'无'
            try:
                desiredSalary = x['desiredSalary']
            except:
                desiredSalary = u'无'
            try:
                careerStatus = x['careerStatus']
            except:
                careerStatus = u'无'
            try:
                workYears = x['workYears']
            except:
                workYears = u'无'
            try:
                jobType = x['jobType']
            except:
                jobType = u'无'
            try:
                desireCity = x['desireCity']
            except:
                desireCity = u'无'
            try:
                major = x['major']
            except:
                major = u'无'
            id = x['id']
            t = x['t']
            k = x['k']
            try:
                companyName = x['lastJobDetail']['companyName']
            except:
                companyName = u'无'
            try:
                jobName = x['lastJobDetail']['jobName']
            except:
                jobName = u'无'
            try:
                description = x['lastJobDetail']['description']
            except:
                description = u'无'
            try:
                school_schoolName = x['schoolDetail']['schoolName']
            except:
                school_schoolName = u'无'
            resume_url = 'https://rd5.zhaopin.com/resume/detail?keyword=&resumeNo=' + quote(id, 'utf-8') + '_1_1%3B' + quote(k, 'utf-8') + '%3B' + quote(t, 'utf-8') + '&openFrom=1'
            information = [modifyDate, username, workYears, age, city, desireCity, eduLevel, school_schoolName, major,
                           desiredSalary, careerStatus, jobType, companyName, jobName, description, id, resume_url]
            csv_write.writerow(information)
            time.sleep(3)
    elif choose == str(2):
        filename = '[qa-' + str(person_number) + '人]' + time.strftime("%Y-%m-%d %H:%M", time.localtime()) + '.csv'
        out = open(filename, 'a+', newline='')
        csv_write = csv.writer(out, dialect='excel')
        csv_header = ['更新时间', '姓名', '工作年限', '年龄', '现居住地', '期望工作地点', '学历', '毕业学校', '专业', '期望月薪', '目前状况',
                      '期望从事职业', '最近所在公司', '最近所在公司职位', '最近工作描述', 'id', '链接']
        csv_write.writerow(csv_header)
        res = requests.post(url_qa, data_qa, headers, cookies=Login_Data)
        check_json = json.loads(res.text)
        datalist = tqdm(check_json['data']['dataList'])
        for x in datalist:
            try:
                username = x['userName']
            except:
                username = u'无'
            try:
                eduLevel = x['eduLevel']
            except:
                eduLevel = u'无'
            try:
                age = x['age']
            except:
                age = u'无'
            try:
                city = x['city']
            except:
                city = u'无'
            try:
                modifyDate = x['modifyDate']
            except:
                modifyDate = u'无'
            try:
                desiredSalary = x['desiredSalary']
            except:
                desiredSalary = u'无'
            try:
                careerStatus = x['careerStatus']
            except:
                careerStatus = u'无'
            try:
                workYears = x['workYears']
            except:
                workYears = u'无'
            try:
                jobType = x['jobType']
            except:
                jobType = u'无'
            try:
                desireCity = x['desireCity']
            except:
                desireCity = u'无'
            try:
                major = x['major']
            except:
                major = u'无'
            id = x['id']
            t = x['t']
            k = x['k']
            try:
                companyName = x['lastJobDetail']['companyName']
            except:
                companyName = u'无'
            try:
                jobName = x['lastJobDetail']['jobName']
            except:
                jobName = u'无'
            try:
                description = x['lastJobDetail']['description']
            except:
                description = u'无'
            try:
                school_schoolName = x['schoolDetail']['schoolName']
            except:
                school_schoolName = u'无'
            resume_url = 'https://rd5.zhaopin.com/resume/detail?keyword=&resumeNo=' + quote(id, 'utf-8') + '_1_1%3B' + quote(k, 'utf-8') + '%3B' + quote(t, 'utf-8') + '&openFrom=1'
            information = [modifyDate, username, workYears, age, city, desireCity, eduLevel, school_schoolName, major,
                           desiredSalary, careerStatus, jobType, companyName, jobName, description, id, resume_url]
            csv_write.writerow(information)
            time.sleep(3)

if __name__ == '__main__':
    search_result()

