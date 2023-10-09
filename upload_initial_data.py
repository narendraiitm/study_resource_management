from main import app
from application.models import db, Role

with app.app_context():
    db.create_all()
    admin = Role(id='admin', name='Admin', description='Admin description')
    db.session.add(admin)
    stud = Role(id='stud', name='Student', description='Student description')
    db.session.add(stud)
    inst = Role(id='inst', name='Instructor', description='Instructor description')
    db.session.add(inst)
    try:
       db.session.commit()
    except:
       pass
    

