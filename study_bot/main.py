from flask import Flask
from . import views, model
from .lib import config


def register_api():
    for cur_blueprint, prefix in views.blueprints:
        APP.register_blueprint(cur_blueprint, url_prefix=prefix)


APP = Flask(__name__)
APP.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
register_api()
config.setup()
model.setup(config.CONF["DB"])

if __name__ == "__main__":
    APP.run(debug=True)
