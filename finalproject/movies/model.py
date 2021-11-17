from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from finalproject import db


class Movies(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer(), primary_key=True)
    original_title = db.Column(db.String(1000), nullable=False)
    budget = db.Column(db.BIGINT())
    popularity = db.Column(db.BIGINT())
    release_date = db.Column(db.String(1000), nullable=False)
    revenue = db.Column(db.BIGINT())
    title = db.Column(db.String(1000), nullable=False)
    vote_average = db.Column(db.REAL())
    vote_count = db.Column(db.BIGINT())
    overview = db.Column(db.String(1000), nullable=False)
    tagline = db.Column(db.String(1000), nullable=False)
    uid = db.Column(db.BIGINT())
    director_id = db.Column(db.BIGINT(), ForeignKey('directors.id'))
    directors = relationship("Directors", back_populates="movies")

    def __repr__(self):
        return self.title

