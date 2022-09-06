from aiogram import Dispatcher, types
from dsp import bot
from tournaments.laliga import laliga
from tournaments.epl import epl
from tournaments.ligue1 import ligue1
from tournaments.serieA import serieA
from tournaments.bundesliga import bundesliga
from tournaments.world_cup import world_cup_A, world_cup_B, world_cup_C, world_cup_D, world_cup_E, \
    world_cup_F, world_cup_G, world_cup_H, world_cup_stats, world_cup_timetable1, world_cup_timetable2, \
    world_cup_timetable3, world_cup_timetable4, world_cup_timetable_quarterfinal, \
    world_cup_timetable_semifinals, world_cup_timetable_final
from keyboards.keyboard_menu import tournaments, leagues, world_cup


async def champ(call: types.CallbackQuery):
    await call.message.delete()
    if call.data == 'tournaments_champ':
        await bot.send_message(call.message.chat.id, 'Информация о турнирах', reply_markup=tournaments)
    if call.data == 'league_champ':
        await bot.send_message(call.message.chat.id, 'Информация о лигах', reply_markup=leagues)
    if call.data == 'LaLiga_champ':
        table = laliga().items()
        positions = ''
        for key, values in table:
            positions += f"\n<b>{values['place']}. {values['team']}</b> <i>(И - {values['games']}; О - {values['points']}</i>)"
        await bot.send_message(call.message.chat.id, positions, reply_markup=leagues)
    if call.data == 'EPL_champ':
        table = epl().items()
        positions = ''
        for key, values in table:
            positions += f"\n<b>{values['place']}. {values['team']}</b> <i>(И - {values['games']}; О - {values['points']}</i>)"
        await bot.send_message(call.message.chat.id, positions, reply_markup=leagues)
    if call.data == 'Ligue1_champ':
        table = ligue1().items()
        positions = ''
        for key, values in table:
            positions += f"\n<b>{values['place']}. {values['team']}</b> <i>(И - {values['games']}; О - {values['points']}</i>)"
        await bot.send_message(call.message.chat.id, positions, reply_markup=leagues)
    if call.data == 'SerieA_champ':
        table = serieA().items()
        positions = ''
        for key, values in table:
            positions += f"\n<b>{values['place']}. {values['team']}</b> <i>(И - {values['games']}; О - {values['points']}</i>)"
        await bot.send_message(call.message.chat.id, positions, reply_markup=leagues)
    if call.data == 'Bundesliga_champ':
        table = bundesliga().items()
        positions = ''
        for key, values in table:
            positions += f"\n<b>{values['place']}. {values['team']}</b> <i>(И - {values['games']}; О - {values['points']}</i>)"
        await bot.send_message(call.message.chat.id, positions, reply_markup=leagues)


async def cup(call: types.CallbackQuery):
    await call.message.delete()
    if call.data == 'world_cup':
        await bot.send_message(call.message.chat.id, 'Информация о Чемпионате Мира', reply_markup=world_cup)
    if call.data == 'groups_world_cup':
        table = world_cup_A().items()
        positions = 'Группа A:'
        for key, values in table:
            positions += f"\n<b>{values['place']}. {values['team']}</b> <i>(И - {values['games']}; О - {values['points']}</i>)"
        table = world_cup_B().items()
        positions += '\n\nГруппа B:'
        for key, values in table:
            positions += f"\n<b>{values['place']}. {values['team']}</b> <i>(И - {values['games']}; О - {values['points']}</i>)"
        table = world_cup_C().items()
        positions += '\n\nГруппа C:'
        for key, values in table:
            positions += f"\n<b>{values['place']}. {values['team']}</b> <i>(И - {values['games']}; О - {values['points']}</i>)"
        table = world_cup_D().items()
        positions += '\n\nГруппа D:'
        for key, values in table:
            positions += f"\n<b>{values['place']}. {values['team']}</b> <i>(И - {values['games']}; О - {values['points']}</i>)"
        table = world_cup_E().items()
        positions += '\n\nГруппа E:'
        for key, values in table:
            positions += f"\n<b>{values['place']}. {values['team']}</b> <i>(И - {values['games']}; О - {values['points']}</i>)"
        table = world_cup_F().items()
        positions += '\n\nГруппа F:'
        for key, values in table:
            positions += f"\n<b>{values['place']}. {values['team']}</b> <i>(И - {values['games']}; О - {values['points']}</i>)"
        table = world_cup_G().items()
        positions += '\n\nГруппа G:'
        for key, values in table:
            positions += f"\n<b>{values['place']}. {values['team']}</b> <i>(И - {values['games']}; О - {values['points']}</i>)"
        table = world_cup_H().items()
        positions += '\n\nГруппа H:'
        for key, values in table:
            positions += f"\n<b>{values['place']}. {values['team']}</b> <i>(И - {values['games']}; О - {values['points']}</i>)"
        await bot.send_message(call.message.chat.id, positions, reply_markup=world_cup)
    if call.data == 'table_world_cup':
        table = world_cup_stats().items()
        positions = ''
        for key, values in table:
            positions += f"\n{key}. {values['name']} - <b>{values['goals']}</b> Г"
        await bot.send_message(call.message.chat.id, '<b>Финал. Аргентина - Катар (100:0)</b>', reply_markup=world_cup)
    if call.data == 'stats_world_cup':
        #     table = world_cup_stats().items()
        #     positions = ''
        #     for key, values in table:
        #         positions += f"\n{key}. {values['name']} - <b>{values['goals']}</b> Г"
        await bot.send_message(call.message.chat.id, '<b>Месси - 100 голов</b>', reply_markup=world_cup)


def register_handlers_champ(dp: Dispatcher):
    dp.register_callback_query_handler(champ, text_contains='_champ')
    dp.register_callback_query_handler(cup, text_contains='_cup')
