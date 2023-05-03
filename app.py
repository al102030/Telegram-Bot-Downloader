from flaskapp import bot_methods, app
from config.secret import lnk


if __name__ == "__main__":
    bot_methods.remove_webhook()
    bot_methods.set_webhook(lnk)
    app.run(debug=True)
    # url = "https://www.youtube.com/shorts/iKXIZd8uUY8"
    # routes.youtube_download(url)
