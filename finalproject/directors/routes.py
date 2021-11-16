from flask import jsonify, request, make_response
from flask_jwt_extended import jwt_required
from flask_pydantic import validate
from flask_restx import Resource, Namespace, marshal

from finalproject import db
from finalproject.shared.api_model import director_request_model, director_response_model
from finalproject.directors.model import Directors
from finalproject.directors.pydantic_model import DirectorRequestModel

api = Namespace('Directors', description='CRUD Directors', path='/')


@api.route('/director')
class DirectorsREST(Resource):

    @api.marshal_list_with(director_response_model, code=200)
    @jwt_required()
    def get(self):
        directors = Directors.query.limit(5).all()
        return directors

    # @api.marshal_with(book_model, code=201)
    @api.expect(director_request_model)
    @api.response(201, 'Created')
    @validate()
    @jwt_required()
    def post(self, body: DirectorRequestModel):
        print(body.name)
        new_director = Directors(
            name=body.name,
            gender=body.gender,
            uid=body.uid,
            department=body.department
        )

        db.session.add(new_director)
        db.session.commit()

        return make_response(jsonify({'msg': f"New director with id {new_director.id} has been created"}), 201)


@api.route('/director/<int:id>')
class DirectorREST(Resource):

    # @api.marshal_with(movie_response_model, code=200)
    @api.response(200, model=director_response_model, description='Success')
    @jwt_required()
    def get(self, id):
        director = Directors.query.get_or_404(id)
        return marshal(director, director_response_model)

    @api.expect(director_request_model)
    @jwt_required()
    @validate()
    def put(self, id, body: DirectorRequestModel):
        director_to_update = Directors.query.get_or_404(id)

        director_to_update.name = body.name
        director_to_update.gender = body.gender
        director_to_update.uid = body.uid
        director_to_update.department = body.department

        db.session.commit()

        return jsonify(msg='Update success')

    # @api.marshal_with(movie_response_model, code=200)
    # @api.response(movie_response_model, code=200)
    @jwt_required()
    def delete(self, id):
        director_to_delete = Directors.query.get_or_404(id)
        db.session.delete(director_to_delete)
        db.session.commit()
        return jsonify(msg='Delete success')
