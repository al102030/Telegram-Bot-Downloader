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
        txt = msg['message']['text']
        if txt == "Hi":
            bot_methods.send_message("Aleyk Hi", chat_id)
        else:
            bot_methods.send_message("What???", chat_id)
        return Response('ok', status=200)
    else:
        return '<h1>Not OK</h1>'


if __name__ == "__main__":
    app.run(debug=True)
