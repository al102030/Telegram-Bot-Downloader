import requests
import os
from telethon import TelegramClient
from config.secret import API_ID, API_HASH


class Telegram:
    def __init__(self, token):
        self.token = token
        self.client = TelegramClient(None, API_ID, API_HASH)

    def get_me(self):
        url = f"https://api.telegram.org/bot{self.token}/getMe"

        headers = {"accept": "application/json"}

        response = requests.post(url, headers=headers, timeout=20)

        return response

    def get_update(self):
        url = f"https://api.telegram.org/bot{self.token}/getUpdates"
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }
        payload = {
            "offset": None,
            "timeout": None
        }
        response = requests.post(
            url, json=payload, headers=headers, timeout=20)
        return response

    def send_message(self, text, chat_id):
        req_url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        payload = {
            "text": text,
            "chat_id": chat_id,
            "disable_web_page_preview": False,
            "disable_notification": False,
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }
        response = requests.post(req_url, json=payload,
                                 headers=headers, timeout=20)
        return response

    def send_message_with_keyboard(self, text, chat_id, keyboard):
        req_url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        payload = {
            "text": text,
            "chat_id": chat_id,
            "disable_web_page_preview": False,
            "disable_notification": False,
            "parse_mode": 'html',
            "reply_markup": {
                "inline_keyboard": keyboard
            }  # reply_markup
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }
        response = requests.post(req_url, json=payload,
                                 headers=headers, timeout=20)
        return response

    def send_message_with_menu(self, text, chat_id, menu):
        req_url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        payload = {
            "text": text,
            "chat_id": chat_id,
            "disable_web_page_preview": False,
            "disable_notification": False,
            "parse_mode": 'html',
            "reply_markup": {
                "keyboard": menu,
                "resize_keyboard": True,
                "one_time_keyboard": True
            }  # reply_markup
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }
        response = requests.post(req_url, json=payload,
                                 headers=headers, timeout=20)
        return response

    def answer_callback_query(self, text, query_id, show_alert):
        req_url = f"https://api.telegram.org/bot{self.token}/answerCallbackQuery"
        payload = {
            "text": text,
            "callback_query_id": query_id,
            "disable_web_page_preview": False,
            "disable_notification": False,
            "show_alert": show_alert
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }
        response = requests.post(req_url, json=payload,
                                 headers=headers, timeout=20)
        return response

    def forward_message(self, message_id, chat_id, from_chat_id):

        url = f"https://api.telegram.org/bot{self.token}/forwardMessage"

        payload = {
            "message_id": message_id,
            "disable_notification": False,
            "chat_id": chat_id,
            "from_chat_id": from_chat_id
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(
            url, json=payload, headers=headers, timeout=20)

        return response

    def send_photo(self, chat_id, photo, caption=""):

        url = f"https://api.telegram.org/bot{self.token}/sendPhoto"

        payload = {
            "photo": photo,
            "caption": caption,
            "disable_notification": False,
            "reply_to_message_id": None,
            "chat_id": chat_id
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(
            url, json=payload, headers=headers, timeout=20)

        return response

    def set_webhook(self, host_link):

        url = f"https://api.telegram.org/bot{self.token}/setWebhook"

        payload = {
            "url": host_link,
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(
            url, json=payload, headers=headers, timeout=20)

        return response

    def remove_webhook(self):

        url = f"https://api.telegram.org/bot{self.token}/setWebhook?remove="

        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(url, headers=headers, timeout=20)

        return response

    def send_video(self, pth, chat_id, caption=""):
        url = f"https://api.telegram.org/bot{self.token}/sendVideo"

        my_file = open(pth, 'rb')

        parameters = {
            "caption": caption,
            "disable_notification": False,
            "reply_to_message_id": None,
            "chat_id": chat_id
        }
        files = {
            "video": my_file,
        }

        response = requests.post(url, data=parameters, files=files, timeout=30)

        return response.text

    def send_audio(self, pth, chat_id, caption=""):

        url = f"https://api.telegram.org/bot{self.token}/sendAudio"

        my_file = open(pth, 'rb')
        parameters = {
            "caption": caption,
            "disable_notification": False,
            "reply_to_message_id": None,
            "chat_id": chat_id
        }
        files = {
            "audio": my_file
        }

        response = requests.post(url, data=parameters, files=files, timeout=30)

        return response.text

    def send_document(self, pth, chat_id, caption=""):

        url = f"https://api.telegram.org/bot{self.token}/sendDocument"

        my_file = open(pth, 'rb')
        parameters = {
            "caption": caption,
            "disable_notification": False,
            "reply_to_message_id": None,
            "chat_id": chat_id
        }
        files = {
            "document": my_file
        }

        response = requests.post(url, data=parameters, files=files, timeout=30)

        return response.text

    def send_sticker(self, sticker, chat_id):

        url = f"https://api.telegram.org/bot{self.token}/sendSticker"

        payload = {
            "sticker": sticker,
            "chat_id": chat_id,
            "disable_notification": False,
            "reply_to_message_id": None
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(
            url, json=payload, headers=headers, timeout=20)

        return response.text

    def send_voice(self, voice, chat_id):

        url = f"https://api.telegram.org/bot{self.token}/sendVoice"

        payload = {
            "voice": voice,
            "disable_notification": False,
            "reply_to_message_id": None,
            "chat_id": chat_id
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(
            url, json=payload, headers=headers, timeout=20)

        return response.text

    def send_location(self, lat, lan, chat_it):

        url = f"https://api.telegram.org/bot{self.token}/sendLocation"

        payload = {
            "latitude": lat,
            "longitude": lan,
            "disable_notification": False,
            "reply_to_message_id": None,
            "chat_id": chat_it
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(
            url, json=payload, headers=headers, timeout=20)

        return response.text

    # typing, upload_photo, record_video, upload_video, record_video_note, upload_video_note
    # record_voice, upload_voice, upload_document, choose_sticker, find_location

    def send_chat_action(self, action, chat_id):

        url = f"https://api.telegram.org/bot{self.token}/sendChatAction"

        payload = {
            "action": action,
            "chat_id": chat_id
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(
            url, json=payload, headers=headers, timeout=20)

        print(response.text)

    def get_user_profile_photos(self, user_id):

        url = f"https://api.telegram.org/bot{self.token}/getUserProfilePhotos"

        payload = {
            "user_id": user_id,
            "offset": None,
            "limit": None
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(
            url, json=payload, headers=headers, timeout=20)

        return response.text

    def get_file(self, file_id):

        url = f"https://api.telegram.org/bot{self.token}/getFile"

        payload = {
            "file_id": file_id}
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(
            url, json=payload, headers=headers, timeout=20)

        return response.text

    def download_file(self, file_path, file_name):
        Download_path = os.path.join(
            "/usr/share/nginx/html/static/", file_name)
        url = f"https://api.telegram.org/file/bot{self.token}/{file_path}"
        response = requests.get(url, stream=True, timeout=30)
        if response.ok:
            print("saving to", os.path.abspath(Download_path))
            with open(Download_path, 'wb') as file:
                file.write(response.content)
                # for chunk in response.iter_content(chunk_size=1024 * 8):
                #     if chunk:
                #         file.write(chunk)
                #         file.flush()
                #         os.fsync(file.fileno())
                print("Your download is completed!")
        else:
            print("Download failed: status code\n",
                  response.status_code, response.text)

    async def tt_download_file(self, file_id):
        try:
            recipient = '@A_D_K'
            self.client.start()
            entity = self.client.get_entity(recipient)
            # await self.client.download_media(file_id)
            await self.client.send_message(entity, "hooryaaa")
            self.client.disconnect()
            print("File downloaded successfully.")
            # return True
        except ValueError as error:
            print("Error downloading file:", str(error))
            # return False

    def get_chat_member(self, channel_id, chat_id):

        url = f"https://api.telegram.org/bot{self.token}/getChatMember"

        payload = {
            "chat_id": channel_id,
            "user_id": chat_id,
            "disable_notification": False
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(
            url, json=payload, headers=headers, timeout=20)

        return response.text
