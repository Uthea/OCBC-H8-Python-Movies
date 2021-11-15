from datetime import datetime

from skeleton import db, app


class Book(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(25), nullable=False)
    author = db.Column(db.String(40), nullable=False)
    date_added = db.Column(db.DateTime(), default=datetime.utcnow())

    def __repr__(self):
        return self.title


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Book': Book
    }


