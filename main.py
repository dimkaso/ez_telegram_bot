import asyncio
from telegram import Bot
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler



# Гороскопи для знаків
horoscopes = {
    "Овен♈️": "Гороскоп на день для Овна:\n\n Сьогодні ви сповнені енергії! 🚀 Використовуйте цей день для рішучих дій та досягнення мети. 💪🔥",
    "Телец♉️": "Гороскоп на день для Тельця:\n\n Спокій та затишок — ваші найкращі друзі сьогодні. ☕️🏡 Подаруйте собі моменти релаксу. 🌸",
    "Близнюки♊️": "Гороскоп на день для Близнюки:\n\n День спілкування та нових ідей! 💬💡 Ваші слова заряджатимуть інших, а нові знайомства принесуть несподівані можливості. 🌟",
    "Рак♋️": "Гороскоп на день для Рака:\n\n Сімейний затишок наповнить ваше серце теплом. 🏠❤️ Проводьте більше часу з близькими. 🌙",
    "Лев♌️": "Гороскоп на день для Лева :\n\n Ви сяєте, як сонце! 🌞✨ Будьте сміливими у своїх починаннях — успіх поруч. 🦁💎",
    "Діва♍️": "Гороскоп на день для Діви:\n\n Сьогодні — ідеальний день для організації справ. 📋🖋 Упорядкованість принесе вам спокій. 🌿",
    "Терези♎️": "Гороскоп на день для Терези: \n\n Шукайте гармонію у всьому. ⚖️💎 Спілкування, мистецтво або час із друзями наповнять вас позитивом. 🎶🎨",
    "Скорпіон♏️": "Гороскоп на день для Скорпіона:\n\n Ваша інтуїція сьогодні неперевершена. 🔮❤️ Використайте цей день, щоб зробити крок до своїх мрій. 🦂✨",
    "Стрілець♐️": "Гороскоп на день для Стрільця:\n\n Вирушайте у пригоди! 🗺🏞 Нові враження наповнять вас натхненням. 🌈",
    "Козоріг♑️": "Гороскоп на день для Козорогів:\n\n Завершення важливих справ сьогодні буде особливо успішним. 🏔💼 Не зупиняйтесь — вершина вже близько! 💪",
    "Водолій♒️": "Гороскоп на день для Водолія:\n\n Ваше креативне мислення сяє. 🎨🌊 Втілюйте свої унікальні ідеї, вони можуть змінити все. 🌟",
    "Риби♓️": "Гороскоп на день для Риби:\n\n Дозвольте собі помріяти. 🌊💙 Тиша, музика або медитація допоможуть відновити сили. 🎵✨",
    # Додайте інші знаки з гороскопами
}

async def start(update, context):
    await update.message.reply_text(
        "Привіт! Напиши /goroskop, щоб отримати гороскоп на день."
    )

async def goroskop(update, context):
    keyboard = [
        [InlineKeyboardButton("Овен♈️", callback_data='Овен♈️')],
        [InlineKeyboardButton("Телец♉️", callback_data='Телец♉️')],
        [InlineKeyboardButton("Близнецы♊️", callback_data='Близнецы♊️')],
        [InlineKeyboardButton("Рак♋️", callback_data='Рак♋️')],
        [InlineKeyboardButton("Лев♌️", callback_data='Лев♌️')],
        [InlineKeyboardButton("Діва♍️", callback_data='Діва♍️')],
        [InlineKeyboardButton("Терези♎️", callback_data='Тереза♎️')],
        [InlineKeyboardButton("Скорпіон♏️", callback_data='Скорпіон♏️')],
        [InlineKeyboardButton("Стрелець♐️", callback_data='Стрелець♐️')],
        [InlineKeyboardButton("Козоріг♑️", callback_data='Козоріг♑️')],
        [InlineKeyboardButton("Водолій♒️", callback_data='Водолій♒️')],
        [InlineKeyboardButton("Риби♓️", callback_data='Риби♓️')],
        # Додайте кнопки для інших знаків
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Виберіть свій знак зодіаку:', reply_markup=reply_markup)

async def button(update, context):
    query = update.callback_query
    sign = query.data
    await query.answer()
    await query.edit_message_text(text=horoscopes.get(sign, "Гороскоп не знайдено"))

def main():
    # Замість вашого токену
    application = Application.builder().token("Your bot code").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("goroskop", goroskop))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
