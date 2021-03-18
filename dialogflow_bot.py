import os
import dialogflow

import send_email

from dotenv import load_dotenv
load_dotenv()

def send_message():
    message = input("Enter message: ")
    project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
    response = detect_intent_texts(project_id, "unique", message, 'en')
    print(response)
    if response == "Brb":
        EMAIL_ADDRESS = os.getenv('SENDER_EMAIL')
        EMAIL_PASSWORD = os.getenv('SENDER_PASSWORD')
        EMAIL_RECIEVER = os.getenv('RECIEVER_EMAIL')
        send_email.send_email(EMAIL_ADDRESS, EMAIL_PASSWORD, EMAIL_RECIEVER)

def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    if text:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(
            session=session, query_input=query_input)
        return response.query_result.fulfillment_text

while True:
    send_message()