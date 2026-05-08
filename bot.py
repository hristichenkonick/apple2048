import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("TOKEN")
WEBAPP_URL = os.environ.get("WEBAPP_URL", "https://example.com")

WELCOME_TEXT = (
    "🍎 <b>Добро пожаловать в игру Apple 2048!</b>\n\n"
    "Соединяйте плитки и доберитесь до самого последнего iPhone!\n\n"
    "👇 Запускайте игру как можно скорее!"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[
        InlineKeyboardButton(
            text="🎮 Запустить игру",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    ]]
    await update.message.reply_text(
        text=WELCOME_TEXT,
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен!")
    app.run_polling()
