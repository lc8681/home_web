# coding=utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.db import connection
from django.contrib.auth.hashers import check_password


# 登录
def login_page(request):
    if 'pc_username' in request.COOKIES:
        return HttpResponseRedirect('/home_page/')
    else:
        if request.method == 'POST':
            try:
                # 登录相关
                username = request.POST['username']
                password = request.POST['password']
                cursor = connection.cursor()
                cursor.execute("select password from auth_user where username=%s", [username])
                pw = cursor.fetchone()[0]
                # 获取的表单数据与数据库进行比较
                if check_password(password, pw) is True:
                    # 比较成功，跳转index
                    response = HttpResponseRedirect('/home_page/')
                    # 将username写入浏览器cookie,失效时间为3600
                    response.set_cookie('pc_username', username, 360000)
                    return response
                else:
                    # 比较失败，还在login
                    login_false = True
                    return render_to_response('login.html', {'login_false': login_false})
            except:
                pass
        return render_to_response('login.html')

# 退出
# def logout(requset):
#     response = HttpResponse('logout !!')
#     # 清理cookie里保存username
#     response.delete_cookie('username')
#     return response
