import asyncio
import sys
import logging
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import BaseMiddleware
from apscheduler.schedulers.asyncio import AsyncIOScheduler

logging.basicConfig(level=logging.INFO)
TOKEN = ''
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
    id =
    await message.answer(
        text="Тест 1"
    )
    scheduler.add_job(bot.send_message, 'cron',day_of_week='mon-fri', hour=7, minute=30, args=(id, "Тест 2"))


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
