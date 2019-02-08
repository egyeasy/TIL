from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# flask 옵션을 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie.sqlite3' # /// 상대경로, //// 절대경로
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 없으면 에러가 남

db = SQLAlchemy(app)

# 테이블 생성
db.init_app(app) # 앱을 넣어서 데이터베이스를 시작

class Movie(db.Model):
    __tablename__ = "movies"
    the_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, unique=True, nullable=False)
    title_en = db.Column(db.String, nullable=False)
    audience = db.Column(db.Integer, nullable=False)
    open_date = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    watch_grade = db.Column(db.String, nullable=False)
    score = db.Column(db.Float, nullable=False)
    poster_url = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    
    
    
db.create_all()


@app.route('/')
def index():
    
    return redirect('/movies')


@app.route('/movies')
def base():
    movies = Movie.query.all()
    
    return render_template('base.html', movies=movies)
    
    
@app.route('/movies/new')
def new():
    
    return render_template('new.html')
    
    
@app.route('/movies/create')
def create():
    title = request.args.get('title')
    title_en = request.args.get('title_en')
    audience = request.args.get('audience')
    open_date = request.args.get('open_date')
    genre = request.args.get('genre')
    watch_grade = request.args.get('watch_grade')
    score = request.args.get('score')
    poster_url = request.args.get('poster_url')
    description = request.args.get('description')
    
    m = Movie(title=title, title_en=title_en, audience=audience, open_date=open_date, genre=genre, watch_grade=watch_grade, score=score, poster_url=poster_url, description=description)
    db.session.add(m)
    db.session.commit()
    
    idx = Movie.query.order_by(Movie.the_id.desc()).first().the_id
    
    return redirect('/movies/{}'.format(idx))
    
    
@app.route('/movies/<int:movie_id>')
def show(movie_id):
    m = Movie.query.get(movie_id)
    
    return render_template('show.html', m=m)
    
    
@app.route('/movies/<int:movie_id>/edit')
def edit(movie_id):
    m = Movie.query.get(movie_id)
    
    return render_template('edit.html', m=m)
    
    
@app.route('/movies/<int:movie_id>/update')
def update(movie_id):
    title = request.args.get('title')
    title_en = request.args.get('title_en')
    audience = request.args.get('audience')
    open_date = request.args.get('open_date')
    genre = request.args.get('genre')
    watch_grade = request.args.get('watch_grade')
    score = request.args.get('score')
    poster_url = request.args.get('poster_url')
    description = request.args.get('description')
    
    m = Movie.query.get(movie_id)
    m.title = title
    m.title_en = title_en
    m.audience = audience
    m.open_date = open_date
    m.genre = genre
    m.watch_grade = watch_grade
    m.score = score
    m.poster_url = poster_url
    m.description = description
    db.session.commit()
    
    return redirect('/movies/{}'.format(m.the_id))
    
    
@app.route('/movies/<int:movie_id>/delete')
def delete(movie_id):
    m = Movie.query.get(movie_id)
    db.session.delete(m)
    db.session.commit()
    
    return redirect('/movies')