# from flaskapp import bot_methods, app
# from config.secret import lnk
import requests
import pickle
from pytube import YouTube, exceptions


def login_to_youtube(username, password):
    session = requests.Session()
    login_data = {
        'username': username,
        'password': password
    }
    response = session.post('https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&hl=en&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26feature%3Dsign_in_button%26hl%3Den%26next%3D%252F&flowName=GlifWebSignIn&flowEntry=ServiceLogin', data=login_data)

    if response.status_code == 200:
        print("Logged in to YouTube successfully.")
        with open('cookies.pkl', 'wb') as f:
            pickle.dump(session.cookies, f)
    else:
        raise exceptions.AgeRestrictedError(
            "Failed to log in to YouTube.")


if __name__ == "__main__":
    GOOGLE_USER = "alitestyou14@gmail.com"
    GOOGLE_PASSWORD = "Mammad123456@"
    login_to_youtube(GOOGLE_USER, GOOGLE_PASSWORD)

    with open('cookies.pkl', 'rb') as f:
        cookies = pickle.load(f)

    # Use the cookies to download a video
    yt = YouTube('https://www.youtube.com/shorts/TW1J-B2roMA')
    yt.cookies = cookies
    stream = yt.streams.first()
    stream.download(output_path='static/DL', filename=yt.title+'-youtube.mp4')


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
# bot_methods.remove_webhook()
# bot_methods.set_webhook(lnk)
# app.run(debug=True)
