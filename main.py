# pip install python-telegram-bot==20.*
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "BURAYA_BOT_TOKENINI_YAZ"  # örnek: "123456789:ABCdefGHI..."

# /start komutu
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Merhaba! Ben senin Telegram botunum 🤖")

# Herhangi bir mesaj geldiğinde
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"Gönderdin: {text}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

print("Bot çalışıyor...")
app.run_polling()
