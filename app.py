import os
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from dotenv import load_dotenv
from sqlalchemy import select
import uuid
import json

from usersBP import users_bp, db, get_users_list
from userslistBP import users_list_bp
from policyBP import policy_bp
load_dotenv()  # load -> os env (environmental variables
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FORM_SECRET_KEY")
# General pattern
# mssql+pyodbc://<username>:<password>@<dsn_name>?driver=<driver_name>
connection_string = os.environ.get("AZURE_DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = connection_string
db.init_app(app)
 
try:
    with app.app_context():
        # Use text() to explicitly declare your SQL command
        result = db.session.execute(text("SELECT 1")).fetchall()
        print("Connection successful:", result)
except Exception as e:
    print("Error connecting to the database:", e)
 
app.register_blueprint(users_bp, url_prefix = "/users") 
app.register_blueprint(users_list_bp, url_prefix = "/usersList") 
app.register_blueprint(policy_bp, url_prefix = "/policies") 
@app.route("/")
def hello_world():
    return "<p>Hddsddqq, 🥹</p>"

@app.route("/admin")
def admin_page():
    #Get the users list
    users = get_users_list()
    print(users)
    return render_template("admin.html",users=users)

@app.get('/users/<id>')
def get_user(id):
    FoundUser = next((user for user in UserData if user['id']==int(id)),None)
    if FoundUser == None:
        error = {'message':'User Not found'}
        return jsonify(error),404
    return jsonify(FoundUser),200


# users = [
#   {
#       "id":12,
#     "balance": "$3,946.45",
#     "picture": "http://placehold.it/32x32",
#     "age": 23,
#     "name": "Bird Ramsey",
#     "gender": "male",
#     "company": "NIMON",
#     "email": "birdramsey@nimon.com"
#   },
#   {
#       "id":13,
#     "balance": "$2,499.49",
#     "picture": "http://placehold.it/32x32",
#     "age": 31,
#     "name": "Lillian Burgess",
#     "gender": "female",
#     "company": "LUXURIA",
#     "email": "lillianburgess@luxuria.com"
#   },
#   {
#       "id":14,
#     "balance": "$2,820.18",
#     "picture": "http://placehold.it/32x32",
#     "age": 34,
#     "name": "Kristie Cole",
#     "gender": "female",
#     "company": "QUADEEBO",
#     "email": "kristiecole@quadeebo.com"
#   },
#   {
#       "id":15,
#     "balance": "$3,277.32",
#     "picture": "http://placehold.it/32x32",
#     "age": 30,
#     "name": "Leonor Cross",
#     "gender": "female",
#     "company": "GRONK",
#     "email": "leonorcross@gronk.com"
#   },
#   {
#       "id":16,
#     "balance": "$1,972.47",
#     "picture": "http://placehold.it/32x32",
#     "age": 28,
#     "name": "Marsh Mccall",
#     "gender": "male",
#     "company": "ULTRIMAX",
#     "email": "marshmccall@ultrimax.com"
#   }
# ]
