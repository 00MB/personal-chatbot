from flask import Flask, request, make_response
import json
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, world"

@app.route("/webhook", methods=['POST'])
def webhook():
    print("recieved")
    json.dump(request.json, open("input.json", "w"), indent=4, sort_keys=True)
    return "Hello, 2"

app.run(port=5000)