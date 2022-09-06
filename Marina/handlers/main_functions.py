from aiogram import Dispatcher, types
from dsp import bot
from cfg import NIKITA, TIMUR, BAGIR, ANDREY, GABIB, VOVA, WOLFS, AZERS, MARINA, CHAT_ID, UPDATES_1, UPDATES_2, COMMANDS
from others.weather import weather_zheldor, weather_moscow
from keyboards.keyboard_menu import menu, clubs, barcelona, liverpool, chelsea, tournaments, other, patch_notes, delete
from keyboards.keyboard_name import nikita, timur, bagir, andrey, gabib, vova, wolfs, azers


async def cmd(message):
    # Функции для вызова участника беседы
    if [names in words for names in NIKITA if names in message.text.lower().split() for words in message.text.lower().split()]:
        await message.answer('Позвать Никиту?', reply_markup=nikita)
    if [names in words for names in TIMUR if names in message.text.lower().split() for words in message.text.lower().split()]:
        await message.answer('Позвать Тимура?', reply_markup=timur)
    if [names in words for names in BAGIR if names in message.text.lower().split() for words in message.text.lower().split()]:
        await message.answer('Позвать Багира?', reply_markup=bagir)
    if [names in words for names in ANDREY if names in message.text.lower().split() for words in message.text.lower().split()]:
        await message.answer('Позвать Андрея?', reply_markup=andrey)
    if [names in words for names in GABIB if names in message.text.lower().split() for words in message.text.lower().split()]:
        await message.answer('Позвать Габиба?', reply_markup=gabib)
    if [names in words for names in VOVA if names in message.text.lower().split() for words in message.text.lower().split()]:
        await message.answer('Позвать Вову?', reply_markup=vova)
    if [names in words for names in WOLFS if names in message.text.lower().split() for words in message.text.lower().split()]:
        await message.answer('Позвать парней?', reply_markup=wolfs)
    if [names in words for names in AZERS if names in message.text.lower().split() for words in message.text.lower().split()]:
        await message.answer('Позвать хачей?', reply_markup=azers)

    # Функции меню
    if [names in words for names in MARINA if names in message.text.lower().split() for words in message.text.lower().split()]:
        await message.answer('Меню', reply_markup=menu)
    if message.text.lower() == "/updates" or message.text.lower() == "обновления":
        await message.delete()
        await message.answer(UPDATES_1)
        await message.answer(UPDATES_2)

    # Дополнительные функции
    if message.text.lower() == "/commands" or message.text.lower() == 'команды':
        await message.delete()
        await message.answer(COMMANDS)
    if message.text.lower() == "/weather" or message.text.lower() == 'погода':
        await message.delete()
        zheldor = weather_zheldor()
        moscow = weather_moscow()
        temperature = f"В Железнодорожном <i>{zheldor['weather'].lower()}</i>\n" \
                      f"Температура <b>{zheldor['temperature_indication']}{zheldor['temperature']}</b>\n\n" \
                      f"В Москве <i>{moscow['weather'].lower()}</i>\n" \
                      f"Температура <b>{moscow['temperature_indication']}{moscow['temperature']}</b>\n\n"
        await bot.send_message(message.chat.id, temperature)


async def btn(call: types.CallbackQuery):
    await call.message.delete()
    if call.data == 'clubs_btn':
        await bot.send_message(call.message.chat.id, 'Клубы', reply_markup=clubs)
    if call.data == 'other_btn':
        await bot.send_message(call.message.chat.id, 'Прочее', reply_markup=other)
    if call.data == 'commands_btn':
        await bot.send_message(call.message.chat.id, COMMANDS, reply_markup=other)
    if call.data == 'weather_btn':
        zheldor = weather_zheldor()
        moscow = weather_moscow()
        temperature = f"В Железнодорожном <i>{zheldor['weather'].lower()}</i>\n" \
                      f"Температура <b>{zheldor['temperature_indication']}{zheldor['temperature']}</b>\n\n" \
                      f"В Москве <i>{moscow['weather'].lower()}</i>\n" \
                      f"Температура <b>{moscow['temperature_indication']}{moscow['temperature']}</b>\n\n"
        await  bot.send_message(call.message.chat.id, temperature, reply_markup=other)
    if call.data == 'patch_notes_btn':
        await bot.send_message(call.message.chat.id, 'Версии обновлений', reply_markup=patch_notes)
    if call.data == 'patch_notes_1_btn':
        await bot.send_message(call.message.chat.id, UPDATES_1, reply_markup=patch_notes)
    if call.data == 'patch_notes_2_btn':
        await bot.send_message(call.message.chat.id, UPDATES_2, reply_markup=patch_notes)
    if call.data == 'back_btn':
        await bot.send_message(call.message.chat.id, 'Меню', reply_markup=menu)
    if call.data == 'back_clubs_btn':
        await bot.send_message(call.message.chat.id, 'Меню', reply_markup=clubs)
    if call.data == 'back_patch_notes_btn':
        await bot.send_message(call.message.chat.id, 'Прочее', reply_markup=other)
    if call.data == 'back_champ_btn':
        await bot.send_message(call.message.chat.id, 'Информация о чемпионатах', reply_markup=tournaments)
    if call.data == 'back_leagues_btn':
        await bot.send_message(call.message.chat.id, 'Информация о чемпионатах', reply_markup=tournaments)
    if call.data == 'yes_nikita_btn':
        await bot.send_message(call.message.chat.id, '@erikhano')
    if call.data == 'yes_timur_btn':
        await bot.send_message(call.message.chat.id, '@bobz87')
    if call.data == 'yes_bagir_btn':
        await bot.send_message(call.message.chat.id, '@bagir_n10')
    if call.data == 'yes_andrey_btn':
        await bot.send_message(call.message.chat.id, '@darindon00')
    if call.data == 'yes_gabib_btn':
        await bot.send_message(call.message.chat.id, '@Gabon35')
    if call.data == 'yes_vova_btn':
        await bot.send_message(call.message.chat.id, '@valdemar_019')
    if call.data == 'yes_wolfs_btn':
        await bot.send_message(call.message.chat.id,
                               '@erikhano @bobz87 @bagir_n10 @darindon00 @Gabon35 @valdemar_019')
    if call.data == 'yes_azers_btn':
        await bot.send_message(call.message.chat.id, '@bobz87 @bagir_n10 @Gabon35')
    if call.data == 'no_nikita_btn' or call.data == 'no_timur_btn' or \
            call.data == 'no_bagir_btn' or call.data == 'no_andrey_btn' or \
            call.data == 'no_gabib_btn' or call.data == 'no_vova_btn' or \
            call.data == 'no_wolfs_btn' or call.data == 'no_azers_btn':
        pass


def register_handlers_cmd(dp: Dispatcher):
    dp.register_callback_query_handler(btn, text_contains='btn')
    dp.register_message_handler(cmd, content_types=['text'])
