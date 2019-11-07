#!/usr/bin/env python
# coding: utf-8

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length

# password + account + remember + submit(登录)
class LoginForm(FlaskForm):
    account = StringField('', validators=[DataRequired(), Length(1, 20)], render_kw={'class': 'login-input form-control', 'placeholder': "请输入账号"})
    password = PasswordField('', validators=[DataRequired(), Length(1, 128)], render_kw={'class': 'login-input form-control', 'placeholder': "请输入密码"})
    # verify_code = StringField(label="验证码", validators=[ DataRequired(), ] )
    remember = BooleanField('记住登录')
    submit = SubmitField('登录', render_kw={'class': 'col-6'})