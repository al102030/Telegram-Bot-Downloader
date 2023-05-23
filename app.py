# from flaskapp import bot_methods, app
# from config.secret import lnk
import pytube
import requests


def login_to_youtube(username, password):

    payload = {
        "username": username,
        "password": password
    }

    session = requests.session()
    response = session.post("https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&hl=en&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26feature%3Dsign_in_button%26hl%3Den%26next%3D%252F&flowName=GlifWebSignIn&flowEntry=ServiceLogin", data=payload)

    if response.status_code == 200:
        print("Logged in to YouTube successfully.")
    else:
        raise Exception("Failed to log in to YouTube.")


if __name__ == "__main__":
    yt = pytube.YouTube('https://www.youtube.com/shorts/9t0LEg12qFY')
    username = 'alitestyou14@gmail.com'
    password = 'Mammad123456@'
    yt.register_on_complete_callback(login_to_youtube(username, password))
    try:
        stream = yt.streams.filter(progressive=True).first()
        stream.download(output_path='static/DL',
                        filename=yt.title+'-youtube.mp4')
    except pytube.exceptions.AgeRestrictedError as e:
        print("Age-restricted video detected, attempting to bypass.")
        yt.register_on_complete_callback(login_to_youtube(username, password))
        stream = yt.streams.filter(progressive=True).first()
        stream.download(output_path='static/DL',
                        filename=yt.title+'-youtube.mp4')
    # bot_methods.remove_webhook()
    # bot_methods.set_webhook(lnk)
    # app.run(debug=True)
