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

login_model = api.model(
    'Login',
    {
        'email': fields.String(),
        'password': fields.String()
    }
)

register_model = api.model(
    'Register',
    {
        'email': fields.String(),
        'username': fields.String(),
        'password': fields.String()
    }
)

refresh_model = api.model(
    'Refresh Token',
    {
        'access_token': fields.String(),
        'refresh_token': fields.String()
    }
)
