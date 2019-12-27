# -*- coding: utf-8 -*-
# @Time    : 2019/12/25 16:13
# @Author  : bill
# @File    : extensions.py
# @Software: PyCharm

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment


bootstrap = Bootstrap()
db = SQLAlchemy()
moment = Moment()
