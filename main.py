from flask import Flask
from flask_security import SQLAlchemyUserDatastore, Security
from application.models import db, User, Role
from config import DevelopmentConfig
from application.resources import api


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    api.init_app(app)
    datastore = SQLAlchemyUserDatastore(db,User, Role)
    app.security = Security(app, datastore)
    with app.app_context():
        import application.views

    return app, datastore

app, datastore = create_app()

if __name__ == '__main__':
    app.run(debug=True)