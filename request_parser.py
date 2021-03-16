from flask_restful import reqparse


parser = reqparse.RequestParser()
parser.add_argument("id", type=int, required=True)
parser.add_argument("surname", type=str, required=True)
parser.add_argument("name", type=str, required=True)
parser.add_argument("age", type=int, required=True)
parser.add_argument("position", type=str, required=True)
parser.add_argument("speciality", type=str, required=True)
parser.add_argument("address", type=str, required=True)
parser.add_argument("email", type=str, required=True)
parser.add_argument("password", type=str, required=True)
parser.add_argument("city_from", type=str, required=True)
