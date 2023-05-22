from flaskapp import bot_methods, app
from config.secret import lnk
from pytube import YouTube

if __name__ == "__main__":
    # yt = YouTube("https://www.youtube.com/watch?v=0Cph9FS9Nyw")
    # print(yt.title)
    # for s in yt.streams:
    #     print(s)
    bot_methods.remove_webhook()
    bot_methods.set_webhook(lnk)
    app.run(debug=True)
