from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder , CallbackQueryHandler , CommandHandler , ContextTypes

TOKEN = ""

savol = "Telegram bot yaratishning nechta turi bor?"

variant = [
    (1,"A"),
    (2,"B"),
    (3,"C"),
    (4,"D")
]

javob = "B"

async def start(update: Update,context: ContextTypes.DEFAULT_TYPE):
    royhat = []

    for matn , qiymat in variant:
        royhat.append(
            [InlineKeyboardButton(matn , callback_data = qiymat)]
        )
        reply_markup = InlineKeyboardMarkup(royhat)
    await update.message.reply_text(
            savol,
            reply_markup=reply_markup
    )

async def button(update: Update,context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == javob:
        await query.edit_message_text("Siz to'g'ri javobni topdingiz!")
    else:
        await query.edit_message_text("Siz to'g'ri javobni topa olmadingiz")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start",start))
    app.add_handler(CallbackQueryHandler(button))
    print("bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
