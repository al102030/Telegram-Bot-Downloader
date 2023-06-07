from flaskapp import bot_methods, app
from asyncio import run, gather
from config.secret import API_ID, API_HASH  # ,LINK
from telethon import TelegramClient


if __name__ == "__main__":
    # client = TelegramClient("cli-session", API_ID, API_HASH)
    # FILE_ID = "BQACAgQAAxkBAAIL5WSAxVv0jFQ7ljCTQUIa8uXSR9XEAAJ2DwACYpDpU8-64EHSRR5JLwQ"
    # MESSAGE_ID = '3045'
    CHAT_ID = "112042461"
    # FILE_NAME = "KMPlayer.0.3.2.Mac.zip"

    async def channel_info(api_id, api_hash):
        async with TelegramClient('cli', api_id, api_hash) as client:
            # dialogs = await client.get_dialogs()
            # for dialog in dialogs:
            #     if dialog.title == 'Al102030':
            #         dialog_id = dialog.id
            messages = await client.get_messages(entity=6235055313)
            message = await client.get_messages(
                messages[0].peer_id.user_id, ids=messages[0].id)
            if message.media:
                await client.download_media(message.media, file=f'/usr/share/nginx/html/static/{messages[0].document.attributes[0].file_name}')
            else:
                print("The message doesn't contain media.")

    async def dl():
        # Start all coroutines concurrently
        await gather(channel_info(API_ID, API_HASH), bot_methods.send_chat_action('upload_video', CHAT_ID))

    run(dl())

    # document = await client.get_input_document(FILE_ID)
    # message = await client.get_messages('me', ids=MESSAGE_ID)
    # message = await client.get_messages('me', ids=MESSAGE_ID)
    # location = message.document
    # .document.id, messages[0].document.access_hash)
    # print(messages[0].document.attributes[0].file_name, messages[0].document.size,
    #       messages[0].document.id, messages[0].document.access_hash)
    # print(messages[0].peer_id.user_id)

    # input_document = InputDocument(
    # id=messages[0].document.id, access_hash=messages[0].document.access_hash, file_reference=messages[0].document.file_reference)
    # print(input_document)
    # with tqdm(unit='B', unit_scale=True, desc=messages[0].document.attributes[0].file_name) as t:
    # await client.download_media(input_document, file='/User/adarvishi/Desktop/file.zip')
    # file=messages[0].document.attributes[0].file_name,
    # progress_callback=lambda current, total: t.update_to(
    #     current),
    # )

    #   messages[0].document.file_name, messages[0].document.size)
    # for message in messages:
    #     # if message.file and message.file.id == FILE_ID:
    #     print(message.text)
    #     break
    # file_path = '/User/adarvishi/Desktop/'
    # await client.download_media(message.document)
    # file = await client.download_media(message=message, file_path='/User/adarvishi/Desktop/')
    # return (file)

    # print(out)

    # bot_methods.remove_webhook()
    # bot_methods.set_webhook(LINK)
    # app.run(debug=True)
