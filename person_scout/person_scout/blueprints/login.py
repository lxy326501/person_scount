#!/usr/bin/env python
# coding: utf-8

import json
from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash

from person_scout.extensions import csrf
from person_scout.models.user import User
from person_scout.forms.login import LoginForm

login_bp = Blueprint('login', __name__)

# 利用form表单获取登录信息并验证，设置权限、登录session 跳转到event/event_manage.html
@login_bp.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('collectionWuxi.user_list'))

    form = LoginForm()
    if form.validate_on_submit():
        account = form.account.data
        password = form.password.data
        remember = form.remember.data

        user_info = User.login_auth(account, password)
        if type(user_info) != str:
            login_user(user_info, remember)
            return redirect(url_for('collectionWuxi.user_list'))
        else:
            print (type(user_info))
            flash(user_info, 'warning')
            print("haha")

    return render_template('login/login.html', form_login=form)

# 登出
@login_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout success.', 'info')
    return redirect(url_for('login.login'))

# 删除用户 删除user对应数据，并刷新页面
@csrf.exempt
@login_bp.route('/updpassword',  methods=['GET', 'POST'])
@login_required
def upd_password():
    new_pw = request.values['new_pw']
    old_pw = request.values['old_pw']

    result = User.change_password(current_user.user_info['user_account'], old_pw, new_pw)
    if result == False:
        return {
            'code': 0,
            'data': 'error'
        }
    return json.dumps({
        'code': 1,
        'data': 'success'
    })