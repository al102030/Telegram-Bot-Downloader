from flaskapp import app, bot_methods
from config.secret import url


if __name__ == "__main__":
    bot_methods.remove_webhook()
    bot_methods.set_webhook(url)
    app.run(debug=True)
