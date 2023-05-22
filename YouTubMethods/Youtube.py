import requests
from pytube import YouTube, exceptions


class Youtube:
    def __init__(self, link) -> None:
        self.link = link

    def check_url(self):
        pattern = '"playabilityStatus":{"status":"ERROR","reason":"Video unavailable"'
        request = requests.get(self.link, timeout=20)
        return False if pattern in request.text else True

    def file_size(self):
        youtube = YouTube(self.link)
        return youtube.streams.get_highest_resolution().filesize

    def youtube_download(self, chat_id):
        try:
            youtube = YouTube(self.link)
            youtube.streams.filter(progressive=True, file_extension='mp4').order_by(
                'resolution').asc().first().download(output_path='DL', filename=chat_id+'-youtube.mp4')
        except exceptions.AgeRestrictedError as error:
            return error
        except exceptions.VideoUnavailable as error:
            return error
        except exceptions.ExtractError as error:
            return error
        except exceptions.PytubeError as error:
            return error
        else:
            return "No exceptions were thrown."
