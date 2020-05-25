import requests
import os
import re
import json
from grammar import numbers, simple_math
from flask import Flask, render_template, request, jsonify, json, redirect, url_for, session, abort, g, flash
from flask.ext import restful
from flask.ext.restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)
app.config.from_object('config')  # config.py is loaded into app.config

number_service = numbers.NumberService()
simple_math_service = simple_math.SimpleMathService()


def make_error(status_code, sub_code, message, action):
    response = jsonify({
        'status': status_code,
        'sub_code': sub_code,
        'message': message,
        'action': action
        })
    response.status_code = status_code
    return response


class NumberResource(Resource):
    """Resource to run a numbers.py parse on a single number"""

    def get(self, number_expression):
        print "GET received"
        try:
            value = number_service.parse_english(number_expression)
            d = {'value': value}
            return jsonify(d)
        except Exception:
            return make_error(404, None, ("Ya dun goofed on your English "
                                          "number expression"), None)


class NumbersResource(Resource):
    """Resource to run a numbers.py parse on at least one number"""

    def __init__(self):
        self.parser = reqparse.RequestParser()
        # we will now accept a list of body data via 'append' action
        self.parser.add_argument('number_expression', type=str, required=True,
                                 help='Expression cannot be converted',
                                 action='append')

    def get(self):
        print "GET received"
        return make_error(404, None, "You sent a GET to a POST-based endpoint",
                          None)

    def post(self):
        print "POST received"
        args = self.parser.parse_args()
        try:
            d = {}
            # key = "expression_"
            for i_e, expression in enumerate(args['number_expression']):
                print expression
                value = number_service.parse_english(expression)
                # d[key + str(i_e + 1)] = value
                d[expression] = value
            return jsonify(d)
        except Exception:
            abort(404)


class SimpleMathResource(Resource):
    """Resource to perform basic arithmetic on a single English expression"""

    def get(self, expression):
        print "GET received"
        # str(expression) to get rid of unicode string
        return simple_math_service.parse_basic_formula(str(expression))


class SimpleMathsResource(Resource):
    """Resource to perform basic arithmetic on at least one English
    expression"""

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('arithmetic_expression',
                                 type=str, required=True,
                                 help='Expression could not be evaluated',
                                 action='append')

    def get(self):
        print "GET received"
        return make_error(404, None, "You sent a GET to a POST-based endpoint",
                          None)

    def post(self):
        print "POST received"
        args = self.parser.parse_args()
        try:
            d = {}
            for expression in args['arithmetic_expression']:
                d[expression] = simple_math_service.parse_basic_formula(
                    str(expression))
            return jsonify(d)
        except Exception:
            abort(404)

# match parts of the path as variables to your resource methods
api.add_resource(NumberResource, '/english_to_number/<string:number_expression>')
api.add_resource(NumbersResource, '/english_to_number')
api.add_resource(SimpleMathResource, '/solve/<string:expression>')
api.add_resource(SimpleMathsResource, '/solve')


@app.route('/index')
def index():
    return "You've reached Numberz"

# start up development web server with our app
if __name__ == '__main__':
    app.run(debug=True)
