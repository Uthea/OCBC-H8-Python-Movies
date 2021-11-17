from flask import jsonify, make_response
from flask_jwt_extended import jwt_required
from flask_pydantic import validate
from flask_restx import Resource, Namespace, marshal
from sqlalchemy.exc import IntegrityError

from finalproject import db
from finalproject.movies.model import Movies
from finalproject.movies.pydantic_model import MovieRequestModel
from finalproject.shared.api_model import movie_response_model, movie_request_model

api = Namespace('Movies', description='CRUD Movies', path='/')


@api.route('/movies')
class MoviesREST(Resource):

    @api.marshal_list_with(movie_response_model, code=200)
    @jwt_required()
    def get(self):
        movies = Movies.query.limit(5).all()
        return movies

    @api.expect(movie_request_model)
    @api.response(201, 'Created')
    @validate()
    @jwt_required()
    def post(self, body: MovieRequestModel):

        new_movie = Movies(
            original_title=body.original_title,
            budget=body.budget,
            popularity=body.popularity,
            release_date=body.release_date,
            revenue=body.revenue,
            title=body.title,
            vote_average=body.vote_average,
            vote_count=body.vote_count,
            overview=body.overview,
            tagline=body.tagline,
            uid=body.uid,
            director_id=body.director_id
        )

        try:
            db.session.add(new_movie)
            db.session.commit()
        except IntegrityError:
            return make_response(jsonify({'msg': f"Request Body contains invalid director_id"}), 400)

        return make_response(jsonify({'msg': f"New movie with id {new_movie.id} has been created"}), 201)


@api.route('/movies/<int:id>')
class MovieREST(Resource):

    @api.response(200, model=movie_response_model, description='Success')
    @jwt_required()
    def get(self, id):
        movie = Movies.query.get_or_404(id)
        return marshal(movie, movie_response_model)

    @api.expect(movie_request_model)
    @jwt_required()
    @validate()
    def put(self, id, body: MovieRequestModel):
        movie_to_update = Movies.query.get_or_404(id)

        movie_to_update.original_title = body.original_title
        movie_to_update.budget = body.budget
        movie_to_update.popularity = body.popularity
        movie_to_update.release_date = body.release_date
        movie_to_update.revenue = body.revenue
        movie_to_update.title = body.title
        movie_to_update.vote_average = body.vote_average
        movie_to_update.vote_count = body.vote_count
        movie_to_update.overview = body.overview
        movie_to_update.tagline = body.tagline
        movie_to_update.uid = body.uid
        movie_to_update.director_id = body.director_id

        try:
            db.session.commit()
        except IntegrityError:
            return make_response(jsonify({'msg': f"Request Body contains invalid director_id"}), 400)

        return jsonify(msg='Update success')

    @jwt_required()
    def delete(self, id):
        movie_to_delete = Movies.query.get_or_404(id)
        db.session.delete(movie_to_delete)
        db.session.commit()
        return jsonify(msg='Delete success')
