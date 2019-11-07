#!/usr/bin/env python
# coding: utf-8
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from bson import ObjectId

from person_scout.models.wuxi import wuxi

collection_wx = Blueprint('collectionWuxi', __name__)


# 从mongo(models的Purchase)中user获取用户列表并展示，跳转到wuxi/collection_untreated.html
@collection_wx.route('/')
@login_required
def user_list():
    columns = [
        {"field": "meta.url", "title": "来源", "sortable": False, },
        {"field": "items.time", "title": "日期", "sortable": False, },
        {"field": "items.title", "title": "标题", "sortable": False, },
        {"field": "details", "title": "操作", "sortable": False, },
    ]
    data = []
    col = wuxi.col
    for record in col.find():
        # print(record)
        record['meta.url'] = '<a class=\"form btn"\ style=\"color: #25ccde;">来源</a>'
        record['details'] = '<a class=\"icon-btn btn\" >详情</button>'
        record['_id'] = str(record['_id'])
        if record['field'] == "null":
            data.append(record)
    return render_template('wuxi/collection_untreated.html', data=data, columns=columns)


# 读取基本信息，从content中读取文章，跳转到collection_detail.html
@collection_wx.route('/collectiondetail')
@login_required
def collection_detail():
    col = wuxi.col
    user_filter = {}
    params = request.args
    # print(params)
    if 'uid' in params:
        user_filter['_id'] = ObjectId(params['uid'])
    cur = col.find(user_filter)
    raw_posts = [x for x in cur]
    posts = []
    # print(raw_posts)
    for post in raw_posts:
        userpost = {
            '_id': post['_id'],
            'url': post['meta']['url'],
            'title': post['items']['title'],
            'time': post['items']['time'],
            'content': post['items']['content'],

        }
        # print(userpost)
        posts.append(userpost)
    # print(posts)
    return render_template('wuxi/collection_detail.html', posts=posts)


@collection_wx.route('/collectionrelated')
@login_required
def collection_related():
    params = request.args
    print(params)
    wuxi.col.update(
        {"_id": ObjectId(params['uid'])},
        {"$set": {"field": "0"}},
    )
    return redirect(url_for('collectionWuxi.user_list'))


@collection_wx.route('/collectionirrelevant')
@login_required
def collection_irrelevant():
    params = request.args
    print(params)
    wuxi.col.update(
        {"_id": ObjectId(params['uid'])},
        {"$set": {"field": "1"}},
    )
    return redirect(url_for('collectionWuxi.user_list'))


# 点击相关刷新页面，主页面变为相关的信息
@collection_wx.route('/collectionrelatedview')
@login_required
def collection_related_view():
    columns = [
        {"field": "meta.url", "title": "来源", "sortable": False, },
        {"field": "items.time", "title": "日期", "sortable": False, },
        {"field": "items.title", "title": "标题", "sortable": False, },
        {"field": "details", "title": "操作", "sortable": False, },
    ]
    data = []
    col = wuxi.col
    for record in col.find():
        # print(record)
        record['meta.url'] = '<a class=\"form btn"\ style=\"color: #25ccde;">来源</a>'
        record['details'] = '<a class=\"icon-btn btn\" >详情</button>'
        record['_id'] = str(record['_id'])
        if record['field'] == "0":
            data.append(record)
    return render_template('wuxi/collection_relevant.html', data=data, columns=columns)


# 点击相关刷新页面，主页面变为不相关的信息
@collection_wx.route('/collectionirrelevantview')
@login_required
def collection_irrelevant_view():
    columns = [
        {"field": "meta.url", "title": "来源", "sortable": False, },
        {"field": "items.time", "title": "日期", "sortable": False, },
        {"field": "items.title", "title": "标题", "sortable": False, },
        {"field": "details", "title": "操作", "sortable": False, },
    ]
    data = []
    col = wuxi.col
    for record in col.find():
        # print(record)
        record['meta.url'] = '<a class=\"form btn"\ style=\"color: #25ccde;">来源</a>'
        record['details'] = '<a class=\"icon-btn btn\" >详情</button>'
        record['_id'] = str(record['_id'])
        if record['field'] == "1":
            data.append(record)
    return render_template('wuxi/collection_irrrelevant.html', data=data, columns=columns)


@collection_wx.route('/collectionirrelevantviews')
@login_required
def collection_irrelevant_views():
    columns = [
        {"field": "meta.url", "title": "来源", "sortable": False, },
        {"field": "items.time", "title": "日期", "sortable": False, },
        {"field": "items.title", "title": "标题", "sortable": False, },
        {"field": "details", "title": "操作", "sortable": False, },
    ]
    data = []
    col = wuxi.col
    for record in col.find():
        # print(record)
        record['meta.url'] = '<a class=\"form btn"\ style=\"color: #25ccde;">来源</a>'
        record['details'] = '<a class=\"icon-btn btn\" >详情</button>'
        record['_id'] = str(record['_id'])
        if record['field'] == "null":
            data.append(record)
    return render_template('wuxi/collection_untreated.html', data=data, columns=columns)
