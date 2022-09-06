from aiogram.utils import executor
from dsp import dp

if __name__ == '__main__':
    from handlers import main_functions, clubs_functions, tournaments_functions

    main_functions.register_handlers_cmd(dp)
    clubs_functions.register_handlers_clubs(dp)
    tournaments_functions.register_handlers_champ(dp)

    executor.start_polling(dp, skip_updates=True)
