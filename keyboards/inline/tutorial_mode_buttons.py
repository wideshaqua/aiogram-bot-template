from random import randint

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from data.text_data import buttons

return_button = InlineKeyboardButton(text=buttons['rus'])

action_callback = CallbackData('action', 'value', 'stage_id', 'message_id')


def make_callback_data(value, stage_id='-', message_id='-') -> CallbackData:
    return action_callback.new(value, stage_id, message_id)


def make_inline_keyboard(next_stage: str, next_message: str) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=2)
    return_button = InlineKeyboardButton(text=buttons['rus']
    ['inline_keyboard']['tutorial_rand_return_buttons'][randint(0,1)],
                                         callback_data=make_callback_data('return'))
    forward_button = InlineKeyboardButton(text=buttons['rus']
    ['inline_keyboard']['tutorial_rand_forward_buttons'][randint(0,1)],
                                          callback_data=make_callback_data('forward', next_stage, next_message))
    skip_button = InlineKeyboardButton(text=buttons['rus']
    ['inline_keyboard']['tutorial_rand_skip_buttons'][randint(0,1)],
                                       callback_data=make_callback_data('skip', next_stage))

    markup.insert(return_button)
    markup.insert(forward_button)
    markup.insert(skip_button)

    return markup



