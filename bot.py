import asyncio
import sys
import logging
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import BaseMiddleware
from apscheduler.schedulers.asyncio import AsyncIOScheduler

import scraper

logging.basicConfig(level=logging.INFO)
TOKEN = '8044322179:AAENnwqp3f8y2xkto-Vrd8W4AA0Rehf08AA'
bot=Bot(token=TOKEN)
dp=Dispatcher()

hello_router = Router(name='hello')


class SchedulerMiddleware(BaseMiddleware):
    def __init__(self, scheduler: AsyncIOScheduler):
        super().__init__()
        self._scheduler = scheduler

    async def __call__(self, handler, event, data):
        data["scheduler"] = self._scheduler
        return await handler(event, data)


@hello_router.message(Command(commands=["dueToday"]))
async def hello(message: Message, bot: Bot, scheduler: AsyncIOScheduler):
    id = -1002312275639
    await message.answer(
        text="Отправка напоминаний о дедлайнах включена!"
    )
    scheduler.add_job(bot.send_message, 'cron',day_of_week='mon-fri', hour=22, minute=20, args=(id, f"Сегодня истекают следующие домашние задания: \n"
                                                                                                   f"{scraper.process_response(scraper.response1)}"))


async def main():
    scheduler = AsyncIOScheduler(timezone='Asia/Yekaterinburg')
    scheduler.start()
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.update.middleware(
        SchedulerMiddleware(scheduler=scheduler),
    )
    dp.include_routers(hello_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        stream=sys.stdout,
        format="%(asctime)s - [%(levelname)s] -  %(name)s - "
               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    )
    asyncio.run(main())
