from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from TLMethods.Telegram import Telegram
from config.secret import token, url

app = Flask(__name__)
app.config['SECRET_KEY'] = '4edc0281f3899c05d40adf12a1102fef'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

bot_methods = Telegram(token)

from flaskapp import routes  # noqa: E402
