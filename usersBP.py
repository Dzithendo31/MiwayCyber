from flask import Flask, jsonify, request, render_template, Blueprint,redirect, url_for
from flask_login import login_required, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
import flask
from extensions import db
from models.user import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email,ValidationError
users_bp = Blueprint('users_bp',__name__)

#Lets do get users
@users_bp.get("/users")
def get_users():
    allUsers = User.query.all()  # Select * from movies | movie_list iterator
    UserData = [user.to_dict() for user in allUsers]  # list of dictionaries
    return jsonify(UserData)

def get_users_list():
    allUsers = User.query.all()  # Select * from movies | movie_list iterator
    UserData = [user.to_dict() for user in allUsers]  # list of dictionaries
    return UserData

#an dd user route for the json
@users_bp.get("/users/<id>")
def get_user(id):
    filtered_user = User.query.get(id)
    if filtered_user:
        data = filtered_user.to_dict()
        return jsonify(data)
    else:
        return jsonify({"message": "User not found"}), 404
    
#Now the actual path for 
@users_bp.delete('/users/<id>')
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
    
@users_bp.put("/users/<id>")
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
@users_bp.post("/users/")
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
    
class RegistrationForm(FlaskForm):

    firstname = StringField('firstname', validators=[InputRequired(), Length(min=3)])
    lastname = StringField('lastname', validators=[InputRequired(), Length(min=3)])
    date_of_birth = StringField('Date of Birth', validators=[InputRequired()])
    phone = StringField('Phone', validators=[InputRequired(), Length(min=10, max=12)])
    email = StringField('Email', validators=[InputRequired(), Email()])
    address = StringField('Address', validators=[InputRequired(), Length(min=5)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=12)])
    gender = StringField('Gender', validators=[InputRequired(), Length(min=4, max=6)])
    
    submit = SubmitField("Sign up")

    #the method will automatically run when  form.validate_on_submit() is run
    def validate_username(self,field):
        print("Validate Username",field.data)
        if User.query.filter(User.first_name == field.data).first():
            raise ValidationError("Username is taken")
        
@users_bp.route("/register", methods =["GET","POST"])  # HOF
def register_page():
    #Create a new ......?
    form = RegistrationForm()
    #So the method is bothe a get, and a post, only submit when its a post
    if form.validate_on_submit():
        new_user = User(
            first_name=form.firstname.data,
            last_name=form.lastname.data,
            date_of_birth=form.date_of_birth.data,
            phone=form.phone.data,
            email=form.email.data,
            address=form.address.data,
            password=form.password.data,
            gender=form.gender.data
            )
        #try connect to database
        try:
            db.session.add(new_user)
            db.session.commit()
            message ={
                "message":"User Added Successfully.",
                "success":True,
                "data":new_user
            }
            return render_template("success.html",message=message)
        except Exception as e:
            db.session.rollback()
            message ={
            "message":"Error Adding User to DB.",
            "success":False,
            "data":str(e)
        }
            return render_template("success.html",message=message)
    return render_template("register.html", form =form)

# Log In Logic
class LoginForm(FlaskForm):
    #Second Parameter is the type of Validations
    firstname = StringField('firstname', validators=[InputRequired(), Length(min=3)])
    lastname = StringField('lastname', validators=[InputRequired(), Length(min=3)])
    password = PasswordField('Password',validators=[InputRequired()])
    submit = SubmitField("Log In")

    #the method will automatically run when  form.validate_on_submit() is run
    def validate_username(self,field):
        user_from_db = User.query.filter(User.first_name == field.data).first()
        if not user_from_db:
            raise ValidationError("Invalid Credentitals")
        
    def validate_password(self,field):
        user_from_db = User.query.filter(User.first_name == field.data).first()
        if user_from_db:
          user_db_data = user_from_db.to_dict()
          formPassword = field.data
          print(user_db_data, formPassword)
          if  user_db_data["password"] != formPassword:
              raise ValidationError("Invalid Credentials")




@users_bp.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(first_name=form.firstname.data).first()
        if user:
            login_user(user)#Token is Stored in the browser.
            flask.flash('Logged in successfully.')
            # Redirect to the next page if available, otherwise to the home page
            next_page = flask.request.args.get('next') or url_for('adminBP.user_list_page')
            return redirect(next_page)
        else:
            flask.flash('Invalid username or password.', 'error')
    return render_template("login.html", form=form)