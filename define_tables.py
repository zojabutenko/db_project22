from app import db, datetime


class Post(db.Model):
    # main table: info about posts
    id = db.Column(db.Integer, primary_key=True)
    author_username = db.Column(db.String, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    post_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Post %r>' % self.id


class Author(db.Model):
    # data about an author, linked to the main table by username
    num_posts = db.column(db.Integer, primart_key=True)     # number of publications from this author
    username = db.Column(db.String, db.ForeignKey('Post.author_id'), nullable=False)
    liked = db.Column(db.Text, primary_key=True)    # list of publications that the author has liked
    country = db.Column(db.Text, primary_key=True)
    age = db.Column(db.Integer, primary_key=True)
    posted = db.Column(db.Text, primary_key=True)   # list of publications from this author


class Likes(db.Model):
    # info about the likes on a post, linked to the main table by post_id
    post_id = db.Column(db.Integer, db.ForeignKey('Post.id'), nullable=False)
    liked_by = db.Column(db.Text, primary_key=True)  # list of users that have liked the post
    num_likes = db.Column(db.Integer, primary_key=True)


class PostText(db.Model):
    # info about the text in the post, linked to the main table by post_id
    post_id = db.Column(db.Integer, db.ForeignKey('Post.id'), nullable=False)
    post_text = db.Column(db.Text, primary_key=True)
    text_length = db.Column(db.Integer, primary_key=True)   # length of post in symbols
    text_keywords = db.Column(db.Text, primary_key=True)    # list of keywords in text generated by a model
    topic_id = db.Column(db.Integer, primary_key=True)     # id of main topic decided by a model


class Topics(db.Model):
    # info about topics of posts, linked to the table PostText by topic_id
    topic_id = db.Column(db.Integer, db.ForeignKey('PostText.post_id'), nullable=False)
    topic_name = db.Column(db.Text, primary_key=True)   # name of the topic by id (e.g. 'sports' or 'music')
