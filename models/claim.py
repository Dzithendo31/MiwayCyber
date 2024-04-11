import uuid
from extensions import db


class claim(db.Model):
    __tablename__ = "claims"
    claim_ID = db.Column(db.String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    userPolicy_ID = db.Column(db.String(50))
    userID = db.Column(db.String(50))
    claimDate = db.Column(db.String(50))
    claimAmount = db.Column(db.String(50))
    claimDescription = db.Column(db.String(555))
    claimStatus = db.Column(db.String(50))

    def to_dict(self):
        return {
            "claim_ID": self.claim_ID,
            "userPolicy_ID": self.userPolicy_ID,
            "userID": self.userID,
            "claimDate": self.claimDate,
            "claimAmount": self.claimAmount,
            "claimDescription": self.claimDescription,
            "claimStatus": self.claimStatus
        }