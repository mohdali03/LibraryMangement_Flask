from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from marshmallow import fields
from .model import LibraryMembers, Books, Authors

class LibraryMemberSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = LibraryMembers
        include_relationships = True
        load_instance = True 
class AuthorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Authors
        include_relationships = True
        load_instance = True 

class BookSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Books
        include_relationships = True
        load_instance = True  

    # Use Nested to serialize the related author
    author = fields.Nested(AuthorSchema)
