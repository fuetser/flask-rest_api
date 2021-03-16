from flask import jsonify
from flask_restful import Resource, abort
from werkzeug.security import generate_password_hash
from __all_models import *
from db_session import *
from request_parser import parser


global_init("db.db")
session = create_session()


def get_user_or_404(user_id):
    user = session.query(User).get(user_id)
    if not user:
        abort(404, error=f"User {user_id} not found")
    else:
        return user


class UsersResource(Resource):
    def get(self, user_id):
        user = get_user_or_404(user_id)
        return jsonify({
            "users": [user.to_dict()]
        })

    def put(self, user_id):
        args = parser.parser_args(strict=True)
        if not args:
            return jsonify({'error': 'Empty request'})
        user = get_user_or_404(user_id)
        for key, value in args.iteritems():
            setattr(user, key, value)
        session.commit()
        return jsonify({'success': 'OK'})

    def delete(self, user_id):
        args = parser.parse_args(strict=True)
        if not args:
            return jsonify({'error': 'Empty request'})
        user = get_user_or_404(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        users = session.query(User).all()
        return jsonify({
            "users": [user.to_dict() for user in users]
        })

    def post(self):
        args = parser.parse_args(strict=True)
        if not args:
            return jsonify({'error': 'Empty request'})
        args = parser.parse_args()
        args["hashed_password"] = generate_password_hash(args.pop("password"))
        user = User(**args)
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})
