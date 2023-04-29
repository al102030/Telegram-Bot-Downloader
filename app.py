# from models import User, Download
from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy
from TLMethods.Telegram import Telegram
from config.secret import token, url

app = Flask(__name__)
app.config['SECRET_KEY'] = '4edc0281f3899c05d40adf12a1102fef'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


bot_methods = Telegram(token)


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
    bot_methods.remove_webhook()
    bot_methods.set_webhook(url)
    app.run(debug=True)
