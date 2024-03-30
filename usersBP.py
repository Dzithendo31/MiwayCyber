from flask import Flask, jsonify, request, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()
users_bp = Blueprint('users_bp',__name__)
UserData = []
class User(db.Model):
    __tablename__ = "users2"
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
@users_bp.get("/")
def get_users():
    allUsers = User.query.all()  # Select * from movies | movie_list iterator
    UserData = [user.to_dict() for user in allUsers]  # list of dictionaries
    return jsonify(UserData)

def get_users_list():
    allUsers = User.query.all()  # Select * from movies | movie_list iterator
    UserData = [user.to_dict() for user in allUsers]  # list of dictionaries
    return UserData

#an dd user route for the json
@users_bp.get("/<id>")
def get_user(id):
    filtered_user = User.query.get(id)
    if filtered_user:
        data = filtered_user.to_dict()
        return jsonify(data)
    else:
        return jsonify({"message": "User not found"}), 404
    
#Now the actual path for 
@users_bp.delete('/<id>')
def delete_user(id):
    user_delete = User.query.get(id)
    if not user_delete:
        #Catch the client Side error
        error = {'message':'User Not found'}
        return jsonify(error),404
    try:
        data = user_delete.to_dict()
        db.session.delete(user_delete)
        #Then you commit
        db.session.commit()
        return jsonify({"message": "Deleted Successfully", "data": data})
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 500
    
@users_bp.put("/<id>")
def update_user_by_id(id):
    filtered_user = User.query.get(id)
    if not filtered_user:
        return jsonify({"message": "User not found"}), 404
    body = request.json  # user

    try:
        for key, value in body.items():
            #Check if the User has the specified Key
            if hasattr(filtered_user, key):
                #Set the Vlaue to the new Updated vlaue
                setattr(filtered_user, key, value)
        db.session.commit()
        return jsonify(
            {"message": "User updated successfully!", "data": filtered_user.to_dict()}
        )
    except Exception as e:
        db.session.rollback()  # Undo the change
        return jsonify({"message": str(e)}), 500
 
 
# Handle the error scenario
@users_bp.post("/")
def create_movies():
    data = request.json  # body
    new_movie = User(**data)
    try:
        db.session.add(new_movie)
        db.session.commit()
        # movies.append(new_movie)
        result = {"message": "Added successfully", "data": new_movie.to_dict()}
        return jsonify(result), 201
    except Exception as e:
        db.session.rollback()  # Undo the change
        return jsonify({"message": str(e)}), 500