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


class UserResource(Resource):
    def get(self, user_id):
        user = UserModel.query.get(user_id)
        if not user:
            abort(404, message="User not found")
        return {"id": user.id, "name": user.name, "email": user.email}

    @marshal_with({"id": fields.Integer, "name": fields.String, "email": fields.String})
    def post(self):
        args = user_args.parse_args()
        new_user = UserModel(name=args["name"], email=args["email"])
        db.session.add(new_user)
        db.session.commit()
        return new_user, 201


api.add_resource(UserResource, "/api/users/<int:user_id>", "/api/users")


@app.route("/api/home", methods=["GET"])
def home():
    name = request.args.get("name", "World")
    return jsonify(message=f"Hello, {name}!")


if __name__ == "__main__":
    app.run(debug=True)
# Note: Replace "
