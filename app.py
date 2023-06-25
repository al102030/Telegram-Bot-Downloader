from flaskapp import bot_methods, app
from config.secret import LINK
# from pytube import YouTube, exceptions


if __name__ == "__main__":
    # yt = YouTube("https://www.youtube.com/watch?v=ftnpGWFaEsQ")
    # file_id = yt.video_id
    # file_name = yt.title
    # print(file_id)
    # print(file_name)
    # print(yt.streams.first())

    bot_methods.remove_webhook()
    bot_methods.set_webhook(LINK)
    app.run(debug=True)
