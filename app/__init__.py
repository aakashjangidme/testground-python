from flask import Flask, Blueprint


def create_app():
    try:
        app = Flask(__name__)

        if app.config["ENV"] == "production":
            app.config.from_object("config.ProdConfig")
        elif app.config["ENV"] == "testing":
            app.config.from_object("config.TestConfig")
        else:
            app.config.from_object("config.DevConfig")

        from .api import blog_route
        app.register_blueprint(blog_route.blog_route)


        return app
    except Exception as e:

        print(e)