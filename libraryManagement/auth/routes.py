import datetime
from flask import Blueprint, jsonify, request
from ..model import LibraryMembers
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db

from flask_jwt_extended import (create_access_token, get_jwt, jwt_required, 
                                set_access_cookies, unset_access_cookies)

auth = Blueprint('auth', __name__, url_prefix='/auth')
BLOCKLIST = set()

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    member = LibraryMembers.query.filter_by(name = data['name']).first()
    
    if member :
        if check_password_hash( member.password,data['password']):
     
            token = create_access_token(identity=str(member.id), additional_claims={'is_admin': member.is_admin, 'name': member.name}, expires_delta=datetime.timedelta(hours=1))
            res=  jsonify(access_token=token)
            set_access_cookies(res, token)
            return res, 200
        else:
            return jsonify({'msg': 'invalid the  password'}), 400
    else:
            return jsonify({'msg': 'invalid the  user'}), 400
    
@auth.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    res = jsonify({'msg': 'successfully logout'})
    unset_access_cookies(res)
    return res, 200

@auth.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    if not data:
        return jsonify({'msg': 'No input data provided'}), 400

    name = data.get("name")
    password = data.get('password')
    contact = data.get('contact')

    if not name or not password or not contact:
        return jsonify({'msg': 'Missing required parameters'}), 400

    user = LibraryMembers.query.filter_by(name=name).first()
    if len(password) < 7:
        return jsonify({'msg': "Password is too short"}), 400
    
    if user: 
        return jsonify({'msg': 'This Username is Taken. Please choose a different'}), 400
    
    hashpassword = generate_password_hash(password)
    user = LibraryMembers(name, contact, hashpassword)
    db.session.add(user)
    db.session.commit()
    
    return jsonify({"success": f"{user.name} User is successfully registered"}), 201
    

        





