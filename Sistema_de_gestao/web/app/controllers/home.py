from . import controller

@controller.route("/")
def home():
    return "home blueprint"