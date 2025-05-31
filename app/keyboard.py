from aiogram.types import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='🍴 Меню')],
                                         [KeyboardButton(text='📞 Контакты'), KeyboardButton(text='🎁 Акции')],
                                         [KeyboardButton(text='✍️ Оставить отзыв')]],
                                         resize_keyboard=True)

