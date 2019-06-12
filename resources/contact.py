from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
from flask_cors import cross_origin
from models.contact import ContactModel


class Contact(Resource):
    
    parser = reqparse.RequestParser()

    parser.add_argument("first_name",
                type=str,
                required=True,
                help="This field cannot be left blank")
    
    parser.add_argument("last_name",
                type=str,
                required=True,
                help="This field cannot be left blank")
    
    parser.add_argument("phone_number",
                type=str,
                required=True,
                help="This field cannot be left blank")


    @jwt_required()
    def get(self):
        return {"data": [contact.json() for contact in ContactModel.get_contacts(current_identity.id)]}


    @jwt_required()
    def post(self):
        contact_data = Contact.parser.parse_args()

        new_contact = ContactModel(contact_data["first_name"], contact_data["last_name"], contact_data["phone_number"], current_identity.id)

        new_contact.save_to_db()

        return new_contact.json(), 201