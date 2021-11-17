from finalproject import api
from flask_restx import fields

'''
Model for marshalling and swagger docs
'''

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