from db import db

class ContactModel(db.Model):
    __tablename__ = 'contacts'

    id = id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    phone_number = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("UserModel")


    def __init__(self, first_name, last_name, phone_number, user_id):

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.user_id = user_id
    

    def json(self):

        return {"first_name": self.first_name, "last_name": self.last_name, "phone_number": self.phone_number, "user_id": self.user_id}


    @classmethod
    def get_contacts(cls, user_id):
        return cls.query.filter_by(user_id=user_id)


    def save_to_db(self):

        db.session.add(self)
        db.session.commit()