# Some set up for the application 

from flask import Flask
from flaskext.mysql import MySQL

# create a MySQL object that we will use in other parts of the API
db = MySQL()

def create_app():
    app = Flask(__name__)
    
    # secret key that will be used for securely signing the session 
    # cookie and can be used for any other security related needs by 
    # extensions or your application
    app.config['SECRET_KEY'] = 'someCrazyS3cR3T!Key.!'

    # these are for the DB object to be able to connect to MySQL. 
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = open('/secrets/db_root_password.txt').readline().strip()
    app.config['MYSQL_DATABASE_HOST'] = 'db2'
    app.config['MYSQL_DATABASE_PORT'] = 3306
    app.config['MYSQL_DATABASE_DB'] = 'coop_connect'  # Change this to your DB name

    # Initialize the database object with the settings above. 
    db.init_app(app)
    
    # Add the default route
    # Can be accessed from a web browser
    # http://ip_address:port/
    # Example: localhost:8001
    @app.route("/")
    def welcome():
        return "<h1>Welcome to the 3200 boilerplate app</h1>"

    # Import the various Beluprint Objects
    from src.User import User
    from src.CompensationPackage import CompensationPackage
    from src.Question import Question
    from src.Review import Review
    from src.Answer import Answer
    from src.CoopCycle import CoopCycle



    # Register the routes from each Blueprint with the app object
    # and give a url prefix to each
    app.register_blueprint(CompensationPackage,   url_prefix='/cp')
    app.register_blueprint(Question,   url_prefix='/q')
    app.register_blueprint(User,   url_prefix='/u')
    app.register_blueprint(Review,   url_prefix='/r')
    app.register_blueprint(Answer,   url_prefix='/a')
    app.register_blueprint(CoopCycle,   url_prefix='/cc')



    # Don't forget to return the app object
    return app