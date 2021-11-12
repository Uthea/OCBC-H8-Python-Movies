from flask import jsonify, request
from flask_jwt_extended import jwt_required
from flask_pydantic import validate
from flask_restx import Resource, Namespace

from skeleton import db
from skeleton.api_model import book_model, book_post_model
from skeleton.model import Book
from skeleton.pydantic_model import RequestBodyModel

api = Namespace('Books', description='CRUD Books', path='/')


@api.route('/book')
class Books(Resource):

    @api.marshal_list_with(book_model, code=200, envelope="books")
    @jwt_required()
    def get(self):
        books = Book.query.all()
        return books

    # @api.marshal_with(book_model, code=201)
    @api.expect(book_post_model)
    @validate()
    @jwt_required()
    def post(self, body: RequestBodyModel):
        title = body.title
        author = body.author
        new_book = Book(title=title, author=author)

        db.session.add(new_book)
        db.session.commit()

        return jsonify({'msg': 'New book has been created'})


@api.route('/book/<int:id>')
class BookResource(Resource):

    @api.marshal_with(book_model, code=200, envelope="book")
    @jwt_required()
    def get(self, id):
        book = Book.query.get_or_404(id)
        return book

    @api.marshal_with(book_model, code=200, envelope="book")
    @api.expect(book_model)
    @jwt_required()
    def put(self, id):
        book_to_update = Book.query.get_or_404(id)

        data = request.get_json()

        book_to_update.title = data.get('title')
        book_to_update.author = data.get('author')
        db.session.commit()

        return book_to_update

    @api.marshal_with(book_model, envelope="book_deleted", code=200)
    @jwt_required()
    def delete(self, id):
        book_to_delete = Book.query.get_or_404(id)
        db.session.delete(book_to_delete)
        db.session.commit()
        return book_to_delete
