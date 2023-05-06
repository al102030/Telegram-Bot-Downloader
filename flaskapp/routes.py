import json
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
            callback_id = msg['callback_query']['id']
            callback_from_id = msg['callback_query']['from']['id']
            callback_data = msg['callback_query']['data']
            ans = bot_methods.get_chat_member(channel_id, callback_from_id)
            json_data = json.loads(ans)
            stat = json_data['result']['status']
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
                        # options = confirm_download
                        # bot_methods.send_message_with_menu(
                        #     "Are you Sure?", chat_id, options)
                elif txt == "/c4":
                    options = simple_options
                    bot_methods.send_message_with_menu(
                        "Are you Sure?", chat_id, options)
                elif "ll" in txt:
                    # youtube = YouTube(txt)
                    # file_size = math.ceil(
                    #     (youtube.streams.get_highest_resolution().filesize)/1000000)
                    user = User.query.filter_by(
                        telegram_id=chat_id).first()
                    if (user.credit - 2) >= 0:
                        bot_methods.send_message(
                            app.send_static_file("DL/weeknd.mp4"), chat_id)  # "Your download has already started."

        return Response('ok', status=200)
    else:
        return '<h1>Not OK</h1>'


@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)


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
