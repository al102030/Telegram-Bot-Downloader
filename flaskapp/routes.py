from flask import request, Response
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
                bot_methods.send_message(
                    f"You are not registered in my user's list, Welcome! (Your Telegram ID: {chat_id})", chat_id)
                user = User(telegram_id=chat_id, credit=0)
                db.session.add(user)
                db.session.commit()
        else:
            if txt == "/c1":
                bot_methods.send_message(txt, chat_id)
            # elif txt == "/c2":
            #     bot_methods.send_message("Login: ", chat_id)
            # elif txt == "/c3":
            #     bot_methods.send_message("About: ", chat_id)
            # elif txt == "/c4":
            #     bot_methods.send_message("Logout: ", chat_id)
            # elif txt == "/c5":
            #     bot_methods.send_message("Please Choose a Username: ", chat_id)

        return Response('ok', status=200)
    else:
        return '<h1>Not OK</h1>'
