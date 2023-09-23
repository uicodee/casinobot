from aiogram import Router, types
from aiogram.fsm.context import FSMContext

from states import GameForm

router = Router()


@router.message(GameForm.dice)
async def on_dice(message: types.Message, state: FSMContext) -> None:
    data = await state.get_data()
    if message.dice is not None:
        if message.dice.emoji == data.get('dice'):
            await message.answer(
                text=str(message.dice.value)
            )
        else:
            await message.answer(
                text=f"Please send only {data.get('dice')} dice"
            )
    else:
        await message.answer(
            text="Please send only dice"
        )
