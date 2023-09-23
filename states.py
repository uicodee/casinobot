from aiogram.fsm.state import StatesGroup, State


class GameForm(StatesGroup):

    dice = State()
