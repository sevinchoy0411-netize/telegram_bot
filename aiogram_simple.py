import asyncio
from aiogram import Bot , Dispatcher,types
from aiogram.filters import Command

TOKEN = ""
bot = Bot(token = TOKEN)
db = Dispatcher()

@db.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Botga hush kelibsiz!")

@db.message(Command("help"))
async def help_handler(message: types.Message):
    await message.answer("Nima yordam kerak?")

async def main():
    await db.start_polling(bot)

asyncio.run(main())