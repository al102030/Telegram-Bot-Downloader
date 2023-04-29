from flask import request, Response
# from flaskapp.models import User, Download
from flaskapp import app, bot_methods


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        chat_id = msg['message']['chat']['id']
        txt = msg['message']['text']
        if txt == "Hi":
            bot_methods.send_message("Aleyk Hi", chat_id)
        else:
            bot_methods.send_message("What???", chat_id)
        return Response('ok', status=200)
    else:
        return '<h1>Not OK</h1>'
