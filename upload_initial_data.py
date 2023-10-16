from main import app, datastore
from application.models import db, Role
from flask_security import hash_password

with app.app_context():
    db.create_all()
    datastore.find_or_create_role(name="admin", description="User is an admin")
    datastore.find_or_create_role(name="inst", description="User is an Instructor")
    datastore.find_or_create_role(name="stud", description="User is a Student")
    db.session.commit()
    if not datastore.find_user(email="admin@email.com"):
        datastore.create_user(email="admin@email.com", password=hash_password("admin"), roles=["admin"])
    if not datastore.find_user(email="inst1@email.com"):
        datastore.create_user(email="inst1@email.com", password=hash_password("inst1"), roles=["inst"], active=False)   
    if not datastore.find_user(email="stud1@email.com"):
        datastore.create_user(email="stud1@email.com", password=hash_password("stud1"), roles=["stud"])
    db.session.commit()