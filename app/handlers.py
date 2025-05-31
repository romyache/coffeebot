from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from app import keyboard as kb
from app.database import requests as rq

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer('☕ Добро пожаловать в нашу кофейню!\n\n'
    'Выберите действие:', reply_markup=kb.keyboard)


@router.message(F.text == '🍴 Меню')
async def show_menu(message: Message):
    menu_text = ('Наше меню:\n\n'
    '- Эспрессо — 150 руб.\n'
    '- Латте — 200 руб.\n'
    '- Капучино — 220 руб.\n'
    '- Чизкейк — 180 руб.\n')
    await message.answer_photo(photo='https://i.pinimg.com/originals/c5/e1/ae/c5e1ae788399297835496f41322b22e3.jpg',
                               caption=menu_text)


@router.message(F.text == "📞 Контакты")
async def show_contacts(message: Message):
    await message.answer('📍Мы находимся по адресу ул.Кофейная, д.1\n\n' \
    '📞Телефон: +7 (123) 456-78-90\n\n' \
    '🕒Часы работы: 8:00 – 22:00')


@router.message(F.text == "🎁 Акции")
async def show_promo(message: Message):
    await message.answer("🎉Акции этой недели:\n\n"
        "- Скидка 20% на все кофе до 12:00\n\n"
        "- Бесплатный десерт к заказу от 500 руб.")


@router.message(F.text == "✍️ Оставить отзыв")
async def ask_review(message: Message):
    await message.answer("Напишите ваш отзыв в одном сообщении:")


@router.message(F.text)
async def save_review(message: Message):
    if message.text not in ["🍴 Меню", "📞 Контакты", "🎁 Акции", "✍️ Оставить отзыв"]:
        await rq.add_review(message.from_user.id, message.text)
        await message.answer("Спасибо за ваш отзыв! ❤️")

