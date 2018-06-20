import pymysql
from flask import Blueprint, render_template, Flask, request, redirect, session
from code_count.utils.md5 import md5
from code_count.utils import helper

account = Blueprint('account', __name__)


@account.route('/login/', methods=['GET', 'POST'])
def login():
    '''
    登陆
    :return:
    '''
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get('user')
    password = request.form.get('pwd')

    pwd_md5 = md5(password)

    data = helper.fetch_one("select id,nickname from userinfo where user=%s and pwd =%s", (username, pwd_md5))

    if not data:
        return render_template('login.html', error='用户名密码错误')

    # session['user_info'] = data
    session['user_info'] = {'id': data['id'], 'nickname': data['nickname']}

    return redirect('/home/')


@account.route('/logout/')
def logout():
    '''
    注销
    :return:
    '''
    if 'user_info' in session:
        del session['user_info']

    return redirect('/login')


@account.route('/register/', methods=['GET', 'POST'])
def register():
    '''
    注册
    :return:
    '''
    row = ''
    if request.method == "POST":
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        name = request.form.get('name')
        pwd_md5 = md5(pwd)
        ret = helper.fetch_all('SELECT * FROM userinfo WHERE user=%s', [user])

        if ret:
            row = '用户名重复请重新更换用户名'
        else:
            helper.insert("insert into userinfo(user,pwd,nickname)values(%s,%s,%s)", [user, pwd_md5, name])
            row = '恭喜你注册成功'
    return render_template('register.html', row=row)
