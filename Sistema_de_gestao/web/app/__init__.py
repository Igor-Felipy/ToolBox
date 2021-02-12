from flask import Flask

app = Flask(__name__)

from app.controllers import controller
app.register_blueprint(controller)