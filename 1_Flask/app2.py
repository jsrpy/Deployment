from flask import Flask, jsonify, request

app = Flask(__name__)
app.run(port=5001)

@app.route("/predict",methods=["POST"]) # url=/predict # POST request
def predict():
    print(request.form.get('name'))
    print(request.form.get('age'))
    return jsonify({"abc":1234}) #jsonify = json.dump