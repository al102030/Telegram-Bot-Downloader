from flaskapp import bot_methods, app
from config.secret import LINK


if __name__ == "__main__":
    bot_methods.remove_webhook()
    bot_methods.set_webhook(LINK)
    app.run(debug=True)
