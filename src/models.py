from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __inint__(self, email, password):
        self.email = email
        self.password = password
        self.is_active = True

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active
            # do not serialize the password, its a security breach
        }
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    phone_number = db.Column(db.String(120), unique=False, nullable=False)
    rewards = db.Column(db.String(120), unique=False, nullable=True)
    diet = db.Column(db.String(120),  nullable=False)
    password = db.Column(db.String(120),  nullable=False)
    user_avatar = db.Column(db.String(120),  nullable=True)
    reviews = db.relationship('Review', backref='profile', lazy=True)

    def __repr__(self):
        return '<Profile %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "phone_number": self.phone_number,
            "diet": self.diet,
            "password": self.password,
            "rewards": self.rewards,
            "user_avatar": self.user_avatar,
            "reviews": list(map(lambda x: x.serialize(), self.reviews))
            
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
    reviews = db.relationship('Review', backref='restaurant', lazy=True)

    def __repr__(self):
        return '<Restaurant %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "phone_number": self.phone_number,
            "diet": self.diet,
            "address": self.address,
            "operational_hours": self.operational_hours,
            "pricing": self.pricing,
            "reviews": list(map(lambda x: x.serialize(), self.reviews))
            
            # do not serialize the password, its a security breach
        }

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.String(120), unique=True, nullable=False)
    diet = db.Column(db.String(120), unique=False, nullable=False)
    recipe_ingredients = db.Column(db.String(120), unique=False, nullable=False)
    images = db.Column(db.String(120),  nullable=False)
    video_recipe_link = db.Column(db.String(120),  nullable=True)
    recipe_description = db.Column(db.String(120),  nullable=True)

    def __repr__(self):
        return '<Recipe %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "profile_id": self.profile_id,
            "diet": self.diet,
            "recipe_ingredients": self.recipe_ingredients,
            "images": self.images,
            "video_recipe_link": self.video_recipe_link,
            "recipe_description": self.recipe_description
            
            # do not serialize the password, its a security breach
        }

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120), unique=False, nullable=False)
    rating = db.Column(db.String(120), unique=False, nullable=True)
    pictures = db.Column(db.String(120),  nullable=False)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'),
        nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'),
        nullable=False)

    def __repr__(self):
        return '<Review %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "description": self.description,
            "rating": self.rating,
            "pictures": self.pictures,
            
            # do not serialize the password, its a security breach
        }

class Review_picture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(120), unique=True, nullable=False)
    review_id = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<Review_picture %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "image_url": self.image_url,
            "review_id": self.review_id,
            
            # do not serialize the password, its a security breach
        }