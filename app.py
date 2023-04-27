from flask import Flask
from config.secret import token, url
from TLMethods.Telegram import Telegram

app = Flask(__name__)

bot_methods = Telegram(token)
bot_methods.remove_webhook()
bot_methods.set_webhook(url)


@app.route("/", methods=["GET", "POST"])
def index():
    return "<p><h1>Hello, World!</h1></p>"


if __name__ == "__main__":
    app.run(debug=True)
