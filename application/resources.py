from flask_restful import Resource, Api, reqparse, fields, marshal
from flask_security import auth_required, roles_required, current_user
from flask import jsonify
from sqlalchemy import or_
from .models import StudyResource, db
from .instances import cache


api = Api(prefix='/api')

parser = reqparse.RequestParser()
parser.add_argument('topic', type=str,
                    help='Topic is required should be a string', required=True)
parser.add_argument('description', type=str,
                    help='Description is required and should be a string', required=True)
parser.add_argument('resource_link', type=str,
                    help='Resource Link is required and should be a string', required=True)


class Creator(fields.Raw):
    def format(self, user):
        return user.email


study_material_fields = {
    'id': fields.Integer,
    'topic':   fields.String,
    'description':  fields.String,
    'resource_link': fields.String,
    'is_approved': fields.Boolean,
    'creator': Creator
}


class StudyMaterial(Resource):
    @auth_required("token")
    @cache.cached(timeout=50)
    def get(self):
        if "inst" in current_user.roles:
            study_resources = StudyResource.query.all()
        else:
            study_resources = StudyResource.query.filter(
                or_(StudyResource.is_approved == True, StudyResource.creator == current_user)).all()
        if len(study_resources) > 0:
            return marshal(study_resources, study_material_fields)
        else:
            return {"message": "No Resourse Found"}, 404

    @auth_required("token")
    @roles_required("stud")
    def post(self):
        args = parser.parse_args()
        study_resource = StudyResource(topic=args.get("topic"), description=args.get(
            "description"), resource_link=args.get("resource_link"), creator_id=current_user.id)
        db.session.add(study_resource)
        db.session.commit()
        return {"message": "Study Resource Created"}


api.add_resource(StudyMaterial, '/study_material')
