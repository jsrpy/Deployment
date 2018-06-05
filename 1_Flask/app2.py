from flask import Flask, jsonify, request

app = Flask(__name__)
app.run(port=5001)

@app.route("/predict",methods=["POST"])
def predict():
    print(request.form.get('name'))
    print(request.form.get('age'))
    return jsonify({"abc":1234})