from . import db


class Property(db.Model):
    # change table name
    __tablename__ = 'properties'
    #columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    photo = db.Column(db.String(100), nullable=False)
    
    def __init__(self, title, bedrooms, bathrooms, location, price, type, description, photo):
        self.title = title
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.location = location
        self.price = price
        self.type = type
        self.description = description
        self.photo = photo
