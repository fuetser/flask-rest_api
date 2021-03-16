from flask import Flask
from flask_restful import Api
from users_resource import *


app = Flask(__name__)
api = Api(app)
api.add_resource(UsersListResource, "/api/v2/users")
api.add_resource(UsersResource, "/api/v2/users/<int:user_id>")


if __name__ == '__main__':
    app.run(debug=True)
