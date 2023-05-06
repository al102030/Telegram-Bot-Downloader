# from pytube import YouTube, exceptions


# class Youtube:
#     def __init__(self, link) -> None:
#         self.ln = link

#     def check_url(self):
#         pattern = '"playabilityStatus":{"status":"ERROR","reason":"Video unavailable"'
#         request = requests.get(tubeurl, timeout=20)
#         return False if pattern in request.text else True

#     def youtube_file_size(self):

#         return youtube.streams.get_highest_resolution().filesize

#     def youtube_download(self, chat_id):
#         try:
#             youtube = YouTube(self.link)

#             youtube.streams.filter(progressive=True, file_extension='mp4').order_by(
#                 'resolution').asc().first().download(output_path='DL', filename=chat_id+'-youtube.mp4')
#         except exceptions.AgeRestrictedError as error:
#             print(error)
#         except exceptions.VideoUnavailable as error:
#             print(error)
#         except exceptions.ExtractError as error:
#             print(error)
#         except exceptions.PytubeError as error:
#             print(error)
#         except exceptions.LiveStreamError as error:
#             print(error)
#         else:
#             print("No exceptions were thrown.")
