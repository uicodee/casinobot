import asyncio

from aiogram import Bot, Dispatcher
from handlers.commands import router as command_router
from handlers.buttons import router as button_router
from handlers.callbacks import router as callback_router
from handlers.content import router as content_router

from config import TOKEN

dp = Dispatcher()


async def main() -> None:
    dp.include_router(command_router)
    dp.include_router(button_router)
    dp.include_router(callback_router)
    dp.include_router(content_router)
    bot = Bot(token=TOKEN, parse_mode="HTML")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
