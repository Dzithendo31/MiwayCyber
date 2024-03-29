from flask import Flask, jsonify, request, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()
movies_bp = Blueprint('movies',__name__)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    date_of_birth = db.Column(db.String(100))  # Assuming you meant "date of birth"
    phone = db.Column(db.String(100))
    email = db.Column(db.String(100))
    address = db.Column(db.String(100))
    password = db.Column(db.String(100))

    # JSON - Keys
    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
            "password": self.password
        }
    

#Lets do get users
@movies_bp.get("/")
def get_users():
    allUsers = User.query.all()  # Select * from movies | movie_list iterator
    data = [user.to_dict() for user in allUsers]  # list of dictionaries
    return jsonify(data)