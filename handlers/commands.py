from aiogram import types, Router
from aiogram.filters import Command

from keyboards import inline_keyboard


router = Router()


@router.message(Command(commands=['start']))
async def on_cmd_start(message: types.Message) -> None:
    await message.answer(
        text="Salom",
        reply_markup=inline_keyboard()
    )
