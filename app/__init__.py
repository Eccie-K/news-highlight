from flask import flask
from flask_bootsrap import flask_bootsrap
from config import config_options

bootsrap = Bootsrap()

def create_app(config_name)

app = Flask(__name__)

#creating app configuarations
app.config.from_object(config_options[config_name])

#initializing flask extensions
bootstrap.init_app(app)

# Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

# Setting config
    from .requests import configure_request
    configure_request(app)

    
return app