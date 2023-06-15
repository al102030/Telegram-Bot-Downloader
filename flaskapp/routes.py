import json
import secrets
import pickle
from asyncio import run, gather
import os
from pytube import YouTube, exceptions
import requests
from flask import request, Response
from flaskapp import app, bot_methods
from config.secret import GOOGLE_USER, GOOGLE_PASSWORD
from flaskapp.models import User, Download, Methods
from view.Menus import joining_channel_keyboard, credit_charge_keyboard, simple_options, start_again


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        channel_id = "-1001904767094"
        msg = request.get_json()
        db_methods = Methods()
        is_text = None
        is_video = None
        is_document = None
        try:
            is_text = msg['message']['text']
        except KeyError as error:
            print("Text not found", error)

        try:
            is_video = msg['message']['video']
        except KeyError as error:
            print("Video not found", error)
        try:
            is_document = msg['message']['document']
        except KeyError as error:
            print("Document not found", error)

        if "callback_query" in msg:
            callback_id = msg['callback_query']['id']
            callback_from_id = msg['callback_query']['from']['id']
            callback_data = msg['callback_query']['data']
            user, new_user = db_methods.add_new_user(callback_from_id)
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
            user, new_user = db_methods.add_new_user(chat_id)
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
                    credit = db_methods.status(chat_id=chat_id)
                    bot_methods.send_message(credit, chat_id)
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
                    user, new_user = db_methods.add_new_user(chat_id)
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
                        if user.credit > 0:
                            login_to_youtube(GOOGLE_USER, GOOGLE_PASSWORD)
                            with open('cookies.pkl', 'rb') as file:
                                cookies = pickle.load(file)
                            yt = YouTube(txt)
                            print(yt.video_id)
                            # yt.cookies = cookies
                            # file_name = str(yt.streams.first().default_filename).replace(
                            #     " ", "-")[:-5]  # secrets.token_hex(8)
                            # db_methods.add_new_download(
                            #     txt, user.id, file_name, 0)
                            # resolution_select_keyboard = []
                            # for stream in (yt.streams.order_by('resolution').desc().filter(adaptive=True, file_extension='mp4')):
                            #     lst = []
                            #     dictionary = {}
                            #     dictionary['text'] = stream.resolution
                            #     dictionary['callback_data'] = stream.resolution
                            #     lst.append(dictionary)
                            #     resolution_select_keyboard.append(lst)
                            # bot_methods.send_message_with_menu("Please select the resolution that you want to download",
                            #                                    chat_id, resolution_select_keyboard)
                elif txt == '1080p' or txt == '720p' or txt == '480p' or txt == '360p' or txt == '240p' or txt == '144p':
                    if user.credit > 0:
                        download = Download.query.filter_by(
                            status=0, user_id=user.id).first()
                        if download:
                            user = User.query.filter_by(
                                telegram_id=chat_id).first()
                            with open('cookies.pkl', 'rb') as file:
                                cookies = pickle.load(file)
                            yt = YouTube(download.link)
                            yt.cookies = cookies
                            stream = yt.streams.filter(res=txt).first()
                            if stream:
                                size_mb = stream.filesize / 1000000
                                if size_mb < 0:
                                    size_mb = 1
                                else:
                                    size_mb = round(size_mb)
                                db_methods.update_download_size(
                                    download.file_name, size_mb)
                                if user.credit >= size_mb:
                                    try:
                                        print(size_mb)
                                        stream.download(
                                            output_path='/usr/share/nginx/html/static/', filename=download.file_name+'.mp4')
                                        bot_methods.send_chat_action(
                                            'upload_video', chat_id)
                                        os.chmod(
                                            f'/usr/share/nginx/html/static/{download.file_name}.mp4', 0o755)
                                        bot_methods.send_message(
                                            "https://telapi.digi-arya.ir/static/"+download.file_name+".mp4", chat_id)
                                        db_methods.update_user_credit(
                                            chat_id, size_mb)
                                        db_methods.update_download_status(
                                            download.file_name)
                                    except ValueError as error:
                                        print(
                                            'Caught this error: ' + repr(error))
                                else:
                                    inline_keyboard = credit_charge_keyboard
                                    bot_methods.send_message_with_keyboard(
                                        "You don't have enough account credit to begin the download.\nPlease select one of the options below to debit your account.\nThank you",
                                        chat_id, inline_keyboard)
                            else:
                                bot_methods.send_message(
                                    "File doesn't Exist.\nPlease try another Resolution or link\nThanks.",
                                    chat_id)

                else:
                    bot_methods.send_message(
                        "I don't know what you're expecting of me?", chat_id)
        elif is_video or is_document:
            chat_id = msg['message']['chat']['id']
            if is_video:
                file_name = secrets.token_hex(8)  # +'.mp4'
                file_size = msg['message']['video']['file_size']
                mime_type = msg['message']['video']['mime_type']
            elif is_document:
                file_name = msg['message']['document']['file_name']
                file_size = msg['message']['document']['file_size']
                mime_type = msg['message']['document']['mime_type']
            size_mb = int(file_size)/1000000
            if size_mb < 0:
                size_mb = 1
            else:
                size_mb = round(size_mb)
            user, new_user = db_methods.add_new_user(chat_id)
            ans = bot_methods.get_chat_member(channel_id, chat_id)
            json_data = json.loads(ans)
            stat = json_data['result']['status']
            if new_user:
                bot_methods.send_message(
                    f"You are not registered in my user's list,Welcome! (Your Telegram ID: {chat_id})", chat_id)
            elif stat == 'left':
                inline_keyboard = joining_channel_keyboard
                bot_methods.send_message_with_keyboard(
                    "You're not joined in our channel!\nPlease join to access our service.", chat_id, inline_keyboard)
            else:
                if user.credit >= size_mb:
                    try:
                        db_methods.add_new_download('telegram', user.id,
                                                    file_name, size_mb)
                        run(async_download(bot_methods.download_media(
                            file_name, chat_id, mime_type), bot_methods.send_chat_action('upload_video', chat_id)))
                        db_methods.update_user_credit(chat_id, size_mb)
                        os.chmod(
                            f'/usr/share/nginx/html/static/{file_name}.mp4', 0o755)
                        bot_methods.send_message(
                            f"https://telapi.digi-arya.ir/static/{file_name}.mp4", chat_id)
                        bot_methods.send_message(
                            "You can use this direct link for 1 month. Please save your Link.", chat_id)
                        db_methods.update_download_status(file_name)
                    except ValueError as error:
                        print('Caught this error: ' + repr(error))
                else:
                    inline_keyboard = credit_charge_keyboard
                    bot_methods.send_message_with_keyboard(
                        "You don't have enough account credit to begin the download.\nPlease select one of the options below to debit your account.\nThank you",
                        chat_id, inline_keyboard)
        else:
            bot_methods.send_message(msg, "112042461")

        return Response('ok', status=200)
    else:
        return '<h1>Telegram Bot Downloader</h1>'


def login_to_youtube(username, password):
    session = requests.Session()
    login_data = {
        'username': username,
        'password': password
    }
    response = session.post('https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&hl=en&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26feature%3Dsign_in_button%26hl%3Den%26next%3D%252F&flowName=GlifWebSignIn&flowEntry=ServiceLogin', data=login_data)

    if response.status_code == 200:
        print("Logged in to YouTube successfully.")
        with open('cookies.pkl', 'wb') as file:
            pickle.dump(session.cookies, file)
    else:
        raise exceptions.AgeRestrictedError(
            "Failed to log in to YouTube.")


async def async_download(func1, func2):
    # Start all coroutines concurrently
    await gather(func1, func2)
