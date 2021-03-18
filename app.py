# from flask import Flask, request, make_response, jsonify
# import json

# app = Flask(__name__)

# #OPTIONAL - FOR WEBHOOKS

# Required:
#   Ngrok

# # @app.route("/webhook", methods=['POST'])
# # def webhook():
# #     print("recieved")
# #     response = request.get_json(silent=True, force=True)
# #     return

# # def processRequest(response):
# #     query_response = response["queryResult"]
# #     text = query_response.get("fulfillmentText", None)
# #     print(text)