# -*- coding: utf-8 -*-
# @Time    : 2019/12/25 17:34
# @Author  : bill
# @File    : models.py
# @Software: PyCharm

from oneblog.extensions import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True, index=True)


class Article(db.Model):
    __tablename__ = 'article'
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    body = db.Column(db.TEXT)
    category = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, default=datetime.now, index=True)
