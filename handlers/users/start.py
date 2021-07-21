from aiogram.dispatcher.filters import CommandStart, Regexp, Text
from aiogram import types

from loader import dp
from keyboards.inline import start_action_buttons as mrkp

from data.text_data import messages

msg_txt = messages['rus']


@dp.message_handler(CommandStart())
async def start(message: types.Message):
    await message.delete()
    await message.answer(text=msg_txt['start'], parse_mode='Markdown',
                         reply_markup=mrkp.start_action_markup)


@dp.callback_query_handler(Regexp('return'))
async def start(call: types.CallbackQuery):
    await call.answer()
    await call.message.edit_text(text=msg_txt['start'], parse_mode='Markdown',
                         reply_markup=mrkp.start_action_markup)


@dp.callback_query_handler(Text('manual'))
async def start_manual_mode(call: types.CallbackQuery):
    await call.answer()
    await call.message.edit_text(text=msg_txt['manual_start'], parse_mode='Markdown',
                                 reply_markup=mrkp.manual_mode_markup)


@dp.callback_query_handler(Text('tutorial'))
async def start_tutorial_mode(call: types.CallbackQuery):
    await call.answer()
    await call.message.edit_text(text=msg_txt['tutorial_start'], parse_mode='Markdown',
                                 reply_markup=mrkp.tutorial_mode_markup)

