"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Profile
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# THIS IS THE ENDPOINT FOR /profile
#  YOU CAN CREATE A NEW PROFILE ( POST )
#  OR YOU CAN GET ALLE THE PROFILES  ( GET )

@app.route('/profile', methods=['POST', 'GET'])
def handle_profile():
    """
    Create profile and retrieve all profiles
    """

    # POST request
    if request.method == 'POST':
        body = request.get_json()

        # if body is None:
        #     raise APIException("You need to specify the request body as a json object", status_code=400)
        
        # if 'email' not in body:
        #     raise APIException('You need to specify the email', status_code=400)
        # if 'password' not in body:
        #     raise APIException('You need to specify the password', status_code=400)    

        profile = Profile(
          email=body['email'], 
          name=body['name'], 
          phone_number=body['phone_number'], 
          rewards=body['rewards'], 
          diet=body['diet'], 
          user_avatar=body['user_avatar'], 
        )
        db.session.add(profile)
        db.session.commit()
        return "ok", 200

    # GET request
    if request.method == 'GET':
        all_profiles = Profile.query.all()
        all_profiles = list(map(lambda x: x.serialize(), all_profiles))
        return jsonify(all_profiles), 200

    return "Invalid Method", 404

@app.route('/restaurant', methods=['POST', 'GET'])
def handle_restaurant():
    """
    Create profile and retrieve all restaurants
    """

    # POST request
    if request.method == 'POST':
        body = request.get_json()

        restaurant = Restaurant(
          email=body['email'], 
          name=body['name'], 
          phone_number=body['phone_number'], 
          address=body['address'], 
          diet=body['diet'], 
          website=body['website'], 
          operational_hours=body['operation_hours'],
          pricing=body['pricing']
        )
        db.session.add(restaurant)
        db.session.commit()
        return "ok", 200

    # GET request
    if request.method == 'GET':
        all_restaurants = restaurant.query.all()
        all_restaurants = list(map(lambda x: x.serialize(), all_restaurants))
        return jsonify(all_restaurants), 200

    return "Invalid Method", 404

@app.route('/recipe', methods=['POST', 'GET'])
def handle_recipe():
    """
    Create profile and retrieve all recipes
    """

    # POST request
    if request.method == 'POST':
        body = request.get_json()

        recipe = Recipe(
          profile_id=body['profile_id'], 
          images=body['images'], 
          video_recipe_link=body['video_recipe_link'], 
          recipe_description=body['recipe_description'], 
          public_recipes=body['public_recipes'], 
        )
        db.session.add(recipe)
        db.session.commit()
        return "ok", 200

    # GET request
    if request.method == 'GET':
        all_recipes = Profile.query.all()
        all_recipes = list(map(lambda x: x.serialize(), all_recipes))
        return jsonify(all_recipes), 200

    return "Invalid Method", 404

@app.route('/review', methods=['POST', 'GET'])
def handle_review():
    """
    Create profile and retrieve all reviews
    """

    # POST request
    if request.method == 'POST':
        body = request.get_json()

        review = Review(
          restaurant_id=body['restaurant_id'], 
          profile_id=body['profile_id'], 
          description=body['description'], 
          rating=body['rating'], 
          images=body['images'], 
        )
        db.session.add(review)
        db.session.commit()
        return "ok", 200

    # GET request
    if request.method == 'GET':
        all_reviews = Review.query.all()
        all_reviews = list(map(lambda x: x.serialize(), all_reviews))
        return jsonify(all_recipes), 200

    return "Invalid Method", 404



@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
