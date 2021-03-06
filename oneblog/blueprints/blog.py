# -*- coding: utf-8 -*-
# @Time    : 2019/12/25 15:08
# @Author  : bill
# @File    : blog.py
# @Software: PyCharm


from flask import Blueprint, render_template, redirect, url_for, abort, request, current_app
from oneblog.models import *
from oneblog.forms import *
from flask_login import login_required
from sqlalchemy import or_, extract, text
blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['BLUELOG_POST_PER_PAGE']
    pagination = Article.query.order_by(Article.timestamp.desc()).paginate(page, per_page=per_page)
    articles = pagination.items
    return render_template('blog/index.html', articles=articles, pagination=pagination)


@blog_bp.route('/article/<int:article_id>')
@login_required
def show_article(article_id):
    delete = DeletearticleForm()
    edit = EditarticleForm()
    article = Article.query.filter(Article.id == article_id).first()
    return render_template('blog/article.html', article=article, delete=delete, edit=edit)


@blog_bp.route('/post/', methods=['GET', 'POST'])
@login_required
def post_article():
    form = ArticleForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        category_id = form.category_id.data
        article = Article(
            title=title, body=body, category_id=category_id
        )
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('.index'))
    return render_template('blog/post.html', forms=form)


@blog_bp.route('/delete/<int:article_id>', methods=['POST'])
@login_required
def delete_article(article_id):
    form = DeletearticleForm()
    if form.validate_on_submit():
        article = Article.query.get(article_id)
        db.session.delete(article)
        db.session.commit()
    else:
        abort(400)
    return redirect(url_for('.index'))


@blog_bp.route('/edit/<int:article_id>', methods=['GET', 'POST'])
@login_required
def edit_article(article_id):
    default = Article.query.get_or_404(article_id)
    form = ArticleForm(title=default.title, body=default.body, category_id=default.category_id)
    if form.validate_on_submit():
        default.title = form.title.data
        default.body = form.body.data
        default.category_id = form.category_id.data
        default.timestamp = datetime.now()
        db.session.commit()
        return redirect(url_for('blog.show_article', article_id=article_id))
    return render_template('blog/post.html', forms=form)


@blog_bp.route('/category/<int:category_id>')
def show_category(category_id):
    category = Category.query.get_or_404(category_id)
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['BLUELOG_POST_PER_PAGE']
    pagination = Article.query.with_parent(category).order_by(Article.timestamp.desc()).paginate(page,
                                                                                                 per_page=per_page)
    articles = pagination.items
    return render_template('blog/index.html', articles=articles, pagination=pagination)


@blog_bp.route('/about_wings')
def about_wings():
    return render_template('blog/wings.html')


@blog_bp.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        kw = request.form.get('kw')
        articles = Article.query.filter(
            or_(Article.title.like("%"+kw+"%") if kw is not None else "",
                Article.body.like("%" + kw + "%") if kw is not None else "",
                extract('year', Article.timestamp) == int(kw) if kw is not None and kw.isdigit() else text(""),
                extract('month', Article.timestamp) == int(kw) if kw is not None and kw.isdigit() else text(""),
                extract('day', Article.timestamp) == int(kw) if kw is not None and kw.isdigit() else text(""),)
        ).order_by(Article.timestamp.desc())
        return render_template('blog/index.html', articles=articles, pagination=None)
    return redirect(url_for('blog.index'))


@blog_bp.route('/404')
def handler_404():
    return render_template('errors/404.html')
