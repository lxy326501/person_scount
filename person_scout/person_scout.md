# person_scout

所有的推文都需要存入solr之中（暂时不用管）

目录结构：
- person_scout
    - apis                **api文件**
        - \_\_init\_\_.py    工厂函数，返回api
        - social_api.py     api的父类
        - twitter_api.py    推特数据项的操作类，包括调用爬取函数，处理数据，设置任务
        - twitter_curl.py   推特信息获取类，由api调用去爬取数据
    - blueprints        **蓝图文件，这里面只负责函数的调用，不管复杂逻辑处理**
        - event_monitor.py            事件任务
        - keyperson_monitor.py    关键人物
        - login.py                          登录、登出
        - spread_analysis.py          传播分析
        - user_manage.py             用户管理
    - forms            **表单文件**
        - keyperson_monitor.py     关键人物的页面中的form表单定义
        - event_monitor.py            事件任务的页面form定义
        - login.py                          登录页面的form
        - user_manage.py             用户管理的form
    - models        **数据库操作文件，一些数据库的关联操作放在这里**
        - event       文件名与数据库名对应
        - ……
    - static           **静态文件**
    - templates    **html文件**
        - errors      错误处理文件
        - event      事件
        - keyperson      关键人物
        - login       登录
        - spread    传播分析
        - user        用户管理
    - __init__.py    **初始化程序**
    - decorators.py    **权限管理装饰器**
    - extensions.py    **不用管**
    - fakes.py             **假数据，暂时没用**
    - settings.py        **设置，用到的只有DevelopmentConfig**
- pipfile 依赖文件
