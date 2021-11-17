from sqlalchemy.orm import relationship

from finalproject import db


class Directors(db.Model):
    __tablename__ = 'directors'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(1000), nullable=False)
    gender = db.Column(db.Integer())
    uid = db.Column(db.Integer())
    department = db.Column(db.String(1000), nullable=False)
    movies = relationship("Movies", back_populates="directors")

    def __repr__(self):
        return self.name
