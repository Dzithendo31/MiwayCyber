from flask import Flask, jsonify, request, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy
from models.user import User
from extensions import db
from userPolicyBP import UserPolicy
from policyBP import Policy
from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField
from wtforms.validators import InputRequired, ValidationError

adminBP = Blueprint('adminBP',__name__)

#This URL is resticted only to the admin Site only.
@adminBP.route("/")  # HOF
def user_list_page():
    user_list = User.query.all()  # Select * from movies | movie_list iterator
    data = [user.to_dict() for user in user_list]  # list of dictionaries

    #Get your policies
    allPolicy = Policy.query.all()  # Select * from movies | movie_list iterator
    data2 = [policy.to_dict() for policy in allPolicy]  # list of dictionaries
    return render_template("admin.html", users=data,policies=data2)
 
@adminBP.route("/user/<id>")  # HOF
def user_detail_page(id):
    filtered_user = User.query.get(id)
    #Then you can query the Policies Database base on the ID to find the client's polices
    user_policies = UserPolicy.query.filter_by(userID=id).all()

    pols = policyNames(user_policies)
    #Add the polic Names

    if filtered_user:
        data = filtered_user.to_dict()
        return render_template("userdetailsAdmin.html", user=data,policies =pols)
    else:
        return "<h1>Movie not found</h1>" 
def policyNames(user_policies):
    newList =[]
    for Userpolicy in user_policies:
        Userpolicy_dict = Userpolicy.to_dict()
        #get the policy
        policy = Policy.query.filter_by(id=Userpolicy.policyID).first()
        Userpolicy_dict['name'] = policy.name
        Userpolicy_dict['description'] = policy.description
        newList.append(Userpolicy_dict)

    return newList


@adminBP.route("/policy/<id>")  # HOF
def policy_detail_page(id):
    filtered_policy = Policy.query.get(id)
    #Then you can query the Policies Database base on the ID to find the client's polices

    if filtered_policy:
        data = filtered_policy.to_dict()
        return render_template("policydetailsAdmin.html", policy=data,user="admin")
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
      db.session.add(new_user)
      db.session.commit()
      message ={
          "message":"User Added Successfully.",
          "success":True,
          "data":new_user_data
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
    

# Adding a New Policy
class PolicyRegistrationForm(FlaskForm):

    policyName = StringField('policyName', validators=[InputRequired()])
    description = StringField('description', validators=[InputRequired()])
    basePremium = StringField('basePremium', validators=[InputRequired()])
    baseCoverge = StringField('baseCoverge', validators=[InputRequired()])
    pictureURL = StringField('imageURL', validators=[InputRequired()])
    
    submit = SubmitField("Sign up")

    #the method will automatically run when  form.validate_on_submit() is run
    def validate_policyName(self, field):
        if Policy.query.filter_by(name=field.data).first():
            raise ValidationError("This policy name is already in use. Please choose a different one.")


@adminBP.route("/register", methods =["GET","POST"])
def register_policy_page():
    
    form = PolicyRegistrationForm()

    if form.validate_on_submit():
        new_policy = Policy(
            name=form.policyName.data,
            description=form.description.data,
            basePremium=form.basePremium.data,
            baseCoverage=form.baseCoverge.data,
            pictureURL=form.pictureURL.data
        )
        try:
            db.session.add(new_policy)
            db.session.commit()
            message ={
                "message":"New Policy Created Successfully.",
                "success":True,
                "action":"View Profile",
                "URL": f"policy/{new_policy.id}",
                "data":new_policy
            }
            return render_template("success.html",message=message)
        except Exception as e:
            db.session.rollback()
            message ={
            "message":"Error Adding Policy to DB.",
            "success":False,
            "data":str(e)
        }
            return render_template("success.html",message=message)
    return render_template("register.html", form =form)
