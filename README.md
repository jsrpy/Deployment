# Python API Deployment
This repo contains guided examples of deploying Python applications via multiple ways.

## 1. Flask
Flask is a micro-framework for deploying Python apps in a straight-forward manner.

You can install flask by pip:

```
pip install Flask
```

### Flask Examples
Under [1_Flask](1_Flask), 2 simple flask apps are provided.

After cloning the files or copying the codes by youself, use command line (bash) to navigate to the directories containing the files.

### Example 1 - GET method
Take a look at the code of [app.py](1_Flask/app.py)
1. On bash:
    1. export FLASK_APP=app.py 
    2. flask run
2. Go to your browser: http://localhost:5000/
    1. You should see ```{"dateOfBirth": null, "numbers": null, "occupation": null}```
3. Change the url to: http://localhost:5000/?dateOfBirth=2000-01-01&numbers=1234567&occupation=datacleaning
    1. You should see ```{"dateOfBirth": "2000-01-01", "numbers": "1234567", "occupation": "datacleaning"}```

**set* instead of *export* on windows

#### Request & Response
All interactions between and client (browser) the server (flask app) are request & response.
When you make a query (the keys & values in url) and send the request to your server, you flask app processes the query and return the response. 

In the example, we make a query from the address bar, which is a GET request.

You can get the user input by ```request.args.get('key')```.

### Example 2 - POST method
[app2.py](1_Flask/app2.py) differs from app.py

* It gives the route name as `"/predict"`
* It is a POST method.

You cannot make a post call in a url from browser address bar. 

We use a third-party tool called [postman](https://www.getpostman.com/). It is the easiest way to make requests to a server.
It supports all request methods and authorisation headers.

Download and install the postman tool:
1. On bash:
    1. export FLASK_RUN_PORT=5001
    2. export FLASK_APP=app2.py 
    3. flask run
2. Browser: http://localhost:5001/predict 
    1. You should see a *Method Not Allowed* error.
3. Postman: http://localhost:5001/predict -> click SEND button
    1. You should see a *Method Not Allowed* error. The same as your browser.
    2. Choose from the scroll down button and change GET -> POST. 
    3. In *Body*, type in the keys ('name','age') and any values you want. Hit SEND.
    4. You should see your input at bash.

### Example 3 - Textbox

[app3.py](1_Flask/app3.py) is an example with textbox input.

You can see the [demo hosted on real](https://uselessflaskapp--jsnc.repl.co/).

The app3.py looks for the designated html file under /templates directory, renders that html, accepts user input in textbox and return the results after processing calculation. 


## Flask Documentation
Check out the [flask documentation](http://flask.pocoo.org/).
