from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from define_tables import Post, Author, Likes, PostText, Topics

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/zoiabutenko/Desktop/db_project22/blog.db'
db = SQLAlchemy(app)



@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/create-article', methods=['POST', 'GET'])
def create_post():
    if request.method == 'POST':
        text = request.form['text']

        post = Post(text=text)

        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/ty')
        except:
            return "При записи ответа произошла ошибка"
    else:
        return render_template('create-article.html')


@app.route('/posts')
def posts():
    posts = Post.query.order_by(Post.post_time.desc()).all()
    return render_template('posts.html', posts=posts)


@app.route('/posts/<int:id>')
def posts_detail(id):
    post = Post.query.get(id)
    return render_template('post_detail.html', post=post)


@app.route('/ty')
def ty():
    return render_template('ty.html')


@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


if __name__ == '__main__':
    app.run(debug=True)
