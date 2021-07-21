import asyncio

from aiogram import types
from aiogram.dispatcher.filters import Regexp, Text

from loader import dp

from data.text_data import messages, stages
from keyboards.inline import tutorial_mode_buttons as tm_btn
from keyboards.inline.tutorial_mode_buttons import make_inline_keyboard


msg_txt = messages['rus']
#TODO запихнуть два хендлера ниже в один
#TODO починить ошибку с ключом словаря, когда id переполняется, и перенаправлять юзера в начало на конечном сообщении

@dp.callback_query_handler(Text('tutorial_mode'))
async def tutorial_mode_start(call: types.CallbackQuery):
    await call.answer()
    await call.message.edit_text(text=msg_txt['tutorial_contents_0'], parse_mode='Markdown')
    await types.ChatActions.typing()
    await asyncio.sleep(5)
    await call.message.answer(text=msg_txt['tutorial_contents_1'], parse_mode='Markdown',
                              reply_markup=make_inline_keyboard('contents', '2'))


@dp.callback_query_handler(tm_btn.action_callback.filter(value='forward'))
async def switch_message(call: types.CallbackQuery, **kwargs):
    await call.answer()
    await call.message.edit_reply_markup(None)
    data = call.data.split(':')

    try:
        await call.message.answer(msg_txt['tutorial_'+str(data[2])+'_'+str(data[3])],
                                     parse_mode='Markdown',
                                  reply_markup=make_inline_keyboard(str(data[2]), str(int(data[3])+1)))
    except KeyError:
        await call.message.edit_text(text=msg_txt['tutorial_'+str(stages(stages.index(data[2]+1)))+'_0'],
                                     parse_mode='Markdown')
        await types.ChatActions.typing()
        await asyncio.sleep(5)
        await call.message.answer(msg_txt['tutorial_'+str(data[2])+'_1'],
                                  parse_mode='Markdown',
                                  reply_markup=make_inline_keyboard(str(stages(stages.index(data[2]+1))), '2'))


