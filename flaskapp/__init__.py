from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from TLMethods.Telegram import Telegram
from config.secret import token


app = Flask(__name__)
app.config['SECRET_KEY'] = '4edc0281f3899c05d40adf12a1102fef'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/al102030/Telegram-Bot-Downloader/site.db'
db = SQLAlchemy(app)
from flaskapp import models  # noqa: E402

bcrypt = Bcrypt(app)
bot_methods = Telegram(token)

from flaskapp import routes  # noqa: E402
