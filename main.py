from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify({"hello": "world"})

@app.route("/event", methods=['POST'])
def consume_event():
    print(request.get_json())
    return jsonify({}), 200
