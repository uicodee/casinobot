from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def reply_keyboard() -> types.ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="🎯 Darts"),
        types.KeyboardButton(text="🏀 Basketball"),
    )
    builder.row(
        types.KeyboardButton(text="⚽️ Football"),
        types.KeyboardButton(text="🎲 Dice")
    )
    builder.row(
        types.KeyboardButton(text="🎳 Bowling")
    )
    return builder.as_markup(resize_keyboard=True)


def inline_keyboard() -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(text="🎯 Darts", callback_data="darts"),
        types.InlineKeyboardButton(text="🏀 Basketball", callback_data="basketball"),
    )
    builder.row(
        types.InlineKeyboardButton(text="⚽️ Football", callback_data="football"),
        types.InlineKeyboardButton(text="🎲 Dice", callback_data="dice")
    )
    builder.row(
        types.InlineKeyboardButton(text="🎳 Bowling", callback_data="bowling")
    )
    builder.row(
        types.InlineKeyboardButton(text="💰 Balance", callback_data="balance")
    )
    return builder.as_markup()


def back() -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(text="⬅️ Back", callback_data="back")
    )
    return builder.as_markup()
