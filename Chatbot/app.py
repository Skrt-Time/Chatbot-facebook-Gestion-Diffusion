from flask import Flask, request
import requests
import json
import config
from fbchat import Client
from fbchat.models import *
from datetime import datetime
# import the chatbot
from chatbot import Chatty,save_infos

app = Flask(__name__)
app.config['SECRET_KEY'] = '5Dmj76-UYh6-9D4Ay-3Mm8g'


# Function to access to the sender API
def callSendAPI(senderPsid, response):
    PAGE_ACCESS_TOKEN = config.PAGE_ACCESS_TOKEN

    payload = {
        'recipient': {'id': senderPsid},
        'message': response,
        'messaging_type': 'RESPONSE'
    }
    headers = {'content-type': 'application/json'}

    url = 'https://graph.facebook.com/v10.0/me/messages?access_token={}'.format(PAGE_ACCESS_TOKEN)
    r = requests.post(url, json=payload, headers=headers)
    print("Request:",r.text)


# Function for handling a message from messenger
def handleMessage(senderPsid, receivedMessage):
    # Check if received message is a text
    print('We entered the HANDLE MESSAGE FUNCTION')
    if 'text' in receivedMessage:
        print('TEXT does exist in the RECEIVER MESSAGE')

        toSend = receivedMessage['text']

        # The Chatbot function ------------------------
        chatbot = Chatty()

        chatbotResponse = chatbot.chatbot_response(toSend)
        print('The Chatbot Response is: {}'.format(chatbotResponse))
        response = {"text": chatbotResponse}
        callSendAPI(senderPsid, response)
    """"if 'text' in receivedMessage:
         response={"text": 'Le message que tu as envoye est: {}'.format(receivedMessage['text'])}
         callSendAPI(senderPsid, response)

    else:
        response = {"text": 'This chatbot only accepts text messages'}
        callSendAPI(senderPsid, response)"""





# GET pour verifier le token
# POST pour verfier le webhook et process messages
'''@app.route('/', methods=["GET", "POST"])
def home():
    return 'Hello World! By SKRT'''


@app.route('/', methods=["GET", "POST"])
def index():
    '''No need'''
    if request.method == 'GET':
        VERIFY_TOKEN = '128fea16-bef2-4f86-8402-2fbb9b9ed70e'
        # Access to the datas sent by facebook
        if 'hub.mode' in request.args:
            mode = request.args.get('hub.mode')
            print("Mode:",mode)
        if 'hub.verify_token' in request.args:
            token = request.args.get('hub.verify_token')
            print("Token: ",token)
        if 'hub.mode' in request.args and 'hub.verify_token' in request.args:
            mode = request.args.get('hub.mode')
            token = request.args.get('hub.verify_token')
            # VERIFICATIONS
            if mode == 'subscribe' and token == VERIFY_TOKEN:
                print('WEBHOOK VERIFIED')

                challenge = request.args.get('hub.challenge')
                return challenge, 200
            else:
                return 'ERROR', 403
        return 'SKRT ON THE BEAT', 200

    if request.method == 'POST':
        VERIFY_TOKEN = '128fea16-bef2-4f86-8402-2fbb9b9ed70e'
        # Access to the datas sent by facebook
        if 'hub.mode' in request.args:
            mode = request.args.get('hub.mode')
            print("Mode: ",mode)
        if 'hub.verify_token' in request.args:
            token = request.args.get('hub.verify_token')
            print("Token: ",token)
        if 'hub.mode' in request.args and 'hub.verify_token' in request.args:

            mode = request.args.get('hub.mode')
            token = request.args.get('hub.verify_token')
            # VERIFICATIONS
            if mode == 'subscribe' and token == VERIFY_TOKEN:
                print('WEBHOOK VERIFIED')

                challenge = request.args.get('hub.challenge')
                return challenge, 200
            else:
                return 'ERROR', 403

        # when somebody send a message without verification webhook
        data = request.data
        # To decode the data sent and it as json because it come as a byte string
        body = json.loads(data.decode('utf-8'))

        if 'object' in body and body['object'] == 'page':
            entries = body['entry']
            for entry in entries:
                webhookEvent = entry['messaging'][0]
                print("WebhookEvent:",webhookEvent)
                senderPsid = webhookEvent['sender']['id']
                print('Sender PSID {}'.format(senderPsid))
                if "message" in webhookEvent:
                    handleMessage(senderPsid, webhookEvent['message'])
                return 'EVENT_RECEIVED', 200
            else:
                return 'ERROR', 404



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
