from flaskapp import bot_methods, app
from config.secret import LINK
# import pickle
# from pytube import YouTube


if __name__ == "__main__":

    # with open('cookies.pkl', 'rb') as f:
    #     cookies = pickle.load(f)

    # # Use the cookies to download a video
    # yt = YouTube('https://www.youtube.com/watch?v=aBqnyEblhDg')
    # yt.cookies = cookies
    # stream = yt.streams.first()
    # stream.download(output_path='static/DL', filename=yt.title+'-youtube.mp4')

    # try:
    #     yt.register_on_complete_callback(login_to_youtube(username, password))
    #     stream = yt.streams.filter(progressive=True).first()
    #     stream.download(output_path='static/DL',
    #                     filename=yt.title+'-youtube.mp4')
    # except pytube.exceptions.AgeRestrictedError as e:
    #     print("Age-restricted video detected, attempting to bypass.")
    #     yt.register_on_complete_callback(login_to_youtube(username, password))
    #     stream = yt.streams.filter(progressive=True).first()
    #     stream.download(output_path='static/DL',
    #                     filename=yt.title+'-youtube.mp4')
    bot_methods.remove_webhook()
    bot_methods.set_webhook(LINK)
    app.run(debug=True)
