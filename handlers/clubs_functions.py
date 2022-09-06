from aiogram import Dispatcher, types
from dsp import bot
from football_teams.barcelona import barcelona_calendar
from football_teams.liverpool import liverpool_stats
from football_teams.chelsea import chelsea_stats
from keyboards.keyboard_menu import barcelona, liverpool, chelsea


async def barcelona_spain(call: types.CallbackQuery):
    await call.message.delete()
    if call.data == 'Barcelona':
        await bot.send_message(call.message.chat.id, 'Информация о Барселоне', reply_markup=barcelona)
    if call.data == 'tableBarcelona':
        next_matches = ''
        for key, values in list(barcelona_calendar().items())[:-5][::-1]:
            next_matches += f"<i>{values['date']} - {values['tournament']}</i>\n" \
                            f"<b>{values['match']}</b>\n\n"
        await bot.send_message(call.message.chat.id, next_matches, reply_markup=barcelona)
    if call.data == "historyBarcelona":
        previous_matches = ''
        for key, values in list(barcelona_calendar().items())[-5:][::-1]:
            previous_matches += f"<i>{values['date']} - {values['tournament']}</i>\n" \
                                f"<b>{values['match']}</b>\n\n"
        await bot.send_message(call.message.chat.id, previous_matches, reply_markup=barcelona)


async def liverpool_england(call: types.CallbackQuery):
    await call.message.delete()
    if call.data == 'Liverpool':
        await bot.send_message(call.message.chat.id, 'Информация о Ливерпуле', reply_markup=liverpool)
    if call.data == 'tableLiverpool':
        next_matches = ''
        for key, values in list(liverpool_stats().items())[:-5][::-1]:
            next_matches += f"<i>{values['date']} - {values['tournament']}</i>\n" \
                            f"<b>{values['match']}</b>\n\n"
        await bot.send_message(call.message.chat.id, next_matches, reply_markup=liverpool)
    if call.data == "historyLiverpool":
        previous_matches = ''
        for key, values in list(liverpool_stats().items())[-5:][::-1]:
            previous_matches += f"<i>{values['date']} - {values['tournament']}</i>\n" \
                                f"<b>{values['match']}</b>\n\n"
        await bot.send_message(call.message.chat.id, previous_matches, reply_markup=liverpool)

async def chelsea_england(call: types.CallbackQuery):
    await call.message.delete()
    if call.data == 'Chelsea':
        await bot.send_message(call.message.chat.id, 'Информация о Челси', reply_markup=chelsea)
    if call.data == 'tableChelsea':
        next_matches = ''
        for key, values in list(chelsea_stats().items())[:-5][::-1]:
            next_matches += f"<i>{values['date']} - {values['tournament']}</i>\n" \
                            f"<b>{values['match']}</b>\n\n"
        await bot.send_message(call.message.chat.id, next_matches, reply_markup=chelsea)
    if call.data == "historyChelsea":
        previous_matches = ''
        for key, values in list(chelsea_stats().items())[-5:][::-1]:
            previous_matches += f"<i>{values['date']} - {values['tournament']}</i>\n" \
                                f"<b>{values['match']}</b>\n\n"
        await bot.send_message(call.message.chat.id, previous_matches, reply_markup=chelsea)


def register_handlers_clubs(dp: Dispatcher):
    dp.register_callback_query_handler(barcelona_spain, text_contains='Barcelona')
    dp.register_callback_query_handler(liverpool_england, text_contains='Liverpool')
    dp.register_callback_query_handler(chelsea_england, text_contains='Chelsea')

