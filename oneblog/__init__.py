# -*- coding: utf-8 -*-
# @Time    : 2019/12/25 14:47
# @Author  : bill
# @File    : __init__.py
# @Software: PyCharm

from flask import Flask
from oneblog.blueprints.blog import blog_bp
from oneblog.extensions import db, moment, bootstrap
import click
from oneblog.models import *
from faker import Faker
import random


def create_app(config_name='config.py'):
    app = Flask('oneblog')
    app.config.from_pyfile(config_name)

    app.register_blueprint(blog_bp)

    db.init_app(app)
    moment.init_app(app)
    bootstrap.init_app(app)

    register_commands(app)
    register_template_context(app)
    return app


def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def init(drop):
        """Initialize the database."""
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        category_list = ['默认', '随笔', '工作', '私人']
        for name in category_list:
            category = Category(name=name)
            db.session.add(category)
        db.session.commit()
        click.echo('Initialized database.')

    @app.cli.command()
    def forge():
        fake = Faker()
        for i in range(20):
            post = Article(
                title=fake.sentence(),
                body=fake.text(2000),
                category=Category.query.get(random.randint(1, Category.query.count())),
                timestamp=fake.date_time_this_year()
            )
            db.session.add(post)
        db.session.commit()
        click.echo('Add some fake articles.')


def register_template_context(app):
    @app.context_processor
    def make_template_context():
        categories = Category.query.order_by(Category.name).all()

        return dict(
            categories=categories,)
