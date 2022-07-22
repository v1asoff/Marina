from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_button = KeyboardButton('Меню')
button_barcelona = KeyboardButton('Барселона')
button_liverpool = KeyboardButton('Ливерпуль')
button_chelsea = KeyboardButton('Челси')
button_tournaments = KeyboardButton('Чемпионаты')
button_patch_notes = KeyboardButton('Обновления')
button_previous = KeyboardButton('Назад')

button_barcelona_next = KeyboardButton('Расписание Барселоны')
button_barcelona_previous = KeyboardButton('История игр Барселоны')
button_liverpool_next = KeyboardButton('Расписание Ливерпуля')
button_liverpool_previous = KeyboardButton('История игр Ливерпуля')
button_chelsea_next = KeyboardButton('Расписание Челси')
button_chelsea_previous = KeyboardButton('История игр Челси')
button_laliga = KeyboardButton('Ла Лига')
button_epl = KeyboardButton('АПЛ')

menu_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
tournaments_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
update_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
barcelona_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
liverpool_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
chelsea_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)


menu_kb.row(button_barcelona, button_liverpool, button_chelsea).add(button_tournaments).add(button_patch_notes)
tournaments_kb.row(button_laliga, button_epl).add(button_previous)
update_kb.add(button_previous)
barcelona_kb.row(button_barcelona_next, button_barcelona_previous).add(button_previous)
liverpool_kb.row(button_liverpool_next, button_liverpool_previous).add(button_previous)
chelsea_kb.row(button_chelsea_next, button_chelsea_previous).add(button_previous)

