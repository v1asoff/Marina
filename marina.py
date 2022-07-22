from aiogram.utils import executor
from dsp import dp
from handlers import functions

functions.register_handlers_cmd(dp)

executor.start_polling(dp, skip_updates=True)
