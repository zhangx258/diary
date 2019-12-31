# -*- coding: utf-8 -*-
# @Time    : 2019/12/25 15:08
# @Author  : bill
# @File    : admin.py
# @Software: PyCharm
from flask import Blueprint, render_template, flash, redirect, url_for
from oneblog.forms import AdminForm
from oneblog.models import Admin
from flask_login import login_user, logout_user
from oneblog.utils import redirect_back
admin_bg = Blueprint('admin', __name__)


@admin_bg.route('/', methods=['GET', 'POST'])
def login():
    form = AdminForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        admin = Admin.query.first()
        if admin:
            if username == admin.username and admin.validate_password(password):
                login_user(admin)
                flash('Welcome back.', 'info')
                return redirect_back()
            flash('Invalid username or password.', 'warning')
        else:
            flash('No account.', 'warning')
    return render_template('admin/login.html', form=form)


@admin_bg.route('/logout')
def logout():
    logout_user()
    flash('Logout success.', 'info')
    return redirect(url_for('blog.index'))
