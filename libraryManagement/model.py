from datetime import datetime



from . import db



class LibraryMembers(db.Model):
    __tablename__ = 'library_members'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(100), nullable= False)
    is_active = db.Column(db.Boolean, default = True, nullable=False)
    register_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    password = db.Column(db.String(250), nullable=False)
    is_admin = db.Column(db.Boolean, default = False, nullable=False)
    def __init__(self, name, contact, password) -> None:
        self.name = name
        self.contact = contact
        self.password = password


      
class Authors(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(100), nullable=False)
    biography = db.Column(db.String(100), nullable= False)
    dob = db.Column(db.Date,nullable= True)
    books = db.relationship('Books', backref='author')
    

class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    
    publication_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    genre = db.Column(db.String(50), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
