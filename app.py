from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
app = Flask(__name__)


app.config.from_object(Config)
db =  SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    
    publication_date = db.Column(db.Date, nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)

    # author = db.relationship('Author', back_populates='books')

class Authors(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(100), nullable=False)
    biography = db.Column(db.String(100), nullable= False)
    dob = db.Column(db.Date,nullable= True)
    books = db.relationship('Book', back_populates='author')
    

class LibraryMembers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(100), nullable= False)
    is_active = db.Column(db.Boolean, default = True, nullable=False)


app.register_blueprint('/books', book)
    

if __name__ == '__main__':
    app.run(debug=True)