from aiogram import F, types, Router


router = Router()


@router.message(F.text == "🎯 Darts")
async def on_game_darts(message: types.Message) -> None:
    await message.answer(
        text="Siz 🎯 Darts o'ynini tanladingiz"
    )