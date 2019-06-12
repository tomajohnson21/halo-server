from db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(100))
    contacts = db.relationship("ContactModel")


    def __init__(self, username, password):
        self.username = username
        self.password = password


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()


    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    # def set_password(self, password):
    #     self.pw_hash = generate_password_hash(password)

    # def check_password(self, password):
    #     return check_password_hash(self.pw_hash, password)