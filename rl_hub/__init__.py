from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

    from rl_hub.main.routes import main
    app.register_blueprint(main)

    return app
