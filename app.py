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
    response = request.get_json(silent=True, force=True)
    processRequest(response)
    return "Hello, 2"

# queryResult -> intent -> endInteraction

def processRequest(response):

    query_response = response["queryResult"]
    text = query_response.get("fulfillmentText", None)
    print(text)

app.run(port=5000)