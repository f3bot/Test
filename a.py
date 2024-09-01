from twilio import Client
from flask import Flask,request

account_sid = 'AC6d3bb8b7eb6529856daac7ec0dacd9ba'
account_auth = '3f72cd2d8db892116c5060b630e8ec05'

client = Client(account_sid, account_auth)

app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])
def whatsapp_bot():
    incoming_msg = request.values.get('Body', '').lower()
    sender = request.values.get('From', '')
    response = ""

    if 'hello' in incoming_msg:
        response = "Hello! How can I assist you today?"

    elif 'bye' in incoming_msg:
        response = "Goodbye! Have a great day."

    else:
        response = "Sorry, I didn't understand that."

    # Send response
    client.messages.create(
        body=response,
        from_='whatsapp:+12404340307',
        to=sender
    )
    return "Message sent!"

if __name__ == '__main__':
    app.run(debug=True)