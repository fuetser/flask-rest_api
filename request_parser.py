from flask_restful import reqparse


users_parser = reqparse.RequestParser()
users_parser.add_argument("id", type=int, required=True)
users_parser.add_argument("surname", type=str, required=True)
users_parser.add_argument("name", type=str, required=True)
users_parser.add_argument("age", type=int, required=True)
users_parser.add_argument("position", type=str, required=True)
users_parser.add_argument("speciality", type=str, required=True)
users_parser.add_argument("address", type=str, required=True)
users_parser.add_argument("email", type=str, required=True)
users_parser.add_argument("password", type=str, required=True)
users_parser.add_argument("city_from", type=str, required=True)

jobs_parser = reqparse.RequestParser()
jobs_parser.add_argument("id", type=int, required=True)
jobs_parser.add_argument("team_leader", type=int, required=True)
jobs_parser.add_argument("job", type=str, required=True)
jobs_parser.add_argument("work_size", type=int, required=True)
jobs_parser.add_argument("collaborators", type=str, required=True)
jobs_parser.add_argument("is_finished", type=int, required=True)
