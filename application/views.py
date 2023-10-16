from flask import current_app as app, jsonify
from flask_security import auth_required, roles_required
from .models import User, db

@app.get('/')
def home():
    return "hello world"


@app.get('/admin')
@auth_required("token")
@roles_required("admin")
def admin():
    return "Hello Admin"

@app.get('/activate/inst/<int:inst_id>')
@auth_required("token")
@roles_required("admin")
def activate_instructor(inst_id):
    instructor = User.query.get(inst_id)
    if not instructor or "inst" not in instructor.roles:
        return jsonify({"message":"Instructor not found"}), 404
    
    instructor.active=True
    db.session.commit()
    return jsonify({"message":"User Activated"})