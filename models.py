from flask_sqlalchemy import SQLAlchemy

"""Models for Blogly."""

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    """User"""
    __tablename__ = 'users'

    def __repr__(self) -> str:
        u = self
        return f'<User id={u.id} first_name={u.first_name} last_name={u.last_name} image_url={u.image_url}'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    image_url = db.Column(db.String)
