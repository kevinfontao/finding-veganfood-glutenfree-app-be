import os
from flask_admin import Admin
from models import db, Profile, Recipe, Restaurant
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')


    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(Profile, db.session))
    admin.add_view(ModelView(Recipe, db.session))
<<<<<<< HEAD
    admin.add_view(ModelView(Restaurant, db.session))
=======
>>>>>>> 1d4c3393fb43c526ccad3c357373734979eb7980

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))