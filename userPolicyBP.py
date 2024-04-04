from flask import Flask, jsonify, request, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy
import uuid
from extensions import db


User_policy_bp = Blueprint('User_policy_bp',__name__)


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