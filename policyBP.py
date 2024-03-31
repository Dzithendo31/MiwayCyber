from flask import Flask, jsonify, request, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy
import uuid
from usersBP import db


policy_bp = Blueprint('policy_bp',__name__)


class Policy(db.Model):
    __tablename__ = "policies"
    id = db.Column(db.String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    basePremium = db.Column(db.String(100))  # Assuming you meant "date of birth"
    baseCoverage = db.Column(db.String(100))
    pictureURL = db.Column(db.String(100))

    # JSON - Keys
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "basePremium": self.basePremium,
            "baseCoverage": self.baseCoverage,
            "pictureURL": self.pictureURL
        }
    
#Lets do get users
@policy_bp.get("/")
def get_policies():
    allPolicy = Policy.query.all()  # Select * from movies | movie_list iterator
    data = [policy.to_dict() for policy in allPolicy]  # list of dictionaries
    return jsonify(data)


def get_policies_list():
    allPolicy = Policy.query.all()  # Select * from movies | movie_list iterator
    data = [policy.to_dict() for policy in allPolicy]  # list of dictionaries
    return data