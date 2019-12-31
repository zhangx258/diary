# -*- coding: utf-8 -*-
# @Time    : 2019/12/27 10:38
# @Author  : bill
# @File    : forms.py
# @Software: PyCharm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from oneblog.models import Category


class ArticleForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(1, 60)])
    body = TextAreaField('Body', validators=[DataRequired()])
    category_id = SelectField('Category', validators=[DataRequired()], coerce=int, default=1)
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.category_id.choices = [(category.id, category.name)
                                    for category in Category.query.order_by(Category.id).all()]


class DeletearticleForm(FlaskForm):
    submit = SubmitField('删除')


class EditarticleForm(FlaskForm):
    submit = SubmitField('编辑')


class AdminForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(1, 128)])
    submit = SubmitField('登录')
