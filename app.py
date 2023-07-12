from threading import Thread
from flaskapp import bot_methods, app
from config.secret import LINK
from asyncio import run, gather


async def async_download(func1, func2):

    await gather(func1, func2)


def f():
    run(async_download(bot_methods.send_async_message(
        "Your download has started!\nPlease wait.", "112042461"), bot_methods.download_media("okok")))


if __name__ == "__main__":
    t = Thread(target=f)
    t.start

    # bot_methods.remove_webhook()
    # bot_methods.set_webhook(LINK)
    # app.run(debug=True, port=8000)
