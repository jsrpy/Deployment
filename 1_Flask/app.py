from flask import Flask
from flask import request
from flask import json

application = Flask(__name__) # set app name = filename

@application.route("/",methods=["GET"]) #GET request
def hello_get():
	# Getting input from users.
	print(request.args.get('dateOfBirth'))
	print(request.args.get('occupation'))
	print(request.args.get('numbers'))
	# Run your model to predict a certain things
	 
	# Returning the result
	#return json.dumps({'123':567})
	return json.dumps({ #return dict in json format
			"dateOfBirth":request.args.get('dateOfBirth'),
			"occupation" :request.args.get('occupation'),
			"numbers": request.args.get('numbers')})