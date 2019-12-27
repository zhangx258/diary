# -*- coding: utf-8 -*-
# @Time    : 2019/12/27 10:38
# @Author  : bill
# @File    : forms.py
# @Software: PyCharm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length


class ArticleForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(1, 60)])
    body = TextAreaField('Body', validators=[DataRequired()])
    # category = SelectField('Category', validators=[DataRequired()],
    #                        choices=[(1, '日记'), (2, '星座'), (3, '爱情')],
    #                        default=1,
    #                        coerce=int)
    submit = SubmitField('Submit')


class DeletearticleForm(FlaskForm):
    submit = SubmitField('Delete')