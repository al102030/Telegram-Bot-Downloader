from flaskapp import bot_methods, app
from config.secret import lnk

if __name__ == "__main__":
    bot_methods.remove_webhook()
    bot_methods.set_webhook(lnk)
    app.run(debug=True)
