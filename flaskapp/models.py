import datetime as dt
from flaskapp import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    telegram_id = db.Column(db.String(20), unique=True, nullable=False)
    mobile = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(120), unique=True)
    credit = db.Column(db.Integer, default=0)
    download = db.relationship('Download', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.telegram_id}', '{self.mobile}', '{self.credit}')"


class Download(db.Model):
    current_time = dt.datetime.now()
    time_stamp = current_time.timestamp()
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.Text, nullable=False)
    file_name = db.Column(db.String(30), nullable=False)
    file_wight = db.Column(db.Integer)
    file_type = db.Column(db.String(20))
    date_downloaded = db.Column(db.Integer, nullable=False, default=time_stamp)
    date_delete = db.Column(db.Integer, nullable=False,
                            default=time_stamp+2592000)
    status = db.Column(db.Integer, nullable=False, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Download('{self.link}', '{self.file_wight}', '{self.file_type}')"
