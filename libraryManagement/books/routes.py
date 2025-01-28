from flask import Blueprint, request

books = Blueprint('books', __name__, url_prefix='/books')

@books.route('/', methods=['POST', 'GET', 'PUT', 'DELETE'])
def book():
    if request.method == 'POST':
        data = request.get_json()
        
        
        return ""
    
    return ""