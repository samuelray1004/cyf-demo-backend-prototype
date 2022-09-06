from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Property(db.Model):
    __tablename__ = "property"
    id = db.Column(db.Integer, primary_key=True)
    street1 = db.Column(db.String, nullable=False)
    street2 = db.Column(db.String, nullable=False)
    street_number = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    zip_code = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    def __init__(self, **kwargs):
        self.street1 = kwargs.get("stree1", "EMPTY")
        self.street2 = kwargs.get("street2", "EMPTY")
        self.street_number = kwargs.get("street_number", "EMPTY")
        self.city = kwargs.get("city", "EMPTY")
        self.state = kwargs.get("state", "EMPTY")
        self.zip_code = kwargs.get("zip_code", "EMPTY")
        self.description = kwargs.get("description", "EMPTY")

    def serialize(self):
        return {
            "id": self.id,
            "street1": self.street1,
            "street2": self.street2,
            "streetNumber": self.street_number,
            "city": self.city,
            "state": self.state,
            "zipCode": self.zip_code,
            "description": self.description
        }
