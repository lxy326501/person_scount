#!/usr/bin/env python
# coding: utf-8

from flask_login import current_user
from werkzeug.security import check_password_hash, generate_password_hash
from bson import ObjectId

from person_scout.models import mongo
from person_scout.extensions import login_manager

'''
user_account
user_true_name
user_phone
user_password
user_permission
'''
class User():
    col = mongo.db.user

    @staticmethod
    def login_auth(user_account, user_password):
        user_info = User.col.find_one({'user_account': user_account})
        col = mongo.db.purchase
        print(col)

        if user_info:
            if check_password_hash(user_info['user_password'], user_password):
                user_info['_id'] = str(user_info['_id'])
                user_info['is_active'] = True
                return LoginManage(user_info)
            else:
                return 'Invalid username or password.'
        else:
            return 'No account.'

    @staticmethod
    def change_password(user_account, old_pw, new_pw):
        user_info = User.col.find_one({'user_account': user_account})
        if user_info:
            if check_password_hash(user_info['user_password'], old_pw):
                new_pw = generate_password_hash(new_pw)
                User.col.update({'_id': user_info['_id']}, {'$set':{'user_password': new_pw}})
                current_user.user_info['user_password'] = new_pw
                user_info['user_password'] = new_pw
                user_info['_id'] = str(user_info['_id'])
                user_info['is_active'] = True
                return LoginManage(user_info)
            else:
                return False
        else:
            return 'No account.'

class LoginManage(dict):

    def __init__(self, user_info):
        self.active = user_info.get('active', True)
        self.authenticated = user_info.get('authenticated', True)
        self.anonymous = user_info.get('anonymous', False)
        self.user_permission = user_info['user_permission']
        self.user_info = user_info

    def get_id(self):
        return self.user_info['_id']

    @property
    def is_active(self):
        return self.active

    @property
    def is_authenticated(self):
        return self.authenticated

    @property
    def is_anonymous(self):
        return self.anonymous

    @login_manager.user_loader
    def load_user(user_id):
        user_info = User.col.find_one({'_id': ObjectId(user_id)})
        if user_info:
            user_info['_id'] = str(user_info['_id'])
        else:
            return None
        return LoginManage(user_info)