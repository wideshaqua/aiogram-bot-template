from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

from data.text_data import buttons

text = buttons['rus']['keyboard']

main_menu_markup = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(button_text)] for button_text in text['main_menu_buttons']
])
