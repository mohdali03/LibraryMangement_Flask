from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt, jwt_required

from libraryManagement.marsh import BookSchema
from ..model import Authors, Books
from .. import db

books = Blueprint('books', __name__, url_prefix='/books')

@books.route('/', methods=['POST', 'GET', 'PUT', 'DELETE'])
@jwt_required()
def book():
    claims = get_jwt()
    if not claims.get('is_admin', False):  
        return jsonify({'msg': "ADMIN is required"}), 400
    else:
        if request.method == 'POST':
            data = request.get_json()
            title = data.get('title')
            genre = data.get('genre')
            authors = data.get('author')
            
            book = Books.query.filter_by(title = title).first()
            if book:
                return {'msg': f'{book.title} is already taken'}, 400
            
            author = Authors.query.filter_by(name = authors).first()
            if not author:
                return {'msg': "Invalid the Author name "}, 400

            new_books = Books(title=title, genre=genre, author=author)
            db.session.add(new_books)
            db.session.commit()
            
            
            
            return {'msg': f'books is successfully add'}
        if request.method == 'PUT':
            data = request.get_json()
            old_title = data.get('old_title')
            new_title = data.get('new_title')
            genre = data.get('genre')
            author = data.get('author')
            book = Books.query.filter_by(title = old_title).first()
            if not book:
                return jsonify({'msg': f'Invalid Books title'}), 400
            
            if new_title  and new_title != old_title:
                if Books.query.filter_by(title = new_title).first() is not None:
                    return jsonify({'msg': f"{new_title} title is taken"}), 400
                book.title = new_title
            
            if genre :
                book.genre = genre
            
            if author:
                reg_author = Authors.query.filter_by(name=author).first()
                if not reg_author:
                    return jsonify({'msg': f'Author "{author}" does not exist in the database'}), 400
                book.author = reg_author
            db.session.commit()
            return jsonify({'msg': f'{new_title if new_title else old_title} is successfully updated'})
        if request.method == 'DELETE':
            
            title = request.args.get('title')
            
            book = Books.query.filter_by(title = title).first_or_404()
            
            db.session.delete(book)
            db.session.commit()
            
            return jsonify({'msg': 'books is succesfully deleted'})
    title = request.args.get('title')
    if title:
            book = Books.query.filter_by(title=title).first_or_404()
            book_schema = BookSchema()
            return book_schema.dump(book)  
    else:
            books = Books.query.all()
            books_schema = BookSchema(many=True)
            return books_schema.dump(books)  
    

            
            


            
        
    
