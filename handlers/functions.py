from aiogram import Dispatcher
from football_teams.barcelona import check_updates_barcelona
from football_teams.chelsea import check_updates_chelsea
from football_teams.liverpool import check_updates_liverpool
from keyboards.keyboard import menu_kb, update_kb, barcelona_kb, liverpool_kb, chelsea_kb, tournaments_kb
from tournaments.epl import check_updates_epl
from tournaments.laliga import check_updates_laliga


async def cmd(message):
    # Функции для вызова участника беседы
    if message.text.lower() == "никита" or message.text.lower() == "власов":
        await message.answer('@erikhano')
    if message.text.lower() == "тимур" or message.text.lower() == "исмаилов":
        await message.answer('@bobz87')
    if message.text.lower() == "багир" or message.text.lower() == "бага" or message.text.lower() == "наджафов":
        await message.answer('@bagir_n10')
    if message.text.lower() == "андрей" or message.text.lower() == "андрюха" \
            or message.text.lower() == "кобрин" or message.text.lower() == "сукаед":
        await message.answer('@darindon000')
    if message.text.lower() == "габиб" or message.text.lower() == "мовсумов":
        await message.answer('@Gabon35')
    if message.text.lower() == "вова" or message.text.lower() == "вовчик" or message.text.lower() == "вован" \
            or message.text.lower() == "коротков":
        await message.answer('@valdemar_019')
    if message.text.lower() == "парни":
        await message.answer('@erikhano @bobz87 @bagir_n10 @darindon000 @Gabon35 @valdemar_019')
    if message.text.lower() == "азеры" or message.text.lower() == "хачи" or message.text.lower() == "хачапури":
        await message.answer('@bobz87 @bagir_n10 @Gabon35')

    # Функции меню
    if message.text.lower() == "menu" or message.text.lower() == "меню" or message.text.lower() == "назад":
        await message.answer('Меню:', reply_markup=menu_kb)
    if message.text.lower() == "чемпионаты":
        await message.answer('Информация о чемпионатах:', reply_markup=tournaments_kb)
    if message.text.lower() == "обновления":
        await message.answer('v1.0 - Добавление слов-команд\n\n'
                             'v1.1 - Изменения слов-команд (теперь бот реагирует на слова из'
                             'контекста сообщения и отмечает человека); меню с функциями;'
                             'функция с расписанием и прошедшими матчами Барселоны\n\n'
                             'v1.2 - Добавление новых слов-команд (/commands); '
                             'функция с расписанием и прошедшими матчами Ливерпуля и Челси\n'
                             'v1.2.1 - Небольшие улучшения роботоспособности\n'
                             'v1.2.2 - Изменения слов-команд (бот снова не реагирует на слова из контекста)\n\n'
                             'v1.3 - Информация по турнирам (Ла Лига, АПЛ); '
                             'Исправление ошибки (неправильный порядок отправки сообщений расписаний матчей)\n\n'
                             'v1.4 - У сообщений, связанных с распиcанием матчей и '
                             'турнирным положением в чемпионатах, изменён шрифт, а также все данные отправляются '
                             'одним сообщением',
                             reply_markup=update_kb)
    if "/commands" in message.text.lower():
        await message.answer('erikhano - Никита, Власов\n\n'
                             'bobz87 - Тимур, Исмаилов\n\n'
                             'bagir_n10 - Багир, Бага, Наджафов\n\n'
                             'darindon000 - Андрей, Андрюха, Кобрин, Сукаед\n\n'
                             'Gabon35 - Габиб, Мовсумов\n\n'
                             'valdemar_019 - Вова, Вован, Вовчик, Коротков\n\n'
                             'Общий сбор - Парни\n\n'
                             'Созвать bobz87, bagir_n10, Gabon35 - азеры, хачи, хачапури', reply_markup=update_kb)
    if message.text.lower() == 'барселона' or message.text.lower() == "барса":
        await message.answer('Информация о Барселоне:', reply_markup=barcelona_kb)
    if message.text.lower() == "ливерпуль" or message.text.lower() == "ливер":
        await message.answer('Информация о Ливерпуле:', reply_markup=liverpool_kb)
    if message.text.lower() == "челси" or message.text.lower() == "членси":
        await message.answer('Информация о Челси:', reply_markup=chelsea_kb)

    # Функции футбольных команд
    if message.text.lower() == "расписание барселоны":
        fresh_news = check_updates_barcelona()
        match_calendar = list(fresh_news.items())
        next_matches = ''
        for key, values in match_calendar[:-5][::-1]:
            next_matches += f"<i>{values['date']} - {values['tournament']}</i>\n" \
                    f"<b>{values['match']}</b>\n\n"
        await message.answer(next_matches, reply_markup=barcelona_kb, parse_mode='HTML')
    if message.text.lower() == "история игр барселоны":
        fresh_news = check_updates_barcelona()
        match_calendar = list(fresh_news.items())
        previous_matches = ''
        for key, values in match_calendar[-5:][::-1]:
            previous_matches += f"<i>{values['date']} - {values['tournament']}</i>\n" \
                            f"<b>{values['match']}</b>\n\n"
        await message.answer(previous_matches, reply_markup=barcelona_kb, parse_mode='HTML')

    if message.text.lower() == "расписание ливерпуля":
        fresh_news = check_updates_liverpool()
        match_calendar = list(fresh_news.items())
        next_matches = ''
        for key, values in match_calendar[:-5][::-1]:
            next_matches += f"<i>{values['date']} - {values['tournament']}</i>\n" \
                            f"<b>{values['match']}</b>\n\n"
        await message.answer(next_matches, reply_markup=liverpool_kb, parse_mode='HTML')
    if message.text.lower() == "история игр ливерпуля":
        fresh_news = check_updates_liverpool()
        match_calendar = list(fresh_news.items())
        previous_matches = ''
        for key, values in match_calendar[-5:][::-1]:
            previous_matches += f"<i>{values['date']} - {values['tournament']}</i>\n" \
                                f"<b>{values['match']}</b>\n\n"
        await message.answer(previous_matches, reply_markup=liverpool_kb, parse_mode='HTML')

    if message.text.lower() == "расписание челси":
        fresh_news = check_updates_chelsea()
        match_calendar = list(fresh_news.items())
        next_matches = ''
        for key, values in match_calendar[:-5][::-1]:
            next_matches += f"<i>{values['date']} - {values['tournament']}</i>\n" \
                            f"<b>{values['match']}</b>\n\n"
        await message.answer(next_matches, reply_markup=chelsea_kb, parse_mode='HTML')
    if message.text.lower() == "история игр челси":
        fresh_news = check_updates_chelsea()
        match_calendar = list(fresh_news.items())
        previous_matches = ''
        for key, values in match_calendar[-5:][::-1]:
            previous_matches += f"<i>{values['date']} - {values['tournament']}</i>\n" \
                                f"<b>{values['match']}</b>\n\n"
        await message.answer(previous_matches, reply_markup=chelsea_kb, parse_mode='HTML')

    # Функции турниров
    if message.text.lower() == "ла лига":
        fresh_news = check_updates_laliga()
        table = list(fresh_news.items())
        positions = ''
        for key, values in table[:20]:
            positions += f"<b>{values['place']}. {values['team']}</b> <i>(Очки: {values['points']}</i>)\n"
        await message.answer(positions, reply_markup=tournaments_kb, parse_mode='HTML')
    if message.text.lower() == "апл":
        fresh_news = check_updates_epl()
        table = list(fresh_news.items())
        positions = ''
        for key, values in table[:20]:
            positions += f"<b>{values['place']}. {values['team']}</b> <i>(Очки: {values['points']}</i>)\n"
        await message.answer(positions, reply_markup=tournaments_kb, parse_mode='HTML')


def register_handlers_cmd(dp: Dispatcher):
    dp.register_message_handler(cmd, content_types=['text'])
