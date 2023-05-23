# from flaskapp import bot_methods, app
# from config.secret import lnk
import requests
import pickle
import time
from pytube import YouTube


# def login_to_youtube(username, password):

#     payload = {
#         "username": username,
#         "password": password
#     }

#     session = requests.session()
#     response = session.post("https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&hl=en&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26feature%3Dsign_in_button%26hl%3Den%26next%3D%252F&flowName=GlifWebSignIn&flowEntry=ServiceLogin", data=payload)

#     if response.status_code == 200:
#         print("Logged in to YouTube successfully.")
#     else:
#         raise Exception("Failed to log in to YouTube.")


if __name__ == "__main__":
    session = requests.Session()
    login_data = {
        'username': 'alitestyou14@gmail.com',
        'password': 'Mammad123456@'
    }
    response = session.post(
        'https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&hl=en&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26feature%3Dsign_in_button%26hl%3Den%26next%3D%252F&flowName=GlifWebSignIn&flowEntry=ServiceLogin"', data=login_data)
    # Save the cookies to a file

    if response.status_code == 200:
        print("Logged in to YouTube successfully.")
        with open('cookies.pkl', 'wb') as f:
            pickle.dump(session.cookies, f)
        time.sleep(20)
    else:
        raise YouTube.exceptions.AgeRestrictedError(
            "Failed to log in to YouTube.")

    # Load the saved cookies from the file
    with open('cookies.pkl', 'rb') as f:
        cookies = pickle.load(f)

    # Use the cookies to download a video
    yt = YouTube('https://www.youtube.com/shorts/9t0LEg12qFY')
    yt.cookies = cookies
    print("OK and ...")
    stream = yt.streams.first()
    stream.download(output_path='static/DL', filename=yt.title+'-youtube.mp4')

# yt = pytube.YouTube('https://www.youtube.com/shorts/9t0LEg12qFY')
# username = 'alitestyou14@gmail.com'
# password = 'Mammad123456@'
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
