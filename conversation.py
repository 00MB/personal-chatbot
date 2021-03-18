import dialogflow_bot

while True:
    message = input("Enter message: ")
    response = dialogflow_bot.send_message(message)
    print(response)
