# Python API Deployment
This repo contains guided examples of deploying Python applications via multiple ways.

## 1. Flask
Flask is a micro-framework for deploying Python apps in a straight-forwarded manner.

You can install flask by pip:

```
pip install Flask
```

## Flask Examples
Under [1_Flask](1_Flask), 2 simple flask apps are provided.

After cloning the files or copying the codes by youself, use command line (bash) to navigate to the directories containing the files.

Take a look at the code of [app.py](1_Flask/app.py)
1. On bash:
    1. export FLASK_APP=app.py 
    2. flask run
2. Go to your browser: http://localhost:5000/
    1. You should see ```{"dateOfBirth": null, "numbers": null, "occupation": null}```
3. Change the url to: http://localhost:5000/?dateOfBirth=2000-01-01&numbers=1234567&occupation=datacleaning
    1. You should see ```{"dateOfBirth": "2000-01-01", "numbers": "1234567", "occupation": "datacleaning"}```

**set* instead of *export* on windows

Check out the [flask documentation](http://flask.pocoo.org/).
