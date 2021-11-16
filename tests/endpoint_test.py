import flask_unittest
from finalproject import app
import json

from unittest import mock


class TestEndpoint(flask_unittest.ClientTestCase):
    app = app

    @mock.patch('flask_jwt_extended.view_decorators.verify_jwt_in_request')
    def test_get_movies_with_client(self, client, mock_jwt_required):
        rv = client.get("/movies")
        self.assertGreater(len(rv.json), 4)

    @mock.patch('flask_jwt_extended.view_decorators.verify_jwt_in_request')
    def test_post_directors_with_client(self, client, mock_jwt_required):
        rv = client.post('/directors', data=json.dumps({
            "id": "33",
            "name": "burger",
            "gender": 2,
            "uid": 123,
            "department": "manila"
        }), headers={
            "Content-Type": "application/json"
        })

        self.assertStatus(rv, 201)
