import pyautogui as pt
from time import sleep
import dialogflow_bot
import pyperclip

# WARNING - Pixel specifications different depending on screen size

position1 = pt.locateOnScreen("images/whatsapp_reference.png", confidence=0.6)
x = position1[0]
y = position1[1]

def get_message():
    global x, y

    position = pt.locateOnScreen("images/whatsapp_reference.png", confidence=0.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x,y, duration=0.05)
    pt.moveTo(x + 100, y - 50, duration=0.05)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(10,-140)
    pt.click()
    return pyperclip.paste()

def post_response(message):
    global x, y

    position = pt.locateOnScreen("images/whatsapp_reference.png", confidence=0.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 200, y + 20, duration=0.05)
    pt.click()
    pt.typewrite(message, interval=0.01)
    pt.typewrite("\n", interval=0.01)

pt.moveTo(x + 100, y - 35, duration=0.05)

while True:
    try:
        position = pt.locateOnScreen("images/whatsapp_notification.png", confidence=0.7)
        if position is not None:
            pt.moveTo(position)
            pt.moveRel(-100,0)
            pt.click()
            sleep(1)

    except(Exception):
        print("no new notifications")

    if pt.pixelMatchesColor(int(x+100), int(y-35), (255,255,255), tolerance=10):
        print("is white")
        message = get_message()
        print(message)
        response = dialogflow_bot.send_message(message)
        print(response)
        post_response(response)