from flask import Flask, jsonify, request, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy
from usersBP import User, db
from policyBP import Policy


adminBP = Blueprint('adminBP',__name__)

#This URL is resticted only to the admin Site only.
@adminBP.route("/")  # HOF
def user_list_page():
    user_list = User.query.all()  # Select * from movies | movie_list iterator
    data = [user.to_dict() for user in user_list]  # list of dictionaries

    #Get your policies
    allPolicy = Policy.query.all()  # Select * from movies | movie_list iterator
    data2 = [policy.to_dict() for policy in allPolicy]  # list of dictionaries
    print(data2)
    return render_template("admin.html", users=data,policies=data2)
 
@adminBP.route("/<id>")  # HOF
def movie_detail_page(id):
    filtered_user = User.query.get(id)
    #Then you can query the Policies Database base on the ID to find the client's polices

    if filtered_user:
        data = filtered_user.to_dict()
        return render_template("userdetailsAdmin.html", user=data)
    else:
        return "<h1>Movie not found</h1>" 
    

@adminBP.route("/addUser", methods=["GET"])
def addUserAdmin():
    return render_template("addUser.html")

@adminBP.route("/success", methods=["POST"])  # HOF
def create_user():
    # Get user data from the request form
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    date_of_birth = request.form.get("date_of_birth")
    phone = request.form.get("phone")
    email = request.form.get("email")
    address = request.form.get("address")
    password = request.form.get("password")

    # Create a new user object
    new_user_data = {
        "first_name": first_name,
        "last_name": last_name,
        "date_of_birth": date_of_birth,
        "phone": phone,
        "email": email,
        "address": address,
        "password": password
    }

    new_user = User(**new_user_data)
    try:
      print('Tryign to addddd')
      db.session.add(new_user)
      db.session.commit()
      print('doneeeeeeeeee???')
      return "<h1>Movie added Successfully</h1>"
    except Exception as e:
        db.session.rollback()
        return f"<h1>Error adding Movie: {str(e)}</h1>"