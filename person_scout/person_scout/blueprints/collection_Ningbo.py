#!/usr/bin/env python
# coding: utf-8
from flask import Blueprint, render_template, request, url_for, redirect
from bson import ObjectId
from flask_login import login_required

from person_scout.models.Ningbo import Ningbo

collection_nb = Blueprint('collectionNingbo', __name__)


# 从mongo(models的Purchase)中user获取用户列表并展示，跳转到ningbo/collection_untreated.html
@collection_nb.route('/')
@login_required
def user_list():
    columns = [
        {"field": "source", "title": "来源", "sortable": False, },
        {"field": "items.time", "title": "注册时间", "sortable": False, },
        {"field": "items.title", "title": "标题", "sortable": False, },
        {"field": "details", "title": "操作", "sortable": False, },
    ]
    data = []
    col = Ningbo.col
    for record in col.find():
        record['source'] = '<a class=\"source btn\" style=\"color: #25ccde; \">来源</button>'
        record[
            'details'] = '<a class=\"icon-btn0 btn\" style=\"color: #25ccde; \">详情</button>'
        record['_id'] = str(record['_id'])
        # print(record)
        if record['field'] == "null":
            data.append(record)

    return render_template('ningbo/collection_untreated.html', columns=columns, data=data)

# 读取基本信息，从content中读取文章，跳转到collection_detail.html
@collection_nb.route('/collectiondetail')
@login_required
def Ningbo_detail():
    col = Ningbo.col
    # post_filter = {}
    user_filter = {}
    params = request.args
    if 'uid' in params:
        user_filter['_id'] = ObjectId(params['uid'])
        post_filter = {}
        # post_filter['_id'] = ObjectId(params['uid'])
    cur = col.find(user_filter)
    raw_posts = [x for x in cur]
    posts = []
    index = 0
    for post in raw_posts:
        userpost = {
            '_id': post['_id'],
            'content': post['items']['content'],
            'url': post['meta']['url'],
            'source': post['meta']['download_slot'],
            'time': post['items']['time'],
            'title': post['items']['title'],
        }
        # print(userpost)
        posts.append(userpost)

        return render_template('ningbo/collection_detail.html', posts=posts,userpost=userpost)

# 用标志位判断相关，刷新页面
@collection_nb.route('/collectionrelatedview')
@login_required
def collection_related_view():
    params = request.args
    # print(params)
    Ningbo.col.update(
        {"_id": ObjectId(params['uid'])},
        {"$set": {"field": "0"}},
    )
    return redirect(url_for('collectionNingbo.user_list'))



# # 用标志位判断相关，刷新页面
@collection_nb.route('/collectionirrelevantview')
@login_required
def collection_irrelevant_view2():
    params = request.args
    Ningbo.col.update(
        {"_id": ObjectId(params['uid'])},
        {"$set": {"field": "1"}},
    )
    return redirect(url_for('collectionNingbo.user_list'))

#相关
@collection_nb.route('/collectionrelated')
@login_required
# def collection_related():
#     print("haha")
#     return redirect(url_for('collectionNingbo.user_list'))
def user_list_related():
    columns = [
        {"field": "source", "title": "来源", "sortable": False, },
        {"field": "items.time", "title": "注册时间", "sortable": False, },
        {"field": "items.title", "title": "标题", "sortable": False, },
        {"field": "details", "title": "操作", "sortable": False, },
    ]
    data = []
    col = Ningbo.col
    for record in col.find():
        record['source'] = '<a class=\"source btn\" style=\"color: #25ccde; \">来源</button>'
        record[
            'details'] = '<a class=\"icon-btn0 btn\" style=\"color: #25ccde; \">详情</button>'
        record['_id'] = str(record['_id'])
        # print(record)
        if record['field'] == "0":
            data.append(record)

    return render_template('ningbo/collection_related.html', columns=columns, data=data)


#不相关
@collection_nb.route('/collectionirrelevant')
@login_required
def user_list_irrelevant():
    columns = [
        {"field": "source", "title": "来源", "sortable": False, },
        {"field": "items.time", "title": "注册时间", "sortable": False, },
        {"field": "items.title", "title": "标题", "sortable": False, },
        {"field": "details", "title": "操作", "sortable": False, },
    ]
    data = []
    col = Ningbo.col
    for record in col.find():
        record['source'] = '<a class=\"source btn\" style=\"color: #25ccde; \">来源</button>'
        record[
            'details'] = '<a class=\"icon-btn0 btn\" style=\"color: #25ccde; \">详情</button>'
        record['_id'] = str(record['_id'])
        # print(record)
        if record['field'] == "1":
            data.append(record)

    return render_template('ningbo/collection_irrelevant.html', columns=columns, data=data)


#未处理
@collection_nb.route('/collectionuntreated')
@login_required
# def collection_related():
#     print("haha")
#     return redirect(url_for('collectionNingbo.user_list'))
def user_list_untreated():
    columns = [
        {"field": "source", "title": "来源", "sortable": False, },
        {"field": "items.time", "title": "注册时间", "sortable": False, },
        {"field": "items.title", "title": "标题", "sortable": False, },
        {"field": "details", "title": "操作", "sortable": False, },
    ]
    data = []
    col = Ningbo.col
    for record in col.find():
        record['source'] = '<a class=\"source btn\" style=\"color: #25ccde; \">来源</button>'
        record[
            'details'] = '<a class=\"icon-btn0 btn\" style=\"color: #25ccde; \">详情</button>'
        record['_id'] = str(record['_id'])
        # print(record)
        if record['field'] == "null":
            data.append(record)

    return render_template('ningbo/collection_untreated.html', columns=columns, data=data)