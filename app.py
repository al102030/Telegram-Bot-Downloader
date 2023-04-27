from flask import Flask, request, Response
from config.secret import token, url
from TLMethods.Telegram import Telegram

app = Flask(__name__)

bot_methods = Telegram(token)
bot_methods.remove_webhook()
bot_methods.set_webhook(url)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        chat_id = msg['message']['chat']['id']
        # txt = msg['message']['text']
        from_chat_id = msg['message']['from']['id']
        message_id = msg['message']['message_id']
        bot_methods.forward_message(message_id, chat_id, from_chat_id)
        return Response('ok', status=200)
    else:
        return '<h1>Not OK</h1>'
