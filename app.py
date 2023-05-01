from flaskapp import app, bot_methods
from config.secret import url
from flaskapp.models import User


if __name__ == "__main__":
    user = User.query.filter_by(telegram_id="112042461").first()
    bot_methods.remove_webhook()
    bot_methods.set_webhook(url)
    app.run(debug=True)
