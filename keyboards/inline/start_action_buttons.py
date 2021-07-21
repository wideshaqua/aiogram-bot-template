from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.text_data import buttons

btn_txt = buttons['rus']

start_action_markup = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=txt, callback_data=callback)] for txt, callback in zip(
        btn_txt['inline_keyboard']['start_action'],
        ('manual', 'tutorial')
    )
])

manual_mode_markup = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=txt, callback_data=callback)] for txt, callback in zip(
        btn_txt['inline_keyboard']['start_change_mode'],
        ('return', 'manual_mode')
    )
])

tutorial_mode_markup = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=txt, callback_data=callback)] for txt, callback in zip(
        btn_txt['inline_keyboard']['start_change_mode'],
        ('return', 'tutorial_mode')
    )
])