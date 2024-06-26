import uuid
from extensions import db

class UserPolicy(db.Model):
    __tablename__ = "userPolicy"
    userPolicy_ID = db.Column(db.String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    userID = db.Column(db.String(50))
    policyID = db.Column(db.String(50))
    coverage = db.Column(db.Float)
    status = db.Column(db.String(50))
    startDate = db.Column(db.String(50))
    endDate = db.Column(db.String(50))
    assetValue = db.Column(db.Float)
    assetDecription = db.Column(db.String(1000))
    assetSecurity = db.Column(db.String(1000))
    clientDeclaration = db.Column(db.String(255))
    premium = db.Column(db.Float)

    def to_dict(self):
        return {
            "userPolicy_ID": self.userPolicy_ID,
            "userID": self.userID,
            "policyID": self.policyID,
            "coverage": self.coverage,
            "status": self.status,
            "startDate": self.startDate,
            "endDate": self.endDate,
            "AssetValue": self.assetValue,
            "assetDescription": self.assetDecription,
            "assetSecurity": self.assetSecurity,
            "clientDeclaration": self.clientDeclaration,
            "premium": self.premium
        }
    
