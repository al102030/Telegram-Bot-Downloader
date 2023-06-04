from flaskapp import bot_methods, app
from config.secret import LINK, API_ID, API_HASH
from telethon import TelegramClient


if __name__ == "__main__":

    client = TelegramClient("cli-session", API_ID, API_HASH)

    async def main():
        # Now you can use all client methods listed below, like for example...
        await client.send_message('me', 'Hello to myself!')

    with client:
        client.loop.run_until_complete(main())
    # bot_methods.remove_webhook()
    # bot_methods.set_webhook(LINK)
    # app.run(debug=True)
