from extensions import db
import uuid
from flask_login import UserMixin

class User(UserMixin,db.Model):
    __tablename__ = "users2"
    id = db.Column(db.String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    date_of_birth = db.Column(db.String(100))  # Assuming you meant "date of birth"
    phone = db.Column(db.String(100))
    email = db.Column(db.String(100))
    address = db.Column(db.String(100))
    password = db.Column(db.String(100))
    gender = db.Column(db.String(10))  # Assuming gender will be stored as a string, adjust data type as needed

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
            "password": self.password,
            "gender": self.gender
        }