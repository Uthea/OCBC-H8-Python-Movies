from skeleton import api
from flask_restx import fields

director_response_model = api.model(
    'Director Response',
    {
        'id': fields.Integer(),
        'name': fields.String(),
        'gender': fields.Integer(),
        'uid': fields.Integer(),
        'department': fields.String(),
    }
)

movie_response_model = api.model(
    'Movie Response',
    {
        'id': fields.Integer(),
        'original_title': fields.String(),
        'budget': fields.Integer(),
        'popularity': fields.Integer(),
        'release_date': fields.String(),
        'revenue': fields.Integer(),
        'title': fields.String(),
        'vote_average': fields.Float(),
        'vote_count': fields.Integer(),
        'overview': fields.String(),
        'tagline': fields.String(),
        'uid': fields.Integer(),
        'director': fields.Nested(director_response_model, attribute="directors"),
    }
)

movie_request_model = api.model(
    'Movie Request',
    {
        'original_title': fields.String(),
        'budget': fields.Integer(),
        'popularity': fields.Integer(),
        'release_date': fields.String(),
        'revenue': fields.Integer(),
        'title': fields.String(),
        'vote_average': fields.Float(),
        'vote_count': fields.Integer(),
        'overview': fields.String(),
        'tagline': fields.String(),
        'uid': fields.Integer(),
        'director_id': fields.Integer(),
    }
)



