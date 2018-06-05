from flask import Flask
from flask import request
from flask import json

application = Flask(__name__)

@application.route("/",methods=["GET"])
def hello_get():
	# Getting input from users.
	print(request.args.get('dateOfBirth'))
	print(request.args.get('occupation'))
	print(request.args.get('numbers'))
	# Run your model to predict a certain things
	 
	# Returning the result
	#return json.dumps({'123':567})
	return json.dumps({
			"dateOfBirth":request.args.get('dateOfBirth'),
			"occupation" :request.args.get('occupation'),
			"numbers": request.args.get('numbers')})

@application.route("/",methods=["POST"])
def hello_post():
	print(request.form.get('test'))
	return json.dumps({"abc":1234})