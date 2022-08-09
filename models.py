"""Models for  app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class MyTable(db.Model):
    """Playlist."""

    __tablename__ = "mytables"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


def connect_db(app):
    """Connect this database to provided Flask app.
    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)


class User(db.Model):
    """"User model"""

    __tablename__ = 'users'

    username = db.Column(db.String(20), nullable=False, primary_key=True, unique=True)
    password = db.Column(db.String(100), nullable=False, unique=False)
    email = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

