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
    server_link = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Download('{self.link}', '{self.file_wight}', '{self.file_type}')"


class Methods:
    def add_new_user(self, user_id):
        user = User.query.filter_by(telegram_id=user_id).first()
        if not user:
            user = User(telegram_id=user_id, credit=0)
            db.session.add(user)
            db.session.commit()
            return user, True
        else:
            return user, False

    def add_new_download(self, url, user_id, file_name, file_size):

        download = Download.query.filter_by(file_name=file_name).first()
        if not download:
            download = Download(link=url, file_name=file_name,
                                file_wight=file_size, file_type="mp4", status=0, user_id=user_id)
            db.session.add(download)
            db.session.commit()
            print("A new download was added!")
            return True

    def update_user_credit(self, user_id, usage):
        user = User.query.filter_by(telegram_id=user_id).first()
        if user:
            user.credit -= usage
            db.session.commit()
            print("User credit decreased!")
        else:
            print("User not found!")

    def update_download_status(self, download_id):

        download = Download.query.filter_by(
            id=download_id, status=0).first()
        if download:
            download.status = 1
            db.session.commit()
            print("Download process completed!")
        else:
            print("Something went wrong in download status updating!")

    def update_download_size(self, file_name, file_size):

        download = Download.query.filter_by(file_name=file_name).first()
        if download:
            download.file_wight = file_size
            db.session.commit()
            return True
        else:
            print("Something went wrong in updating download size!")

    def check_link_in_db(self, url, user_id, file_name):

        download = Download.query.filter_by(
            link=url, user_id=user_id, file_name=file_name).first()
        if not download:
            return False, None
        else:
            return True, download.id

    def status(self, chat_id):
        user = User.query.filter_by(telegram_id=chat_id).first()
        if user.credit == 0:
            return f"Your credit is: {user.credit} Mb.\nPlease charge your account to start your download."
        else:
            return f"Your credit is: {user.credit} Mb"

    def reorder_old_download(self, download_id):
        current_time = dt.datetime.now()
        time_stamp = current_time.timestamp()
        download = Download.query.filter_by(id=download_id).first()
        if download:
            download.date_downloaded = time_stamp
            download.date_delete = time_stamp+2592000
            download.server_link = ""
            download.status = 0
            db.session.commit()
            print("Download record reordered.")
        else:
            print("Something went wrong in reordering a download record process!")

    def update_server_link(self, download_id, link):

        download = Download.query.filter_by(
            id=download_id).first()
        if download:
            download.server_link = link
            db.session.commit()
            print("Server link updated.")
        else:
            print("Something went wrong in updating server link!")
