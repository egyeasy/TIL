from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    
    return redirect('/articles')
    
    
@app.route('/articles')
def articles():
    db = sqlite3.connect('blog.db')
    c = db.cursor()
    sql = 'SELECT * FROM articles'
    c.execute(sql)
    articles = c.fetchall()
    
    return render_template('articles.html', articles=articles)
    
@app.route('/articles/new')
def new():
    
    return render_template('new.html')
    
@app.route('/articles/create')
def create():
    title = request.args.get('title')
    content = request.args.get('content')
    author = request.args.get('author')
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    db = sqlite3.connect('blog.db')
    
    # 1. 커서를 생성 - SQL 문장을 쓸 수 있게끔
    c = db.cursor()
    # 2. sql 실행
    sql = 'INSERT INTO articles (title, content, author, created_at) VALUES ("{}", "{}", "{}", "{}")'.format(title, content, author, created_at)
    c.execute(sql)
    # 3. commit - transaction 개념. 
    db.commit()
    
    c = db.cursor()
    sql = 'SELECT id FROM articles ORDER BY id DESC LIMIT 1'
    c.execute(sql)
    
    article_id = c.fetchone()[0]
    
    return redirect('/articles/{}'.format(article_id))
    

@app.route('/articles/<int:article_id>')
def detail(article_id):
    db = sqlite3.connect('blog.db')
    c = db.cursor()
    sql = 'SELECT * FROM articles WHERE id == {}'.format(article_id)
    c.execute(sql)
    article = c.fetchone()
    
    return render_template('detail.html', article=article)
    
    
@app.route('/articles/<int:article_id>/edit')
def edit(article_id):
    db = sqlite3.connect('blog.db')
    c = db.cursor()
    sql = 'SELECT * FROM articles WHERE id == {}'.format(article_id)
    c.execute(sql)
    article = c.fetchone()
    
    return render_template('edit.html', article=article)
    
    
@app.route('/articles/<int:article_id>/update')
def update(article_id):
    edits = request.args
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    db = sqlite3.connect('blog.db')
    c = db.cursor()
    sql = 'UPDATE articles SET title = "{}", content = "{}", author = "{}", created_at = "{}" WHERE id == {}'.format(edits.get('title'), edits.get('content'), edits.get('author'), created_at, article_id)
    c.execute(sql)
    db.commit()
    
    return redirect('/articles/{}'.format(article_id))
    
    
@app.route('/articles/<int:article_id>/delete')
def delete(article_id):
    
    db = sqlite3.connect('blog.db')
    c = db.cursor()
    sql = 'DELETE FROM articles WHERE id == {}'.format(article_id)
    c.execute(sql)
    db.commit()
    
    return redirect('/articles')