from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.db"
db = SQLAlchemy(app)
api = Api(app)


class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f"<User (name = {self.name}, email = {self.email})>"


user_args = reqparse.RequestParser()
user_args.add_argument("name", type=str, help="Name of the user", required=True)
user_args.add_argument("email", type=str, help="Email of the user", required=True)

userFields = {"id": fields.Integer, "name": fields.String, "email": fields.String}


class Users(Resource):
    @marshal_with(userFields)
    def get(self):
        users = UserModel.query.all()
        if not users:
            abort(404, message="User not found")
        return users

    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()
        new_user = UserModel(name=args["name"], email=args["email"])
        db.session.add(new_user)
        db.session.commit()
        return new_user, 201


class User(Resource):
    @marshal_with(userFields)
    def get(self, user_id):
        user = UserModel.query.get(user_id)
        if not user:
            abort(404, message="User not found")
        return user

    @marshal_with(userFields)
    def put(self, user_id):
        args = user_args.parse_args()
        user = UserModel.query.get(user_id)
        if not user:
            abort(404, message="User not found")
        user.name = args["name"]
        user.email = args["email"]
        db.session.commit()
        return user

    def delete(self, user_id):
        user = UserModel.query.get(user_id)
        if not user:
            abort(404, message="User not found")
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}, 204


api.add_resource(Users, "/api/users/", "/api/users/<int:user_id>", "/api/users")
api.add_resource(User, "/api/user/<int:user_id>")


@app.route("/api/home", methods=["GET"])
def home():
    name = request.args.get("name", "World")
    return jsonify(message=f"Hello, {name}!")


if __name__ == "__main__":
    app.run(debug=True)
# Note: Replace "
