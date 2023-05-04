import json
from pytube import YouTube, exceptions
from flask import request, Response
from flaskapp import app, bot_methods, db
from flaskapp.models import User
from view.Menus import joining_channel_keyboard, credit_charge_keyboard, simple_options


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        channel_id = "-1001904767094"
        msg = request.get_json()

        if "callback_query" in msg:
            callback_from_id = msg['callback_query']['from']['id']
            callback_data = msg['callback_query']['data']
            bot_methods.send_message(callback_data, callback_from_id)
        else:
            chat_id = msg['message']['chat']['id']
            txt = msg['message']['text']
            user = User.query.filter_by(telegram_id=chat_id).first()
            ans = bot_methods.get_chat_member(channel_id, chat_id)
            json_data = json.loads(ans)
            stat = json_data['result']['status']
            if txt == "/start":
                if user:
                    bot_methods.send_message(
                        f"You already registered in my user's list, Welcome back! (Your Telegram ID: {chat_id})", chat_id)
                    if stat == 'left':
                        inline_keyboard = joining_channel_keyboard
                        bot_methods.send_message_with_keyboard(
                            "You're not joined in our channel!\nPlease join to access our service.", chat_id, inline_keyboard)
                else:
                    bot_methods.send_message(
                        f"You are not registered in my user's list, Welcome! (Your Telegram ID: {chat_id})", chat_id)
                    if stat == 'left':
                        inline_keyboard = joining_channel_keyboard
                        bot_methods.send_message_with_keyboard(
                            "You're not joined in our channel!\nPlease join to access our service.", chat_id, inline_keyboard)
                    user = User(telegram_id=chat_id, credit=0)
                    db.session.add(user)
                    db.session.commit()
            else:
                if txt == "/c1":
                    if user:
                        status(chat_id=chat_id)
                    else:
                        user = User(telegram_id=chat_id, credit=0)
                        db.session.add(user)
                        db.session.commit()
                        status(chat_id=chat_id)
                elif txt == "/c2":
                    bot_methods.send_message("""Hi there!
                                            I'm a smart Bot that can help you to download your file from a variety of Internet services like YouTube, Instagram, etc., faster and safer.

                                            Thank you for your trustiness.

                                            Let's go on...""", chat_id)
                elif txt == "/c3":
                    if stat == 'left':
                        inline_keyboard = joining_channel_keyboard
                        bot_methods.send_message_with_keyboard(
                            "with keyboard", chat_id, inline_keyboard)
                    elif user.credit == 0:
                        inline_keyboard = credit_charge_keyboard
                        bot_methods.send_message_with_keyboard(
                            "with keyboard", chat_id, inline_keyboard)
                    else:
                        bot_methods.send_message(
                            "Enter your YouTube Link to start your download: ", chat_id)
                elif txt == "/c4":
                    options = simple_options
                    bot_methods.send_message_with_menu(
                        "Are you Sure?", chat_id, options)
                elif "youtube" in txt:
                    pass

        return Response('ok', status=200)
    else:
        return '<h1>Not OK</h1>'


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


def youtube_download(link, chat_id):
    try:
        youtube = YouTube(link)
        print(youtube.streams.get_highest_resolution().filesize)

        # youtube.streams.filter(progressive=True, file_extension='mp4').order_by(
        #     'resolution').asc().first().download(output_path='DL', filename=chat_id+'-youtube.mp4')
    except exceptions.AgeRestrictedError as error:
        print(error)
    except exceptions.VideoUnavailable as error:
        print(error)
    except exceptions.ExtractError as error:
        print(error)
    except exceptions.PytubeError as error:
        print(error)
    else:
        print("No exceptions were thrown.")
