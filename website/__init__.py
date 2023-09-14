from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Define a database variable for which to call to whenever changes are made to the database
db = SQLAlchemy()
DB_NAME = "database.db"

# Website is a python package, which means we can define this function here and use it elsewhere by calling the website package
def create_app():
    app = Flask(__name__)
    # Configure app to encrypt/secure cookies related to website
    # In production, this secret key would never be shared publicly
    app.config["SECRET_KEY"] = "secretkey2986" 
    # Set the "SQLALCHEMY_DATABASE_URI" configuration variable to a SQLite database URI(Uniform Resource Identifier)
    # The URI is constructed using an f string - embeds expressions inside string literals
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    # Show database which app will be used 
    db.init_app(app)

    # Tell Flask to look at blueprints for routes
    from .views import views
    from .auth import auth
    
    # Register these blueprints with Flask
    # The url_prefix dictates how to access all of the urls stored under blueprints file
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    
    # Import database models
    from .models import User, Note

    with app.app_context():
        db.create_all()
        print("Created Database!")

    # Tell Flask how we load a user
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app
