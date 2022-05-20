import re
from flask import Flask, jsonify, request
from util import verify_signature

app = Flask(__name__)

@app.route("/healthcheck", methods=['GET'])
def hello_world():
    return jsonify({"status": "up"})

@app.route("/event", methods=['POST'])
def consume_event():

    verify = verify_signature(request)

    print(f'verify: {verify}')

    print(request.get_json())
    return jsonify({}), 200
