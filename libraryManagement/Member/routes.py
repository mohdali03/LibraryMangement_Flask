from flask import Blueprint

member = Blueprint('member', __name__, url_prefix='/member')

@member.route('/login', methods=['POST', 'GET'])
def login():
    return ""
@member.route('/logout', methods=['POST', 'GET'])
def logout():
    return ""

@member.route('/signup', methods=['POST', 'GET'])
def signup():
    return ""

