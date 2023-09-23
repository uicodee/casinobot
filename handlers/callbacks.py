from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext

from keyboards import back, inline_keyboard
from states import GameForm

router = Router()


@router.callback_query(F.data == "darts")
async def on_darts(callback: types.CallbackQuery, state: FSMContext) -> None:
    await callback.message.delete()
    await callback.message.answer_dice(
        emoji="🎯",
        reply_markup=back()
    )
    await state.update_data(dice="🎯")
    await state.set_state(GameForm.dice)


@router.callback_query(F.data == "balance")
async def on_balance(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(
        text="Balance: $0",
        reply_markup=back()
    )


@router.callback_query(F.data == "back")
async def on_back(callback: types.CallbackQuery) -> None:
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.message.answer(
        text="Salom",
        reply_markup=inline_keyboard()
    )
