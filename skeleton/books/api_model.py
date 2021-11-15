from skeleton import api
from flask_restx import fields

book_model = api.model(
    'Book',
    {
        'id': fields.Integer(),
        'title': fields.String(),
        'author': fields.String(),
        'date_added': fields.String()
    }
)

book_post_model = api.model(
    'Book Post',
    {
        'title': fields.String(),
        'author': fields.String()
    }
)


