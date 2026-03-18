import asyncio
from aiogram import Bot , Dispatcher,types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup , KeyboardButton , InlineKeyboardButton , InlineKeyboardMarkup

TOKEN = "8574401368:AAFIimD9AzRgEZGwWTjVXz9ELPB7jckn4aE"
bot = Bot(token = TOKEN)
db = Dispatcher()

kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Kurslar")]],
    
    resize_keyboard=True
)

kb2 = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Bosh menyu🏠"),KeyboardButton(text="Dasturlash"),KeyboardButton(text="Kompyuter savodxonligi"),KeyboardButton(text="Ingliz tili")]],
    resize_keyboard=True
)

murojat=InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Qabulga yozilish", callback_data="write_to_admission")]]
)

@db.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Botga hush kelibsiz!",reply_markup=kb)

@db.message()
async def msg(message: types.Message):
    if message.text == "Kurslar":
        await message.answer("Kurslarimiz:",reply_markup=kb2)
    elif message.text == "Bosh menyu🏠":
        await message.answer("Asosiy" , reply_markup=kb)
    elif message.text == "Dasturlash":
        await message.answer("📌 Kurs davomiyligi: 2–12 oy\n💰 Narx: oyiga 600 000so‘m\n💻 O‘rgatiladigan tillar va yo‘nalishlar:\n✔ HTML, CSS, JavaScript – Frontend web dasturlash\n✔ Python – Backend va Data Science asoslari\n✔ React, Django, SQL, Git\n✔ Flutter / Mobile ilovalar",reply_markup=murojat)
    elif message.text == "Kompyuter savodxonligi":
        await message.answer("📌 Kurs davomiyligi: 1–3 oy\n💰 Narx: 400 000so‘m\n💡 Nimalarni o‘rganasiz:\n- Windows va MS Office (Word, Excel, PowerPoint)\n- Internet va elektron pochta ishlatish\n- Fayllarni boshqarish va xavfsizlik asoslari\n- Oddiy grafik va prezentatsiyalar tayyorlash",reply_markup=murojat)
    elif message.text == "Ingliz tili":
        await message.answer("📌 Kurs davomiyligi: 1yil oy\n💰 Narxi: 500 000so‘m\n💡 Nimalarni o‘rganasiz:\n- Speaking, Listening, Reading va Writing ko‘nikmalari\n- Grammatikani amaliy mashqlar orqali o‘rganish\n- So‘z boyligini oshirish\n- Testlar va real muloqot mashqlari",reply_markup=murojat)
            
@db.message(Command("help"))
async def help_handler(message: types.Message):
    await message.answer("Nima yordam kerak?")

async def main():
    await db.start_polling(bot)
if __name__ == "__main__":
    print("Bot ishga tushdi")
asyncio.run(main())
