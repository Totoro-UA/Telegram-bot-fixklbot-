try:
    import t_bot.fix as fix
    import t_bot.config as config
except ModuleNotFoundError:
    import fix as fix
    import config as config

import datetime
import logging

from aiogram import Bot, Dispatcher, executor, types

# setting logs level
logging.basicConfig(level=logging.INFO)

# bot init
bot = Bot(token=config.API_TOKEN)

dp = Dispatcher(bot)


# echo
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(fix.fix_func(message.text))

    """Activity logging"""
    u_mention = message.from_user.mention
    u_fname = message.from_user.full_name
    now_time = datetime.datetime.now()
    now_time = now_time.strftime("%Y-%m-%d  %H:%M:%S")

    logpath = r'log.txt'
    with open(logpath, "a") as f:
        f.write("time: " + str(now_time) + "    user: " + str(u_mention) + "    name: " + str(u_fname))
        f.write("\n____send____\n" + message.text + "\n___answer___\n" + fix.fix_func(message.text) + "\n" + 32 * "_" + "\n")

# exec long polling
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
