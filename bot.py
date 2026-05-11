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

HELP_TEXT = (
    "❓ <b>Как играть?</b>\n\n"
    "Это игра в стиле 2048: соединяй одинаковые плитки и открывай новые уровни. "
    "Только вместо цифр здесь — iPhone! Начни с iPhone 2G и дойди до iPhone 17 Pro. "
    "Объединяй плитки и прокачивай свою коллекцию iPhone!\n\n"
    "📱 <b>На телефоне:</b>\n"
    "Используй свайпы, чтобы передвигать плитки.\n\n"
    "💻 <b>На компьютере:</b>\n"
    "Используй стрелки на клавиатуре, чтобы передвигать плитки."
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bot_username = (await context.bot.get_me()).username
    keyboard = [[
        InlineKeyboardButton(
            text="🎮 Запустить игру",
            url=f"https://t.me/{bot_username}?startapp=game"
        )
    ]]
    await update.message.reply_text(
        text=WELCOME_TEXT,
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        text=HELP_TEXT,
        parse_mode="HTML"
    )

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    print("Бот запущен!")
    app.run_polling()
