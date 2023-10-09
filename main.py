from flask import Flask
from application.models import db
from config import DevelopmentConfig
from application.resources import api


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    api.init_app(app)
    with app.app_context():
        import application.views

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)