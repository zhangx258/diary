# -*- coding: utf-8 -*-
# @Time    : 2019/12/25 16:13
# @Author  : bill
# @File    : extensions.py
# @Software: PyCharm

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_login import LoginManager


bootstrap = Bootstrap()
db = SQLAlchemy()
moment = Moment()
login_manager = LoginManager()
login_manager.login_view = 'admin.login'
login_manager.login_message_category = 'warning'
login_manager.login_message = '请先登录！'


@login_manager.user_loader
def load_user(user_id):
    from oneblog.models import Admin
    user = Admin.query.get(int(user_id))
    return user
