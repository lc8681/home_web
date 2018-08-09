# coding=utf-8
import json
import requests
import csv
from tqdm import tqdm
from urllib.parse import quote
import time
import math


def search_result(input_name, start_page, at_code):
    # url
    global res, filename, datalist
    url = 'https://rdapi.zhaopin.com/custom/search/resumeListV2?_=1533721400702'
    # postdata部分
    data = json.dumps({
        "start": int(start_page),
        "rows": 30,
        "S_DISCLOSURE_LEVEL": 2,
        "S_KEYWORD_JOBDESC": "生产;质量;采购;qa;qc;gmp;炮制;提取;包装;制剂;配方颗粒",
        "S_COMPANY_NAME_LAST": input_name,
        "S_DATE_MODIFIED": "180508,180808",
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
    res = requests.post(url, data, headers, cookies=Login_Data)
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

        # # resume_name = x['name']
        # username = x['userName']
        # # jobTitle = x['jobTitle']
        # eduLevel = x['eduLevel']
        # # gender = x['gender']
        # # isFemale = x['isFemale']
        # age = x['age']
        # city = x['city']
        # # cityId = x['cityId']
        # modifyDate = x['modifyDate']
        # desiredSalary = x['desiredSalary']
        # careerStatus = x['careerStatus']
        # workYears = x['workYears']
        # school = x['school']
        # # employment = x['employment']
        # jobType = x['jobType']
        # desireCity = x['desireCity']
        # major = x['major']
        # id = x['id']
        # t = x['t']
        # k = x['k']
        # # beginDate = x['lastJobDetail']['beginDate']
        # # endDate = x['lastJobDetail']['endDate']
        # companyName = x['lastJobDetail']['companyName']
        # # department = x['lastJobDetail']['department']
        # jobName = x['lastJobDetail']['jobName']
        # # salary = x['lastJobDetail']['salary']
        # # industry = x['lastJobDetail']['industry']
        # # profession = x['lastJobDetail']['profession']
        # # companyType = x['lastJobDetail']['companyType']
        # description = x['lastJobDetail']['description']
        # # school_beginDate = x['schoolDetail']['beginDate']
        # # school_endDate = x['schoolDetail']['endDate']
        # school_schoolName = x['schoolDetail']['schoolName']
        # # school_major = x['schoolDetail']['major']
        # # school_degree = x['schoolDetail']['degree']
        resume_url = 'https://rd5.zhaopin.com/resume/detail?keyword=&resumeNo=' + quote(id,
                                                                                        'utf-8') + '_1_1%3B' + quote(k,
                                                                                                                     'utf-8') + '%3B' + quote(
            t, 'utf-8') + '&openFrom=1'
        information = [modifyDate, username, workYears, age, city, desireCity, eduLevel, school_schoolName, major,
                       desiredSalary, careerStatus, jobType, companyName, jobName, description, resume_url]
        csv_write.writerow(information)
        time.sleep(3)


if __name__ == '__main__':
    input_name = input("一、请输入要搜索的公司的名称，用英文分号隔开，例如：广东一方;江阴天江\n")
    while 1:
        rows = input("二、要抓取多少条数据？搜索公司：" + input_name + "\n")
        if rows.isdigit():
            try:
                break
            except UnicodeDecodeError:
                print("\033[0;31;47m\t####### 请输入纯数字！！！#######\033[0m\n")
        else:
            print("\033[0;31;47m\t####### 请输入纯数字！！！#######\033[0m\n")

    filename = time.strftime('[定点挖掘:(' + input_name + ')]' + "%Y-%m-%d %H-%M-%S", time.localtime()) + '.csv'
    out = open(filename, 'a+', newline='')
    csv_write = csv.writer(out, dialect='excel')
    csv_header = ['更新时间', '姓名', '工作年限', '年龄', '现居住地', '期望工作地点', '学历', '毕业学校', '专业', '期望月薪', '目前状况',
                  '期望从事职业', '最近所在公司', '最近所在公司职位', '最近工作描述', '链接']
    csv_write.writerow(csv_header)
    while 1:
        try:
            at_code = input("二、输入验证码，需手动登录后用浏览器查看然后输入到这里\n")
            # 220f426b1b264afbb51eb3e19ecaff0a
            for n in range(0, int(math.ceil(int(rows)/30))):
                search_result(input_name=input_name, start_page=n, at_code=at_code)

            break
        except Exception as e:
            print("\033[0;31;47m\t错误码：\033[0m\n" + str(e))
            print("\033[0;31;47m\t####### 验证码不正确请重新输入！！！#######\033[0m\n")
