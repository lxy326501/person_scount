#!/usr/bin/env python
# coding: utf-8
import json
import datetime
from time import strftime
from bson import json_util,ObjectId
from flask import Blueprint, render_template, request, flash, redirect, url_for ,json
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash
from person_scout import csrf
from person_scout.decorators import permission_required
from person_scout.models.user import User

user_bp = Blueprint('usermanage', __name__)


# 仅管理员用户可见，从mongo中user获取用户列表并展示。需要设置修改/添加用户表单，体哦啊转到user/user_manage.html
@user_bp.route('/')
@login_required
def user_list():
    columns = [
        {"field": 'state', 'checkbox': True, 'hidden': True, },
        {"field": "user_account", "title": "账号", "sortable": False, },
        {"field": "user_true_name", "title": "姓名", "sortable": False, },
        {"field": "user_phone", "title": "用户电话", "sortable": False, },
        {"field": "user_create_time", "title": "注册时间", "sortable": False, },
        {"field": "details", "title": "操作", "sortable": False, },
    ]
    data = []
    col = User.col
    for record in col.find():
        record['details'] = '<div><a class=\"RoleOf btn\" data-toggle=\"modal\" data-target=\"#edit\" style=\"color: #25ccde; \">修改</a></div>'
        record['_id'] = str(record['_id'])
        data.append(record)
    return render_template('user/user_manage.html', columns=columns, data=data)


# 修改用户 修改user表，并刷新页面
@user_bp.route('/upduser', methods=['GET', 'POST'])
@permission_required(['admin'])
@csrf.exempt
@login_required
def upd_user():
    data = request.values
    print(data['_id'])
    user_account = request.args.get('user_account')
    print(user_account)
    user_true_name = request.args.get('user_true_name')
    print(user_true_name)
    user_phone = request.args.get('user_phone')
    print(user_phone)
    new = request.args.get('user_password')
    new_pw = generate_password_hash(new)
    User.col.update(
        {"_id": ObjectId(data['_id'])},

      {"$set": {"user_account": user_account,"user_true_name": user_true_name,"user_phone": user_phone,
                  "user_password": new_pw}},
    )
    return redirect(url_for('usermanage.user_list'))



# 添加用户 ajax 插入user，并刷新页面
@user_bp.route('/adduser', methods=['GET', 'POST'])
@permission_required(['admin'])
@login_required
def add_user():
    admin = request.values
    print(admin)
    print(admin['selectTest'])
    event_create_user = current_user.user_info
    print(event_create_user)
    now = datetime
    ntime = strftime('%Y-%m-%d %H:%M:%S')
    print(ntime)
    new = request.values.get('user_password')
    new_pw = generate_password_hash(new)
    co = User.col.find({"user_account": event_create_user['user_account']})
    for i in co:
        user_create_user_id = i['_id']
        print(user_create_user_id)
        newtask = {
            'user_account': request.values.get('user_account'),
            'user_true_name': request.values.get('user_true_name'),
            'user_phone': request.values.get('user_phone'),
            'user_create_time': ntime,
            'user_password': new_pw,
            'user_permission':admin['selectTest'],
            'user_create_user_id':str(user_create_user_id)
        }
        col = User.col
        col.insert(newtask)
        return redirect(url_for('usermanage.user_list'))


# 删除用户 删除user对应数据，并刷新页面
@user_bp.route('/deluser', methods=['GET', 'POST'])
@permission_required(['admin'])
@csrf.exempt
@login_required
def delete_user():
    if request.method == 'POST':
        event_id = request.values.get('info[0][_id]')
        print(event_id)
        user_id = ObjectId(event_id)
        data = User.col.find({"_id": user_id})
        raw_posts = [x for x in data]
        for i in raw_posts:
            id = str(i['user_create_user_id'])
            event_create_user = current_user.user_info
            co = User.col.find({"user_account": event_create_user['user_account']})
            for i in co:
                #当前用户id
                person_id = str(i['_id'])
                print(id)
                print(person_id)
                if id == person_id:
                    User.col.remove({"_id":user_id})
                    flash('删除成功.', 'success')
                    return 'success!'
                else:
                    flash('失败.', 'success')
                    return 'failed!'



