#!/usr/bin/env python
# coding: utf-8
from bson import ObjectId
from flask import Blueprint, render_template, request, url_for
from flask_login import login_required
from werkzeug.utils import redirect


from person_scout.models.Hangzhou import Hangzhou

collection_hz = Blueprint('collectionHangzhou', __name__)


# 从mongo(models的Hangzhou)中user获取用户列表并展示，跳转到collection/collection_hz_manage.html
@collection_hz.route('/')
@login_required
def user_list():
    columns = [
        {"field": "meta.download_slots", "title": "来源", "sortable": False, },
        {"field": "items.time", "title": "日期", "sortable": False, },
        {"field": "items.title", "title": "标题", "sortable": False, },
        {"field": "details", "title": "操作", "sortable": False, },
    ]
    data = []
    col = Hangzhou.col

    for record in col.find():
        record['meta.download_slots'] = '<a class=\"form btn"\ style=\"color: #25ccde;">来源</a>'
        record['details'] = '<a class=\"icon-btn btn\" >详情</button>'
        record['_id'] = str(record['_id'])
        if record['field'] == "null":
            data.append(record)

    return render_template('Hangzhou/collection_unrelated.html', columns=columns, data=data)



# 读取基本信息，从content中读取文章，跳转到collection_detail.html
@collection_hz.route('/collectionhzdetail')
@login_required
def collection_detail():
    col = Hangzhou.col
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
            'url':post['meta']['url'],
            '_id': post['_id'],
            'title': post['items']['title'],
            'time': post['items']['time'],
            'content': post['items']['content'],

        }
        # print(userpost)
        posts.append(userpost)
    print(posts)
    return render_template('Hangzhou/collection_hz_detail.html', posts=posts)

# 用标志位判断相关，刷新页面
@collection_hz.route('/collectionrelated')
@login_required
def collection_related():
    params = request.values
    Hangzhou.col.update(
        {"_id": ObjectId(params['uid'])},
        {"$set": {"field": "0"}},
    )
    return redirect(url_for('collectionHangzhou.user_list'))
# 用标志位判断相关，刷新页面
@collection_hz.route('/collectionirrelevant')
@login_required
def collection_irrelevant():
    params = request.values
    Hangzhou.col.update(
        {"_id": ObjectId(params['uid'])},
        {"$set": {"field": "1"}},
    )
    return redirect(url_for('collectionHangzhou.user_list'))

# 点击相关刷新页面，主页面变为相关的信息
@collection_hz.route('/collectionrelatedview')
@login_required
def collection_related_view():
    columns = [
        {"field": "meta.download_slots", "title": "来源", "sortable": False, },
        {"field": "items.time", "title": "日期", "sortable": False, },
        {"field": "items.title", "title": "标题", "sortable": False, },
        {"field": "details", "title": "操作", "sortable": False, },
    ]
    data = []
    col = Hangzhou.col
    for record in col.find():
        # print(record)
        record['meta.download_slots'] = '<a class=\"form btn"\ style=\"color: #25ccde;">来源</a>'
        record[
            'details'] = '<a class=\"icon-btn btn\" >详情</button> '
        record['_id'] = str(record['_id'])
        if record['field'] == "0":
            data.append(record)
    return render_template('Hangzhou/collection_related.html', data=data, columns=columns)

# 点击相关刷新页面，主页面变为不相关的信息
@collection_hz.route('/collectionirrelevantview')
@login_required
def collection_irrelevant_view():
    columns = [
        {"field": "meta.download_slots", "title": "来源", "sortable": False, },
        {"field": "items.time", "title": "日期", "sortable": False, },
        {"field": "items.title", "title": "标题", "sortable": False, },
        {"field": "details", "title": "操作", "sortable": False, },
    ]
    data = []
    col = Hangzhou.col
    for record in col.find():
        # print(record)
        record['meta.download_slots'] = '<a class=\"form btn"\ style=\"color: #25ccde;">来源</a>'
        record[
            'details'] = '<a class=\"icon-btn btn\" >详情</button> '
        record['_id'] = str(record['_id'])
        if record['field'] == "1":
            data.append(record)
    return render_template('Hangzhou/collection_irrelevant.html', data=data, columns=columns)

@collection_hz.route('/collectionirrelevantviews')
@login_required
def collection_irrelevant_views():
    columns = [
        {"field": "meta.download_slots", "title": "来源", "sortable": False, },
        {"field": "items.time", "title": "日期", "sortable": False, },
        {"field": "items.title", "title": "标题", "sortable": False, },
        {"field": "details", "title": "操作", "sortable": False, },
    ]
    data = []
    col = Hangzhou.col
    for record in col.find():
        record['meta.download_slots'] = '<a class=\"form btn"\ style=\"color: #25ccde;">来源</a>'
        record[
            'details'] = '<a class=\"icon-btn btn\" >详情</button> '
        record['_id'] = str(record['_id'])
        if record['field'] == "null":
            data.append(record)

    return render_template('Hangzhou/collection_unrelated.html', data=data, columns=columns)
