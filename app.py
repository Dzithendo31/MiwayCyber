import os
from flask_login import login_required, logout_user
from flask import Flask, jsonify, redirect, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from dotenv import load_dotenv
from models.user import User
from policyBP import Policy
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
connection_string = os.environ.get("LOCAL_DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = connection_string
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



 
app.register_blueprint(users_bp) 
app.register_blueprint(users_list_bp, url_prefix = "/usersList") 
app.register_blueprint(policy_bp, url_prefix = "/policies") 
app.register_blueprint(adminBP, url_prefix = "/admin") 
@app.route("/")
def home():
    allPolicy = Policy.query.all()  # Select * from movies | movie_list iterator
    data2 = [policy.to_dict() for policy in allPolicy]  # list of dictionaries
    return render_template("index.html", policies = data2)

try:
    with app.app_context():
        # Use text() to explicitly declare your SQL command
        result = db.session.execute(text("SELECT 1")).fetchall()
        print("Connection successful:", result)
        #db.drop_all()
        #db.create_all()
except Exception as e:
    print("Error connecting to the database:", e)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))