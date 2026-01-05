import logging
import os
import random

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is not set")
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

IDEAS = [
    "Где лучше размещать розетки на кухне в новостройке",
    "Сколько автоматов нужно в квартире 2-комнатной",
    "Типовые ошибки при замене электропроводки",
    "Почему нельзя соединять медь и алюминий напрямую",
    "Как правильно сделать электрику под кондиционер",
    "Нужно ли УЗО в квартире и где его ставить",
    "Тренды электромонтажа в квартирах 2025 года",
    "Скрытая или открытая проводка — что выбрать",
    "Как электрик проверяет квартиру перед сдачей",
    "Чек-лист электрики перед чистовой отделкой"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! ⚡\n"
        "Я бот-планировщик идей для канала про электромонтаж.\n\n"
        "Команды:\n"
        "/idea — получить идею поста"
    )

async def idea(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💡 Идея поста:\n" + random.choice(IDEAS))

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError("BOT_TOKEN not set")

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("idea", idea))
    app.run_polling()

if __name__ == "__main__":
    main()
