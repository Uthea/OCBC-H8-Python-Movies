from sqlalchemy import ForeignKey

from skeleton import db, app
from sqlalchemy.orm import relationship


class Movies(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer(), primary_key=True)
    original_title = db.Column(db.String(255), nullable=False)
    budget = db.Column(db.Integer())
    popularity = db.Column(db.Integer())
    release_date = db.Column(db.String(255), nullable=False)
    revenue = db.Column(db.Integer())
    title = db.Column(db.String(255), nullable=False)
    vote_average = db.Column(db.REAL())
    vote_count = db.Column(db.Integer())
    overview = db.Column(db.String(255), nullable=False)
    tagline = db.Column(db.String(255), nullable=False)
    uid = db.Column(db.Integer())
    director_id = db.Column(db.Integer(), ForeignKey('directors.id'))
    directors = relationship("Directors", back_populates="movies")

    def __repr__(self):
        return self.title


class Directors(db.Model):
    __tablename__ = 'directors'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.Integer())
    uid = db.Column(db.Integer())
    department = db.Column(db.String(255), nullable=False)
    movies = relationship("Movies", back_populates="directors")

    def __repr__(self):
        return self.name
