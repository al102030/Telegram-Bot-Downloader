# from flaskapp import bot_methods, app
# from config.secret import lnk
from flaskapp import routes


if __name__ == "__main__":
    # bot_methods.remove_webhook()
    # bot_methods.set_webhook(lnk)
    # app.run(debug=True)
    link = "https://www.youtube.com/watch?v=bVNPRCv431M"
    routes.youtube_download(link)
