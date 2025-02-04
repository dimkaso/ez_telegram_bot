import asyncio
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

# Ваш токен бота
TOKEN = "Bot token"

# ID канала (например, @channelusername или -1001234567890)
CHANNEL_ID = "@Your Telegram channel in which you want to use the bot"  # Замените на ID вашего канала

# Асинхронная функция для отправки сообщения с кнопкой
async def send_message_with_button():
    bot = Bot(token=TOKEN)

    # Текст сообщения
    message = "🌟 *Гороскоп на день* 🌟\n\n" \
              "Узнайте свой гороскоп на сегодня, нажав на кнопку ниже!"

    # Создаем кнопку с ссылкой на бота
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Перейти к боту", url="link to bot")]
    ])

    # Отправляем сообщение с кнопкой
    await bot.send_message(
        chat_id=CHANNEL_ID,
        text=message,
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

# Запуск асинхронной функции
if __name__ == "__main__":
    asyncio.run(send_message_with_button())
