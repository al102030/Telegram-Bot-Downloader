from flask import request, Response, url_for, redirect
from flaskapp.models import User
from flaskapp import app, bot_methods, db


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        chat_id = msg['message']['chat']['id']
        txt = msg['message']['text']
        user = User.query.filter_by(telegram_id=chat_id).first()
        if txt == "/start":
            if user:
                bot_methods.send_message(
                    f"You already registered in my user's list, Welcome back! (Your Telegram ID: {chat_id})", chat_id)
            else:
                # bot_methods.forward_message(chat_id, "-1001976338494", "4")
                bot_methods.send_message(
                    f"You are not registered in my user's list, Welcome! (Your Telegram ID: {chat_id})", chat_id)
                user = User(telegram_id=chat_id, credit=0)
                db.session.add(user)
                db.session.commit()
        else:
            if txt == "/c1":
                status(chat_id=chat_id)
            elif txt == "/c2":
                bot_methods.send_message("""Hi there! 
                                        I'm a smart Bot that can help you to download your file from a variety of Internet services like YouTube, Instagram, etc., faster and safer.
                                        Thank you for your trustiness.
                                        Let's go on...""", chat_id)
            elif txt == "/c3":
                bot_methods.send_message(
                    "Before Start your download please join our channel: ", chat_id)
            # elif txt == "/c4":
            #     bot_methods.send_message("Logout: ", chat_id)
            # elif txt == "/c5":
            #     bot_methods.send_message("Please Choose a Username: ", chat_id)

        return Response('ok', status=200)
    else:
        return '<h1>Not OK</h1>'


@app.route("/status", methods=["GET", "POST"])
def status(chat_id):
    if request.method == 'POST':
        user = User.query.filter_by(telegram_id=chat_id).first()
        if user.credit == 0:
            bot_methods.send_message(
                f"Your credit is: {user.credit} Mb", chat_id)
            bot_methods.send_message(
                "Please charge your account to start your download.", chat_id)
        else:
            bot_methods.send_message(
                f"Your credit is: {user.credit} Mb", chat_id)
    return redirect(url_for('index'))
