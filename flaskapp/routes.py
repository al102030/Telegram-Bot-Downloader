import json
import requests
import pickle
import time
import secrets
from pytube import YouTube, exceptions
from flask import request, Response
from flaskapp import app, bot_methods, db
from config.secret import GOOGLE_USER, GOOGLE_PASSWORD
from flaskapp.models import User, Download
from view.Menus import joining_channel_keyboard, credit_charge_keyboard, simple_options, start_again


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        channel_id = "-1001904767094"
        msg = request.get_json()
        is_text = None
        is_video = None
        try:
            is_text = msg['message']['text']
        except KeyError as error:
            print("Text is not find", error)

        try:
            is_video = msg['message']['video']
        except KeyError as error:
            print("Video is not find", error)

        if "callback_query" in msg:
            callback_id = msg['callback_query']['id']
            callback_from_id = msg['callback_query']['from']['id']
            callback_data = msg['callback_query']['data']
            user, new_user = add_new_user(callback_from_id)
            ans = bot_methods.get_chat_member(channel_id, callback_from_id)
            json_data = json.loads(ans)
            stat = json_data['result']['status']
            if new_user:
                options = start_again
                bot_methods.send_message_with_menu(
                    "Please start again.", callback_from_id, options)
            if callback_data == "01d0cfb8b904ad49":
                if stat != "left":
                    bot_methods.send_message(
                        "🍀Thank you for joining us.🍀\nNow you can use our services.",
                        callback_from_id)
                else:
                    bot_methods.answer_callback_query(
                        "Sorry! You're still not in our channel list.\nPlease join us:\nChannel: https://t.me/al102030_D",
                        callback_id, True)
            elif callback_data == "e01fdd230aeaa411":
                bot_methods.send_message(
                    "5 Gigabyte add to your account.\ncongratulations!", callback_from_id)
            elif callback_data == "1a710b5dc955e113":
                bot_methods.send_message(
                    "10 Gigabyte add to your account.\ncongratulations!", callback_from_id)
            elif callback_data == "5e14766d46f51eb7":
                bot_methods.send_message(
                    "20 Gigabyte add to your account.\ncongratulations!", callback_from_id)
            elif callback_data == "ad0eec6b4cf3c8ef":
                bot_methods.send_message(
                    "30 Gigabyte add to your account.\ncongratulations!", callback_from_id)

        elif is_text:
            chat_id = msg['message']['chat']['id']
            txt = msg['message']['text']
            user, new_user = add_new_user(chat_id)
            # download = Download.query.filter_by(
            #     user_id=User.id, status=2).first()
            ans = bot_methods.get_chat_member(channel_id, chat_id)
            json_data = json.loads(ans)
            stat = json_data['result']['status']
            if txt == "/start":
                if not new_user:
                    bot_methods.send_message(
                        f"You already registered in my user's list, Welcome back! (Your Telegram ID: {chat_id})", chat_id)
                    if stat == 'left':
                        inline_keyboard = joining_channel_keyboard
                        bot_methods.send_message_with_keyboard(
                            "You're not joined in our channel!\nPlease join to access our service.", chat_id, inline_keyboard)
                else:
                    bot_methods.send_message(
                        f"You are not registered in my user's list,Welcome! (Your Telegram ID: {chat_id})", chat_id)
                    if stat == 'left':
                        inline_keyboard = joining_channel_keyboard
                        bot_methods.send_message_with_keyboard(
                            "You're not joined in our channel!\nPlease join to access our service.", chat_id, inline_keyboard)
            else:
                if txt == "/c1":
                    status(chat_id=chat_id)
                elif txt == "/c2":
                    bot_methods.send_message("""Hi there!
                                            I'm a smart Bot that can help you to download your file from a variety of Internet services like YouTube, Instagram, etc., faster and safer.

                                            Thank you for your trustiness.

                                            Let's go on...""", chat_id)
                elif txt == "/c3":
                    if stat == "left":
                        inline_keyboard = joining_channel_keyboard
                        bot_methods.send_message_with_keyboard(
                            "Please Join our channel to use our services.\nThank you.",
                            chat_id, inline_keyboard)
                    elif user.credit == 0:
                        inline_keyboard = credit_charge_keyboard
                        bot_methods.send_message_with_keyboard(
                            "You don't have enough account credit to begin the download.\nPlease select one of the options below to debit your account.\nThank you",
                            chat_id, inline_keyboard)
                    else:
                        bot_methods.send_message(
                            "Enter your YouTube Link to start your download: ", chat_id)
                elif txt == "/c4":
                    options = simple_options
                    bot_methods.send_message_with_menu(
                        "Are you Sure?", chat_id, options)
                elif "youtube.com/" in txt:
                    if stat != "left" and user.credit != 0:
                        # login_to_youtube(GOOGLE_USER, GOOGLE_PASSWORD)
                        with open('cookies.pkl', 'rb') as f:
                            cookies = pickle.load(f)
                        yt = YouTube(txt)
                        yt.cookies = cookies
                        resolution_select_keyboard = []
                        for stream in (yt.streams.order_by('resolution').desc().filter(adaptive=True, file_extension='mp4')):
                            lst = []
                            dictionary = {}
                            dictionary['text'] = stream.resolution
                            dictionary['callback_data'] = stream.resolution
                            lst.append(dictionary)
                            resolution_select_keyboard.append(lst)

                        bot_methods.send_message_with_menu("Please select the resolution that you want to download",
                                                           chat_id, resolution_select_keyboard)
                        # filter(file_extension='mp4').
                        # res = yt.streams.order_by('resolution').desc()
                        # bot_methods.send_message(res, chat_id)
                        # .order_by('resolution').desc().first()
                        # Only look for video streams to avoid None values
                        # for stream in yt.streams:
                        #     bot_methods.send_message(stream.resolution, chat_id)
                        # time.sleep(1)

                        # stream = yt.streams.first()
                        # stream.download(output_path='/var/www/html/download',
                        #                 filename=str(chat_id)+'.mp4')
                        # bot_methods.send_chat_action('upload_video', chat_id)
                        # time.sleep(5)
                        # bot_methods.send_message(
                        #     "https://telapi.digi-arya.ir/downloads/"+str(chat_id)+".mp4", chat_id)
                elif txt == '1080p' or txt == '720p' or txt == '480p' or txt == '360p' or txt == '240p' or txt == '144p':
                    bot_methods.send_message(txt, chat_id)
                else:
                    bot_methods.send_message(
                        "I don't know what you're expecting of me?", chat_id)
                    # create record in DB
                    # download
                    # decrease user credit
        elif is_video:
            file_name = secrets.token_hex(8)
            chat_id = msg['message']['chat']['id']
            file_id = msg['message']['video']['file_id']
            file_size = msg['message']['video']['file_size']
            size_mb = int(file_size)/1000000
            if size_mb < 0:
                size_mb = 1
            else:
                size_mb = round(size_mb)
            user, new_user = add_new_user(chat_id)
            ans = bot_methods.get_chat_member(channel_id, chat_id)
            json_data = json.loads(ans)
            stat = json_data['result']['status']
            if new_user:
                bot_methods.send_message(
                    f"You are not registered in my user's list,Welcome! (Your Telegram ID: {chat_id})", chat_id)
                if stat == 'left':
                    inline_keyboard = joining_channel_keyboard
                    bot_methods.send_message_with_keyboard(
                        "You're not joined in our channel!\nPlease join to access our service.", chat_id, inline_keyboard)
            else:
                if user.credit >= size_mb:
                    try:
                        video = bot_methods.get_file(file_id=file_id)
                        if video is not None:
                            video_json = json.loads(video)
                            path = video_json["result"]["file_path"]
                            add_new_download(user.id, file_name, size_mb)
                            bot_methods.download_file(
                                path, file_name+'.mp4')
                    except ValueError as error:
                        print('Caught this error: ' + repr(error))
                    bot_methods.send_chat_action('upload_video', chat_id)
                    update_user_credit(chat_id, size_mb)
                    time.sleep(5)
                    bot_methods.send_message(
                        "https://telapi.digi-arya.ir/downloads/"+file_name+".mp4", chat_id)
                    bot_methods.send_message(
                        "You can use this direct link for 1 month. Please save your Link.", chat_id)
                    update_download_status(file_name)

                else:
                    inline_keyboard = credit_charge_keyboard
                    bot_methods.send_message_with_keyboard(
                        "You don't have enough account credit to begin the download.\nPlease select one of the options below to debit your account.\nThank you",
                        chat_id, inline_keyboard)

        else:
            bot_methods.send_message(msg, "112042461")

        return Response('ok', status=200)
    else:
        return '<h1>Not OK</h1>'


def add_new_user(user_id):
    user = User.query.filter_by(telegram_id=user_id).first()
    if not user:
        user = User(telegram_id=user_id, credit=0)
        db.session.add(user)
        db.session.commit()
        return user, True
    else:
        return user, False


def add_new_download(user_id, file_name, file_size):

    download = Download.query.filter_by(file_name=file_name).first()
    if not download:
        download = Download(link="telegram", file_name=file_name,
                            file_wight=file_size, file_type="mp4", status=0, user_id=user_id)
        db.session.add(download)
        db.session.commit()
        print("A new download was added!")
        return True


def update_user_credit(user_id, usage):
    user = User.query.filter_by(telegram_id=user_id).first()
    if user:
        user.credit -= usage
        db.session.commit()
        return True
    else:
        print("User not found!")


def update_download_status(file_name):

    download = Download.query.filter_by(file_name=file_name).first()
    if download:
        download.status = 1
        db.session.commit()
        return True
    else:
        print("Something went wrong!")


def status(chat_id):
    user = User.query.filter_by(telegram_id=chat_id).first()
    if user.credit == 0:
        bot_methods.send_message(
            f"Your credit is: {user.credit} Mb", chat_id)
        bot_methods.send_message(
            "Please charge your account to start your download.", chat_id)
    else:
        bot_methods.send_message(
            f"Your credit is: {user.credit} Mb", chat_id)


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
