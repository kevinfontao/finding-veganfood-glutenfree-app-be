from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    phone_number = db.Column(db.String(120), unique=False, nullable=False)
    rewards = db.Column(db.String(120), unique=False, nullable=True)
    diet = db.Column(db.String(120),  nullable=False)
    user_avatar = db.Column(db.String(120),  nullable=True)

    def __repr__(self):
        return '<Profile %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "phone_number": self.phone_number,
            "diet": self.diet,
            
            # do not serialize the password, its a security breach
        }

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    diet = db.Column(db.String(120), unique=False, nullable=False)
    address = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=True)
    phone_number = db.Column(db.String(120),  nullable=False)
    operational_hours = db.Column(db.String(120),  nullable=True)
    pricing = db.Column(db.String(120),  nullable=True)

    def __repr__(self):
        return '<Profile %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "phone_number": self.phone_number,
            "diet": self.diet,
            
            # do not serialize the password, its a security breach
        }

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    diet = db.Column(db.String(120), unique=False, nullable=False)
    address = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=True)
    phone_number = db.Column(db.String(120),  nullable=False)
    operational_hours = db.Column(db.String(120),  nullable=True)
    pricing = db.Column(db.String(120),  nullable=True)

    def __repr__(self):
        return '<Profile %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "phone_number": self.phone_number,
            "diet": self.diet,
            
            # do not serialize the password, its a security breach
        }

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    diet = db.Column(db.String(120), unique=False, nullable=False)
    address = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=True)
    phone_number = db.Column(db.String(120),  nullable=False)
    operational_hours = db.Column(db.String(120),  nullable=True)
    pricing = db.Column(db.String(120),  nullable=True)

    def __repr__(self):
        return '<Profile %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "phone_number": self.phone_number,
            "diet": self.diet,
            
            # do not serialize the password, its a security breach
        }

class Review_picture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(120), unique=True, nullable=False)
    review_id = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<Profile %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.image_url,
            "name": self.review_id,
            "phone_number": self.phone_number,
            "diet": self.diet,
            
            # do not serialize the password, its a security breach
        }