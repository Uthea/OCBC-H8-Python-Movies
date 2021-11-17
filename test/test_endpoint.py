import flask_unittest
import json
import os
from unittest import mock

basedir = os.path.dirname(os.path.realpath(__file__))
db_url = 'sqlite:///' + os.path.join(basedir, 'test.db')

with mock.patch.dict(os.environ, {'FLASK_ENV': 'test', 'DATABASE_URL': db_url}):
    from finalproject import app


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
