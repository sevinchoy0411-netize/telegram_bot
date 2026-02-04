# from telegram import Update
# from telegram.ext import (
#     ApplicationBuilder,
#     CommandHandler,
#     MessageHandler,
#     ContextTypes,
#     filters
# )

# TOKEN = ""

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Salom!\nIsmingizni kiriting: ")

# async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     name = update.message.text
#     await update.message.reply_text(f"Salom, {name}!")

# app = ApplicationBuilder().token(TOKEN).build()

# app.add_handler(CommandHandler("start",start))
# app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_name))

# print("Bot ishga tushdi...")
# app.run_polling()