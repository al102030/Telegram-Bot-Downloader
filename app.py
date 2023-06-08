from flaskapp import bot_methods, app
# from telethon import TelegramClient
from config.secret import LINK  # , API_ID, API_HASH
# from asyncio import run


if __name__ == "__main__":
    # async def get_message():
    #     async with TelegramClient('cli', API_ID, API_HASH) as client:
    #         messages = await client.get_messages(entity=6235055313)
    #         for item in messages:
    #             if 'user_id=112042461' in str(item):
    #                 message = item
    #                 break
    #         print(message)

    # run(get_message())

    # =============================================================================
    # client = TelegramClient("cli-session", API_ID, API_HASH)
    # FILE_ID = "BQACAgQAAxkBAAIL5WSAxVv0jFQ7ljCTQUIa8uXSR9XEAAJ2DwACYpDpU8-64EHSRR5JLwQ"
    # MESSAGE_ID = '3045'
    # FILE_NAME = "KMPlayer.0.3.2.Mac.zip"

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

    bot_methods.remove_webhook()
    bot_methods.set_webhook(LINK)
    app.run(debug=True)
