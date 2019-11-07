#!/usr/bin/env python
# coding: utf-8
from bson import ObjectId
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required


from person_scout.models.Suzhou import Suzhou

collection_sz = Blueprint('collectionSuzhou', __name__)


# 从mongo(models的Purchase)中user获取用户列表并展示，跳转到collection/collection_untreated.html
@collection_sz.route('/')
@login_required
def user_list():
    columns = [
        {"field": "meta.download_slots", "title": "来源", "sortable": False, },
        {"field": "items.time", "title": "日期", "sortable": False, },
        {"field": "items.title", "title": "标题", "sortable": False, },
        {"field": "details", "title": "操作", "sortable": False, },
    ]
    data = []
    col = Suzhou.col
    for record in col.find():
        record['meta.download_slots'] = '<a class=\"form btn"\ style=\"color: #25ccde;">来源</a>'
        record['details'] = '<a class=\"icon-btn btn\" >详情</a>'
        record['_id'] = str(record['_id'])
        if record['field'] == "null":
            data.append(record)

    return render_template('suzhou/collection_untreated.html', columns=columns, data=data)



# 读取基本信息，从content中读取文章，跳转到collection_detail.html
@collection_sz.route('/collectiondetail')
@login_required
def collection_detail():
    col = Suzhou.col
    user_filter = {}
    params = request.args
    print(params)
    if 'uid' in params:
        user_filter['_id'] = ObjectId(params['uid'])
    cur = col.find(user_filter)
    raw_posts = [x for x in cur]
    posts = []
    print(raw_posts)
    for post in raw_posts:
        userpost = {
            'url':post['meta']['url'],
            '_id': post['_id'],
            'title': post['items']['title'],
            'time': post['items']['time'],
            'content': post['items']['content'],
        }
        # print(userpost)
        posts.append(userpost)
    print(posts)
    return render_template('suzhou/collection_detail.html', posts=posts)

# 用标志位判断相关，刷新页面
@collection_sz.route('/collectionrelated')
@login_required
def collection_related():
    params = request.args
    print(params)
    Suzhou.col.update(
        {"_id": ObjectId(params['uid'])},
        {"$set": {"field": "0"}},
    )
    return redirect(url_for('collectionSuzhou.user_list'))


# 用标志位判断相关，刷新页面
@collection_sz.route('/collectionirrelevant')
@login_required
def collection_irrelevant():
    params = request.args
    print(params)
    Suzhou.col.update(
        {"_id": ObjectId(params['uid'])},
        {"$set": {"field": "1"}},
    )
    return redirect(url_for('collectionSuzhou.user_list'))

# 点击相关刷新页面，主页面变为相关的信息
@collection_sz.route('/collectionrelatedview')
@login_required
def collection_related_view():
    columns = [
        {"field": "meta.download_slot", "title": "来源", "sortable": False, },
        {"field": "items.time", "title": "日期", "sortable": False, },
        {"field": "items.title", "title": "标题", "sortable": False, },
        {"field": "details", "title": "操作", "sortable": False, },
    ]
    data = []
    col = Suzhou.col
    for record in col.find():
        # print(record)
        record['meta.download_slot'] = '<a class=\"form btn\" style=\"color: #25ccde; \">来源</button>'
        record[
            'details'] = '<a class=\"icon-btn btn\" >详情</button> '
        record['_id'] = str(record['_id'])
        if record['field'] == "0":
            data.append(record)
    return render_template('suzhou/collection_relevant.html', data=data, columns=columns)


# 点击相关刷新页面，主页面变为不相关的信息
@collection_sz.route('/collectionirrelevantview')
@login_required
def collection_irrelevant_view():
    columns = [
        {"field": "meta.download_slot", "title": "来源", "sortable": False, },
        {"field": "items.time", "title": "日期", "sortable": False, },
        {"field": "items.title", "title": "标题", "sortable": False, },
        {"field": "details", "title": "操作", "sortable": False, },
    ]
    data = []
    col = Suzhou.col
    for record in col.find():
        # print(record)
        record['meta.download_slot'] = '<a class=\"form btn\" style=\"color: #25ccde; \">来源</button>'
        record['details'] = '<a class=\"icon-btn btn\" >详情</button> '
        record['_id'] = str(record['_id'])
        if record['field'] == "1":
            data.append(record)
    return render_template('suzhou/collection_irrrelevant.html', data=data, columns=columns)


@collection_sz.route('/collectionirrelevantviews')
@login_required
def collection_irrelevant_views():
    return redirect(url_for('collectionSuzhou.user_list'))


