import os
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from dotenv import load_dotenv
from models.user import User

from usersBP import users_bp
from userslistBP import users_list_bp
from policyBP import policy_bp
from adminBP import adminBP

#Import the DB
from extensions import db
from flask_login import LoginManager
load_dotenv()  # load -> os env (environmental variables
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FORM_SECRET_KEY")
# General pattern
# mssql+pyodbc://<username>:<password>@<dsn_name>?driver=<driver_name>
connection_string = os.environ.get("AZURE_DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = connection_string
db.init_app(app)

login_manager = LoginManager()


login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


try:
    with app.app_context():
        # Use text() to explicitly declare your SQL command
        result = db.session.execute(text("SELECT 1")).fetchall()
        print("Connection successful:", result)
except Exception as e:
    print("Error connecting to the database:", e)
 
app.register_blueprint(users_bp) 
app.register_blueprint(users_list_bp, url_prefix = "/usersList") 
app.register_blueprint(policy_bp, url_prefix = "/policies") 
app.register_blueprint(adminBP, url_prefix = "/admin") 
@app.route("/")
def home():
    return render_template("index.html")


@app.get('/users/<id>')
def get_user(id):
    FoundUser = next((user for user in UserData if user['id']==int(id)),None)
    if FoundUser == None:
        error = {'message':'User Not found'}
        return jsonify(error),404
    return jsonify(FoundUser),200
