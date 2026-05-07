import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, MenuButtonWebApp
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Токен берётся из переменной окружения Railway
TOKEN = os.environ.get("TOKEN")

# Ссылка на твою игру (замени на свою ссылку с GitHub Pages)
WEBAPP_URL = os.environ.get("WEBAPP_URL", "https://ВАШ_САЙТ/Apple_2048.html")

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
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.set_chat_menu_button(
        chat_id=update.effective_chat.id,
        menu_button=MenuButtonWebApp(
            text="🎮 Играть",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    )

    await update.message.reply_text(
        text=WELCOME_TEXT,
        parse_mode="HTML",
        reply_markup=reply_markup
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен!")
    app.run_polling()
