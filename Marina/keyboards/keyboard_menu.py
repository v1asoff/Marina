from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(row_width=3)
clubs = InlineKeyboardMarkup(row_width=2)
barcelona = InlineKeyboardMarkup(row_width=2)
liverpool = InlineKeyboardMarkup(row_width=2)
chelsea = InlineKeyboardMarkup(row_width=2)
tournaments = InlineKeyboardMarkup(row_width=2)
leagues = InlineKeyboardMarkup(row_width=3)
world_cup = InlineKeyboardMarkup(row_width=2)
other = InlineKeyboardMarkup(row_width=3)
patch_notes = InlineKeyboardMarkup(row_width=3)
delete = InlineKeyboardMarkup(row_width=1)

# Клубы
clubs_btn = InlineKeyboardButton(text='⚽ Клубы', callback_data='clubs_btn')
back_clubs_btn = InlineKeyboardButton(text='🔙 Назад', callback_data='back_clubs_btn')
# Барслеона
barcelona_btn = InlineKeyboardButton(text='🇪🇸 Барселона', callback_data='Barcelona')
barcelona_next_btn = InlineKeyboardButton(text='📅 Расписание', callback_data='tableBarcelona')
barcelona_previous_btn = InlineKeyboardButton(text='✅ История игр', callback_data='historyBarcelona')
# Ливерпуль
liverpool_btn = InlineKeyboardButton(text='🏴󠁧󠁢󠁥󠁮󠁧󠁿 Ливерпуль', callback_data='Liverpool')
liverpool_next_btn = InlineKeyboardButton(text='📅 Расписание', callback_data='tableLiverpool')
liverpool_previous_btn = InlineKeyboardButton(text='✅ История игр', callback_data='historyLiverpool')
# Челси
chelsea_btn = InlineKeyboardButton(text='🏴󠁧󠁢󠁥󠁮󠁧󠁿 Челси', callback_data='Chelsea')
chelsea_next_btn = InlineKeyboardButton(text='📅 Расписание', callback_data='tableChelsea')
chelsea_previous_btn = InlineKeyboardButton(text='✅ История игр', callback_data='historyChelsea')

# Турниры
tournaments_btn = InlineKeyboardButton(text='🏆 Турниры', callback_data='tournaments_champ')
back_tournaments_btn = InlineKeyboardButton(text='🔙 Назад', callback_data='back_tournaments_btn')
# Лиги
leagues_btn = InlineKeyboardButton(text='🏅 Лиги', callback_data='league_champ')
laliga_btn = InlineKeyboardButton(text='🇪🇸 Ла Лига', callback_data='LaLiga_champ')
epl_btn = InlineKeyboardButton(text='🏴󠁧󠁢󠁥󠁮󠁧󠁿 АПЛ', callback_data='EPL_champ')
ligue1_btn = InlineKeyboardButton(text='🇫🇷󠁧󠁢󠁥󠁮󠁧󠁿 Лига 1', callback_data='Ligue1_champ')
serieA_btn = InlineKeyboardButton(text='🇮🇹󠁧󠁢󠁥󠁮󠁧󠁿 Серия А', callback_data='SerieA_champ')
bundesliga_btn = InlineKeyboardButton(text='🇩🇪󠁧󠁢󠁥󠁮󠁧󠁿 Бундеслига', callback_data='Bundesliga_champ')
back_leagues_btn = InlineKeyboardButton(text='🔙 Назад', callback_data='back_leagues_btn')
# Чемпионат Мира
world_cup_btn = InlineKeyboardButton(text='🌍 Чемпионат Мира', callback_data='world_cup')
groups_wc_btn = InlineKeyboardButton(text='ℹ Группы', callback_data='groups_world_cup')
table_wc_btn = InlineKeyboardButton(text='📅 Расписание', callback_data='table_world_cup')
stats_wc_btn = InlineKeyboardButton(text='⚽ Бомбардиры', callback_data='stats_world_cup')

# Другое
other_btn = InlineKeyboardButton(text='⚙ Прочее', callback_data='other_btn')
# Погода
weather_btn = InlineKeyboardButton(text='⛅ Погода', callback_data='weather_btn')
# Команды
commands_btn = InlineKeyboardButton(text='ℹ Команды', callback_data='commands_btn')
# Обновления
patch_notes_btn = InlineKeyboardButton(text='🔄 Обновления', callback_data='patch_notes_btn')
patch_notes_1_btn = InlineKeyboardButton(text='🔄 v1.0 - v1.4', callback_data='patch_notes_1_btn')
patch_notes_2_btn = InlineKeyboardButton(text='🔄 v1.5 - v1.6', callback_data='patch_notes_2_btn')
back_patch_notes_btn = InlineKeyboardButton(text='🔙 Назад', callback_data='back_patch_notes_btn')

# Прочее
back_btn = InlineKeyboardButton(text='🔙 Назад', callback_data='back_btn')
delete_btn = InlineKeyboardButton(text='Да, удалить', callback_data='delete_btn')

menu.row(clubs_btn, tournaments_btn).add(other_btn)
clubs.add(barcelona_btn).row(liverpool_btn, chelsea_btn).add(back_btn)
barcelona.row(barcelona_next_btn, barcelona_previous_btn).add(back_clubs_btn)
liverpool.row(liverpool_next_btn, liverpool_previous_btn).add(back_clubs_btn)
chelsea.row(chelsea_next_btn, chelsea_previous_btn).add(back_clubs_btn)
tournaments.row(leagues_btn, world_cup_btn).add(back_btn)
leagues.row(laliga_btn, epl_btn, ligue1_btn).row(serieA_btn, bundesliga_btn).add(back_leagues_btn)
world_cup.row(groups_wc_btn, table_wc_btn).add(stats_wc_btn).add(back_leagues_btn)
other.add(weather_btn).row(commands_btn, patch_notes_btn).add(back_btn)
patch_notes.row(patch_notes_1_btn, patch_notes_2_btn).add(back_patch_notes_btn)
delete.row(delete_btn)
