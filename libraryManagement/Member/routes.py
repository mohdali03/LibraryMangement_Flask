from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt, jwt_required

from libraryManagement.marsh import LibraryMemberSchema as Member_schema
from ..model import LibraryMembers as Members
from .. import db


member = Blueprint('member', __name__, url_prefix='/member')

@member.route('/', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def profile():
    claims = get_jwt()
    name = request.args.get('name')

    if not claims.get('is_admin', False):  
        return jsonify({'msg': "ADMIN is required"}), 400
    else:
        if request.method == 'PUT':
            data = request.get_json()
            old_name = data.get("old_name")
            name = data.get('new_name')
            contact = data.get('contact')
            is_admin = data.get('is_admin')
            is_active = data.get('is_active')
            members = Members.query.filter_by(name= old_name).first()
            
            if not members:
                return jsonify({'msg': "member is invalid "})
            
            if name and name != old_name:
                if Members.query.filter_by(name= name).first() is not None:
                    return jsonify({'msg': 'Name is already taken '}), 404
                members.name = name
            
            if contact:
                members.contact =  contact
            if 'is_admin' in data:
                members.is_admin = is_admin
            if 'is_active' in data:
                members.is_active = is_active
            
            db.session.commit()
            return jsonify({"msg": f"{name if name else old_name} is updated"})
        if request.method == 'DELETE':
            members = Members.query.filter_by(name = name).first_or_404()
            
            db.session.delete(members)
            db.session.commit()
            return jsonify({'msg': f'{members.name}successfully deleted'})
            
                
            
            
    
    if name: 
        member = Members.query.filter_by(name= name).first_or_404()
        member_schema = Member_schema()
        return member_schema.dump(member)
    else:
        member = Members.query.all()
        members_schema = Member_schema(many=True)
        return members_schema.dumps(member)

   