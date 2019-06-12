from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("username",
                type=str,
                required=True,
                help="This field cannot be left blank")

    parser.add_argument("password",
                type=str,
                required=True,
                help="This field cannot be left blank")


    # def set_password(self, password):
    #     self.pw_hash = generate_password_hash(password)


    def post(self):
        user_data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(user_data["username"]):
            return {"message": "A user with this username already exists"}, 400

        user = UserModel(**user_data)

        user.save_to_db()

        return {"message": "User created successfully"}, 201