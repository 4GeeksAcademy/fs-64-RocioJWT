"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint 
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/signup', methods=['POST'])
def handle_sign():
    request_body= request.json
    user_query= User.query.filter_by(email=request_body["email"]).first()
    if user_query is None:
        create_user= User(email=request_body["email"], password=request_body["password"], is_active=request_body["is_active"])
        db.session.add(create_user)
        db.session.commit()
        response_body= {
            "message":"usuario creado en éxito"
        }
        return jsonify(response_body), 200
    else:
        response_body= {
            "message": "el usuario ya existe"
        }
        return jsonify(response_body), 404

    #     @api.route('/signup', methods=['POST'])
    # def handle_sign():
    # request_body= request.json
    # user_query= User.query.filter_by(email=request_body["email"]).first()
    # if user_query is None:
    #     create_user= User(email=request_body["email"], password=request_body["password"], is_active=request_body["is_active"])
    #     db.session.add(create_user)
    #     db.session.commit()
    #     response_body= {
    #         "message":"usuario creado en éxito"
    #     }
    #     return jsonify(response_body), 200
    # else:
    #     response_body= {
    #         "message": "el usuario ya existe"
    #     }
    #     return jsonify(response_body), 404


@api.route('/login', methods=['POST'])
def handle_login():
    request_body= request.json
    email=request_body.get("email")
    password=request_body.get("password")
    user_login= User.query.filter_by(email=request_body["email"]).first()
    if user_login is None:
        response_body={"message": "not found"} 
        return jsonify(response_body), 404
    elif email !=user_login.email or password !=user_login.password:
        return jsonify( {
            "message": "usuario y/o contraseña incorrectas"

        }), 404
    else:
        access_token=create_access_token(identity=user_login.id)
        return jsonify ({
            "token":access_token,
            "user_id":user_login.id
        })
    
       
      

@api.route('/signup', methods=['POST'])
def handle_sign():
    request_body= request.json
    user_query= User.query.filter_by(email=request_body["email"]).first()
    if user_query is None:
        create_user= User(email=request_body["email"], password=request_body["password"], is_active=request_body["is_active"])
        db.session.add(create_user)
        db.session.commit()
        response_body= {
            "message":"usuario creado en éxito"
        }
        return jsonify(response_body), 200
    else:
        response_body= {
            "message": "el usuario ya existe"
        }
        return jsonify(response_body), 404







    


    

