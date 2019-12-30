# -*- coding: utf-8 -*-
# @Time    : 2019/12/25 17:02
# @Author  : bill
# @File    : config.py
# @Software: PyCharm
import os


SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/oneblog?charset=utf8"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.getenv('SECRET_KEY', 'iknowiwouldnotforgetyou')
