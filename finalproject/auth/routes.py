from flask import jsonify, make_response
from flask_jwt_extended import create_access_token, create_refresh_token, decode_token, get_jti
from flask_pydantic import validate
from flask_restx import Resource, Namespace
from werkzeug.security import generate_password_hash, check_password_hash

from finalproject import db
from finalproject.auth.api_model import register_model, login_model, refresh_model
from finalproject.auth.model import User, Tokenlist
from finalproject.auth.pydantic_model import RegisterBodyModel, LoginBodyModel, RefreshBodyModel

api = Namespace('Auth', description='auth related operations', path='/auth')


# # Callback function to check if a JWT exists in the database blocklist
# @jwt.token_in_blocklist_loader
# def check_if_token_revoked(jwt_header, jwt_payload):
#     jti = jwt_payload["jti"]
#     token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()
#     print(token)
#     return token is not None


@api.route('/login')
class Login(Resource):
    @api.expect(login_model)
    @validate()
    def post(self, body: LoginBodyModel):
        email = body.email
        password = body.password

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            return make_response(jsonify({'msg': 'Wrong Email or Password'}), 400)

        access_token = create_access_token(identity=email)
        refresh_token = create_refresh_token(identity=email)

        token = Tokenlist(jti=get_jti(access_token), refresh_token=refresh_token, used=False)

        db.session.add(token)
        db.session.commit()

        return jsonify(access_token=access_token, refresh_token=refresh_token)


@api.route('/register')
class Register(Resource):
    @api.expect(register_model)
    @validate()
    def post(self, body: RegisterBodyModel):
        email = body.email
        username = body.username
        password = body.password

        user = User.query.filter_by(email=email).first()

        if user:
            return make_response(jsonify({'msg': f"Email {email} already exist in db"}), 400)

        new_user = User(email=email, username=username, password=generate_password_hash(password))

        db.session.add(new_user)
        db.session.commit()

        return jsonify({'msg': "Register Succeed !"})


@api.route('/refreshToken')
class RefreshToken(Resource):
    @api.expect(refresh_model)
    @validate()
    def post(self, body: RefreshBodyModel):
        access_token = body.access_token
        refresh_token = body.refresh_token

        decoded_access_token = decode_token(access_token)  # will return 401 if token expired

        identity = decoded_access_token['sub']
        jti = decoded_access_token['jti']

        result = Tokenlist.query.filter_by(jti=jti).first()

        if result:
            if result.used:
                return make_response(jsonify(msg='Refresh Token already used'), 400)
            elif result.refresh_token != refresh_token:
                return make_response(jsonify(msg='Access Token and Refresh Token doesnt Match'), 400)
            else:
                result.used = True

                new_access_token = create_access_token(identity=identity)
                new_refresh_token = create_refresh_token(identity=identity)

                token = Tokenlist(jti=get_jti(new_access_token), refresh_token=new_refresh_token, used=False)

                db.session.add(token)
                db.session.commit()

                return jsonify(access_token=new_access_token, refresh_token=new_refresh_token)
        else:
            return make_response(jsonify(msg='Access Token not found'), 400)
