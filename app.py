from flaskapp import bot_methods, app
from config.secret import LINK
from asyncio import run, gather


async def async_download(func1, func2):

    await gather(func1, func2)


if __name__ == "__main__":
    run(async_download(bot_methods.send_async_message(
        "Your download has started!\nPlease wait.", "112042461"), bot_methods.download_media("okok")))

    # bot_methods.remove_webhook()
    # bot_methods.set_webhook(LINK)
    app.run(debug=True, port=8000)
