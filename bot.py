from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = ""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton("👍 Ha",callback_data="ha"),
            InlineKeyboardButton("👎 Yo'q",callback_data="yoq")
        ]
    ]

    markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Tanlang: ",
        reply_markup=markup
    )


async def button(update: Update, context:ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "ha":
        await query.edit_message_text("Siz HAni bosdingiz 👍")

    else:
        await query.edit_message_text("Siz YO'Qni bosdingiz 👎")


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start",start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()