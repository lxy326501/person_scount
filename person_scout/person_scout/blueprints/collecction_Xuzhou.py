from flask import Blueprint, render_template, request, redirect, url_for
from bson import ObjectId
from flask_login import login_required

from person_scout.decorators import permission_required
from person_scout.models.Xuzhou import Xuzhou

collection_xz = Blueprint('collectionXuzhou', __name__)

@collection_xz.route('/')
@login_required
def collection_list():
    columns = [
        {"field": "source", "title": "来源", "sortable": False, },
        {"field": "items.time", "title": "注册时间", "sortable": False, },
        {"field": "items.title", "title": "标题", "sortable": False, },
        {"field": "details", "title": "操作", "sortable": False, },
    ]
    data = []
    col = Xuzhou.col
    for record in col.find():
        record['source'] = '<a class=\"source btn\" style=\"color: #25ccde; \">来源</button>'
        record[
            'details'] = '<a class=\"icon-btn0 btn\" style=\"color: #25ccde; \">详情</button>'
        record['_id'] = str(record['_id'])
        # print(record)
        if record['field'] == "null":
            data.append(record)

    return render_template('xuzhou/collection_untreated.html', columns=columns, data=data)


# 读取基本信息，从content中读取文章，跳转到collection_detail.html
@collection_xz.route('/collectiondetail')
@login_required
def collection_detail():
    col = Xuzhou.col
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
        print(post['items']['content'],'\t')
        userpost = {
            '_id': post['_id'],
            'url': post['meta']['url'],
            'content': '\n'.join(post['items']['content']),
            'source': post['meta']['download_slot'],
            'time': post['items']['time'],
            'title': post['items']['title'],
        }
        posts.append(userpost)

        return render_template('xuzhou/collection_detail.html', posts=posts, userpost=userpost)

# 点击相关刷新页面，主页面变为相关的信息
@collection_xz.route('/collectionrelatedview')
@login_required
def collection_related_view():
    params = request.args
    # print(params)
    Xuzhou.col.update(
        {"_id": ObjectId(params['uid'])},
        {"$set": {"field": "0"}},
    )
    return redirect(url_for('collectionXuzhou.collection_list'))


# 点击相关刷新页面，主页面变为不相关的信息
@collection_xz.route('/collectionirrelevantview')
@login_required
def collection_irrelevant_view():
    params = request.args
    # print(params)
    Xuzhou.col.update(
        {"_id": ObjectId(params['uid'])},
        {"$set": {"field": "1"}},
    )
    return redirect(url_for('collectionXuzhou.collection_list'))


@collection_xz.route('/collectionrelated')
@login_required
def collection_related():
    columns = [
        {"field": "source", "title": "来源", "sortable": False, },
        {"field": "items.time", "title": "注册时间", "sortable": False, },
        {"field": "items.title", "title": "标题", "sortable": False, },
        {"field": "details", "title": "操作", "sortable": False, },
    ]
    data = []
    col = Xuzhou.col
    for record in col.find():
        record['source'] = '<a class=\"source btn\" style=\"color: #25ccde; \">来源</button>'
        record[
            'details'] = '<a class=\"icon-btn0 btn\" style=\"color: #25ccde; \">详情</button>'
        record['_id'] = str(record['_id'])
        # print(record)
        if record['field'] == "0":
            data.append(record)

    return render_template('xuzhou/collection_related.html', columns=columns, data=data)


@collection_xz.route('/collectionirrelevant')
@login_required
def collection_irrelevant():
    columns = [
        {"field": "source", "title": "来源", "sortable": False, },
        {"field": "items.time", "title": "注册时间", "sortable": False, },
        {"field": "items.title", "title": "标题", "sortable": False, },
        {"field": "details", "title": "操作", "sortable": False, },
    ]
    data = []
    col = Xuzhou.col
    for record in col.find():
        record['source'] = '<a class=\"source btn\" style=\"color: #25ccde; \">来源</button>'
        record[
            'details'] = '<a class=\"icon-btn0 btn\" style=\"color: #25ccde; \">详情</button>'
        record['_id'] = str(record['_id'])
        # print(record)
        if record['field'] == "1":
            data.append(record)

    return render_template('xuzhou/collection_irrelevant.html', columns=columns, data=data)


#未处理
@collection_xz.route('/collectionuntreated')
@login_required

def collection_untreated():
    columns = [
        {"field": "source", "title": "来源", "sortable": False, },
        {"field": "items.time", "title": "注册时间", "sortable": False, },
        {"field": "items.title", "title": "标题", "sortable": False, },
        {"field": "details", "title": "操作", "sortable": False, },
    ]
    data = []
    col = Xuzhou.col
    for record in col.find():
        record['source'] = '<a class=\"source btn\" style=\"color: #25ccde; \">来源</button>'
        record[
            'details'] = '<a class=\"icon-btn0 btn\" style=\"color: #25ccde; \">详情</button>'
        record['_id'] = str(record['_id'])
        # print(record)
        if record['field'] == "null":
            data.append(record)

    return render_template('xuzhou/collection_untreated.html', columns=columns, data=data)


# @collection_xz.route('/collectionirrelevantviews')
# @login_required
# def collection_irrelevant_views():
#     pass