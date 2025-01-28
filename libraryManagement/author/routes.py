import datetime
from flask import Blueprint, jsonify, make_response, request
from flask_jwt_extended import get_jwt, jwt_required
from flask_restful import Api, Resource

from libraryManagement.marsh import AuthorSchema
from .. import db
from libraryManagement.model import Authors

author = Blueprint('author', __name__, url_prefix='/author')
api = Api(author)

class Author(Resource):

    @jwt_required()
    def get(self):
        name = request.args.get('name')
        if name:
            author = Authors.query.filter_by(name=name).first()
            authors_schema = AuthorSchema()
            return authors_schema.dump(author)  
        else:
            authors = Authors.query.all()
            authors_schema = AuthorSchema(many=True)
            return authors_schema.dump(authors)  
    
    @jwt_required()
    def post(self):
        claims = get_jwt()
        if not claims.get('is_admin', False):  
            return jsonify({'msg': 'Admin is required to access this'}), 403

        data = request.get_json()



        name = data.get('name')
        biography = data.get('biography')
        dob_str = data.get('dob')

        if not name or not biography:
            return jsonify({"msg": "name and biography are required"}), 400
        
        author = Authors.query.filter_by(name=name).first()
        if not author:
            dob = None
            if dob_str:
                try:
                    dob = datetime.datetime.strptime(dob_str, '%Y-%m-%d').date()  
                except ValueError:
                    return jsonify({"msg": "Invalid date format. Use YYYY-MM-DD"}), 400
            
            author = Authors(name=name, biography=biography, dob=dob) #type:ignore
            db.session.add(author)
            db.session.commit()

            print("Author Created:", author)

            author_schema = AuthorSchema()
            return jsonify({'msg': f'{author.name} is successfully registered', 'author': author_schema.dump(author)}), 200
        
        
        return  f"{author.name} name is already taken"

    @jwt_required()
    def put(self):
        data = request.get_json()
        claims = get_jwt()
        if not claims.get('is_admin', False):
            return {'msg': 'To access this Admin is required'}, 403
        
        new_name = data.get('new_name')
        old_name = data.get('old_name')
        biography = data.get('biography')
        dob = data.get('dob')
        
        author = Authors.query.filter_by(name=old_name).first()
        
        if not author:
            return {"msg": "Invalid the old name"}, 400
        
        if new_name and new_name != old_name:
            if Authors.query.filter_by(name=new_name).first() is not None:

                return {"msg": "Author name is already taken"},400
            author.name = new_name
        if biography:
            author.biography = biography
        if dob:
            try:
                    dob = datetime.datetime.strptime(dob, '%Y-%m-%d').date()  
                    author.dob = dob
            except ValueError:
                    return jsonify({"msg": "Invalid date format. Use YYYY-MM-DD"}), 400
        
        db.session.commit()
        
        return {'msg': f"{new_name if new_name else old_name} Author is successfully updated"}

    @jwt_required()
    def delete(self):
        claims = get_jwt()
        if not claims.get('is_admin'):
            return jsonify({'msg': 'Admin is required to access this'}), 403
        
        name = request.args.get('name')
        
        if not name:
            return jsonify({"msg": "Name parameter is required"}), 400
        
        author = Authors.query.filter_by(name=name).first()
        
        if not author:
            return jsonify({"msg": "Author not found"}), 404
        
        db.session.delete(author)
        db.session.commit()
        
        return jsonify({'msg': f'{name} is successfully deleted'})

api.add_resource(Author, '/')
