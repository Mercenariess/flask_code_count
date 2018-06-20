from flask import Blueprint, render_template, Flask, request, redirect,session
import os
import uuid
from ..utils import helper


ind = Blueprint('ind', __name__)

@ind.before_request
def process_request():
    if not session.get("user_info"):
        return redirect("/login")
    return None


@ind.route('/home/')
def home():
    return render_template('home.html')




@ind.route('/user_list/')
def user_list():
    code_sum = helper.fetch_all('SELECT sum(line)as num,nickname  FROM userinfo inner JOIN record ON userinfo.id = record.user_id GROUP BY userinfo.id', [])
    print(code_sum, '------********************************')
    data_list = helper.fetch_all("SELECT id,user,nickname FROM userinfo",[])
    #  session['user_info'] = {'id':data['id'],'nickname':data['nickname']}



    # for i in user_id:
    #     q= helper.fetch_all('SELECT line FROM record WHERE user_id=%s',[i])
    #     print(q,'+++++++++++++++++++++++++++++++++++++++')

    return render_template('user_list.html',data_list=data_list,code_sum=code_sum)


@ind.route('/qwer/<int:nid>')
def detail(nid):


    record_list = helper.fetch_all("SELECT id,line,ctime FROM record where user_id=%s", (nid,))
    user_id = helper.fetch_all('SELECT nickname FROM userinfo where id=%s',(nid,))
    user=user_id[0]['nickname']
    print('user',type(user))
    return render_template('index.html',record_list=record_list,user=user)

@ind.route('/upload/',methods=['GET','POST'])
def upload():
    '''
    上传代码
    :return:
    '''
    row = ''
    if request.method == "GET":
        return render_template('upload.html')
    from werkzeug.datastructures import FileStorage

    file_obj = request.files.get('code')

    # 1. 检查上传文件后缀名
    name_ext = file_obj.filename.rsplit('.',maxsplit=1)
    if len(name_ext) != 2:
        row = '请上传zip压缩文件'
        return render_template("demo3.html",row=row)
    if name_ext[1] != 'zip':
        row = "请上传zip压缩文件"
        return render_template("demo3.html", row=row)

    """
    # 2. 接收用户上传文件,并写入到服务器本地.
    file_path = os.path.join("files",file_obj.filename)
    # 从file_obj.stream中读取内容，写入到文件
    file_obj.save(file_path)

    # 3. 解压zip文件
    import shutil
    # 通过open打开压缩文件，读取内容再进行解压。
    shutil._unpack_zipfile(file_path,'xsadfasdfasdf')
    """

    # 2+3, 接收用户上传文件，并解压到指定目录
    import shutil
    target_path = os.path.join('files',str(uuid.uuid4()))
    shutil._unpack_zipfile(file_obj.stream,target_path)

    # 4. 遍历某目录下的所有文件
    # for item in os.listdir(target_path):
    #     print(item)
    total_num = 0
    for base_path,folder_list,file_list in os.walk(target_path):
        for file_name in file_list:
            file_path = os.path.join(base_path,file_name)
            file_ext = file_path.rsplit('.',maxsplit=1)
            if len(file_ext) != 2:
                continue
            if file_ext[1] != 'py':
                continue
            file_num = 0
            with open(file_path,'rb') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    if line.startswith(b'#'):
                        continue
                    file_num += 1
            total_num += file_num
    
    # 获取当前时间
    import datetime
    ctime = datetime.date.today()
    print(total_num,ctime,session['user_info']['id'])

    # import pymysql
    # conn = pymysql.Connect(host='127.0.0.1', user='root', password='123456', database='s9day118', charset='utf8')
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # cursor.execute("select id from record where ctime=%s and user_id=%s",(ctime,session['user_info']['id']))
    # data = cursor.fetchone()
    # cursor.close()
    # conn.close()
    data = helper.fetch_one("select id from record where ctime=%s and user_id=%s",(ctime,session['user_info']['id']))
    if data:
        row ="今天已经上传"
        return render_template("demo3.html", row=row)


    # import pymysql
    # conn = pymysql.Connect(host='127.0.0.1', user='root', password='123456', database='s9day118', charset='utf8')
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # cursor.execute("insert into record(line,ctime,user_id)values(%s,%s,%s)",(total_num,ctime,session['user_info']['id']))
    # conn.commit()
    # cursor.close()
    # conn.close()
    helper.insert("insert into record(line,ctime,user_id)values(%s,%s,%s)",(total_num,ctime,session['user_info']['id']))
    row = "上传成功"
    return render_template("demo3.html", row=row)