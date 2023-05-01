from flask import request, Response
from flaskapp.models import User, Download
from flaskapp import app, bot_methods, db, bcrypt

registration = 0


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        chat_id = msg['message']['chat']['id']
        txt = msg['message']['text']
        user = User.query.filter_by(telegram_id=chat_id)
        if user:
            bot_methods.send_message(
                "You already registered in my user's list, Welcome back!", chat_id)
        if txt == "/c1":
            bot_methods.send_message("Your Status: ", chat_id)
        elif txt == "/c2":
            bot_methods.send_message("Login: ", chat_id)
        elif txt == "/c3":
            bot_methods.send_message("About: ", chat_id)
        elif txt == "/c4":
            bot_methods.send_message("Logout: ", chat_id)
        elif txt == "/c5":
            registration = 1
            bot_methods.send_message("Please Choose a Username: ", chat_id)

        return Response('ok', status=200)
    else:
        return '<h1>Not OK</h1>'
