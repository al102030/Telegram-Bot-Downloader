import time
import os
import json
import requests
import aiohttp
from telethon import TelegramClient
from config.secret import API_ID, API_HASH

# Telegram methods class


class Telegram:
    def __init__(self, token):
        self.token = token

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

    async def send_async_message(self, text1, text2, chat_id):
        req_url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        payload1 = {
            "text": text1,
            "chat_id": chat_id,
            "disable_web_page_preview": False,
            "disable_notification": False,
        }
        payload2 = {
            "text": text2,
            "chat_id": chat_id,
            "disable_web_page_preview": False,
            "disable_notification": False,
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(req_url, json=payload1, headers=headers, timeout=20) as response1:
                print(await response1.text())
        time.sleep(3)
        async with aiohttp.ClientSession() as session:
            async with session.post(req_url, json=payload2, headers=headers, timeout=20) as response2:
                print(await response2.text())

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

    async def send_chat_action(self, action, chat_id):

        url = f"https://api.telegram.org/bot{self.token}/sendChatAction"

        payload = {
            "action": action,
            "chat_id": chat_id
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, headers=headers, timeout=20) as response:
                print(await response.text())

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
        download_path = os.path.join(
            "/usr/share/nginx/html/static/", file_name)
        url = f"https://api.telegram.org/file/bot{self.token}/{file_path}"
        response = requests.get(url, stream=True, timeout=30)
        if response.ok:
            print("saving to", os.path.abspath(download_path))
            with open(download_path, 'wb') as file:
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

    async def download_media(self, file_name, chat_id, mime_type):
        path = "/usr/share/nginx/html/static/"
        async with TelegramClient('cli', API_ID, API_HASH) as client:
            # dialogs = await client.get_dialogs()
            # for dialog in dialogs:
            #     if dialog.title == 'Al102030':
            #         dialog_id = dialog.id
            # print(dialog_id)
            messages = await client.get_messages(entity=6235055313)
            print(messages[0])
            # print(messages[0])
            # print(messages[0].document.attributes[0].file_name, messages[0].document.size,
            # messages[0].document.id, messages[0].document.access_hash)
            for item in messages:
                if str(file_name) in str(item):
                    message = item
                    break
                elif str(chat_id) in str(item):
                    message = item
                    break

            # self.send_message(str(message), "112042461")
            message = await client.get_messages(
                message.peer_id.user_id, ids=message.id)
            print('================================================\n')
            print(message)
            # print(message.peer_id.user_id, message.id)

            # try:
            #     print(message.media, "Media part")
            # except:
            #     print("No media", "112042461")
            # try:
            #     print(message.file, "File part")
            # except:
            #     print("No file", "112042461")
            # try:
            #     print(message.message, "Message part")
            # except:
            #     print("No Message", "112042461")
            file = path+file_name
            if message.media:
                if "application/" in mime_type:
                    print("it is a document(media) or app!")
                    await client.download_media(message.media, file=file)
                    print("Document downloaded!(media)")
                elif mime_type == "video/mp4":
                    print("it is a video!")
                    file += '.mp4'
                    await client.download_media(message.media, file=file)
                    print("Video downloaded!(media)")
                else:
                    print("Media format not supported!")
            elif message.message:
                ID_ = message.message
                print(ID_)
                print(mime_type)
                # if "application/" in mime_type:
                #     print("it is a document(file) or app!")
                #     await client.download_media(message.message, file=file)
                #     print("Document downloaded!(message)")
                # elif mime_type == "video/mp4":
                #     print("it is a video!")
                #     file += '.mp4'
                #     await client.download_file(message.message, file=file)
                #     print("Video downloaded!(message)")
                # else:
                #     print("File format not supported!")
            else:
                print("The message doesn't contain media.")

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

    def restrict_chat_member(self, chat_id, user_id):
        url = f"https://api.telegram.org/bot{self.token}/restrictChatMember"
        payload = {
            "chat_id": chat_id,
            "user_id": user_id,
            "disable_notification": False,
            "can_send_messages": False,
            "can_send_media_messages": False,
            "can_send_other_messages": False,
            "can_add_web_page_previews": False,
            "until_date": 15
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(
            url, json=payload, headers=headers, timeout=20)

        return response.text

    def set_chat_permissions(self, chat_id):
        url = f"https://api.telegram.org/bot{self.token}/setChatPermissions"

        permissions = {
            "can_send_messages": False,
            "can_send_media_messages": False,
            "can_send_polls": False,
        }
        payload = {
            "chat_id": chat_id,
            "permissions": json.dumps(permissions),
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(
            url, json=payload, headers=headers, timeout=20)

        if response.status_code == 200:
            print('Permissions updated successfully.')
            return response.text
        else:
            print(
                f'Error updating permissions: {response.status_code} - {response.text}')
