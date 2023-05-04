import json
from pytube import YouTube, exceptions
from flask import request, Response
from flaskapp import app, bot_methods, db
from flaskapp.models import User


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
                        inline_keyboard = [[
                            {
                                "text": "A",
                                "callback_data": "A1"
                            },
                            {
                                "text": "B",
                                "url": "https://t.me/al102030_D"
                            }],
                            [{
                                "text": "C",
                                "url": "https://www.google.com/"
                            }]
                        ]
                        bot_methods.send_message_with_keyboard(
                            "with keyboard", chat_id, inline_keyboard)
                else:
                    bot_methods.send_message(
                        f"You are not registered in my user's list, Welcome! (Your Telegram ID: {chat_id})", chat_id)
                    if stat == 'left':
                        inline_keyboard = [[
                            {
                                "text": "A",
                                "callback_data": "A1"
                            },
                            {
                                "text": "B",
                                "url": "https://t.me/al102030_D"
                            }],
                            [{
                                "text": "C",
                                "url": "https://www.google.com/"
                            }]
                        ]
                        bot_methods.send_message_with_keyboard(
                            "with keyboard", chat_id, inline_keyboard)
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
                        inline_keyboard = [[
                            {
                                "text": "I already joined!",
                                "callback_data": "A1"
                            },
                            {
                                "text": "Join to channel",
                                "url": "https://t.me/al102030_D"
                            }]
                        ]
                        bot_methods.send_message_with_keyboard(
                            "with keyboard", chat_id, inline_keyboard)
                    elif user.credit is 0:
                        inline_keyboard = [
                            [{
                                "text": "5-Gig",
                                "callback_data": "5g"
                            },
                                {
                                "text": "10-Gig",
                                "callback_data": "105"
                            }],
                            [{
                                "text": "20-Gig",
                                "callback_data": "20g"
                            },
                                {
                                "text": "30-Gig",
                                "callback_data": "30g"
                            }]
                        ]
                        bot_methods.send_message_with_keyboard(
                            "with keyboard", chat_id, inline_keyboard)
                    else:
                        bot_methods.send_message(
                            "Enter your YouTube Link to start your download: ", chat_id)
                elif txt == "/c4":
                    my_menu = [[
                        {
                            "text": "Yes",
                        },
                        {
                            "text": "No",
                        }]
                    ]
                    bot_methods.send_message_with_menu(
                        "Are you Sure?", chat_id, my_menu)
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
        youtube.streams.filter(progressive=True, file_extension='mp4').order_by(
            'resolution').desc().first().download(output_path='DL', filename=chat_id+'-youtube.mp4')
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
