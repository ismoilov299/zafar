import asyncio
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import *
from data.music_controller import MusicSearcher
from keyboards.inline.keyboards import KeyboardSetter
from loader import dp


@dp.message_handler(commands=['top'])
async def top_command(message: types.Message):
    main_keyboard = types.InlineKeyboardMarkup()

    main_keyboard.add(types.InlineKeyboardButton(text="Uzbekistan 🇺🇿", callback_data="top_UZ"))
    main_keyboard.add(types.InlineKeyboardButton(text="Russia 🇷🇺", callback_data="top_ru"))

    await message.answer("Выберите страну:", reply_markup=main_keyboard)


@dp.callback_query_handler(lambda c: c.data.startswith('top_'))
async def process_top_callback(callback_query: types.CallbackQuery):
    selected_country = callback_query.data.replace('top_', '')
    print(selected_country)

    loading_msg = await callback_query.message.answer("🎵 Загрузка...")

    searcher = MusicSearcher()
    keyboarder = KeyboardSetter()
    search_result = await searcher.top_chart10(selected_country)
    keyboard = await keyboarder.search_result_keyboard(search_result)

    musics_info = ""
    line = 1
    for info in search_result[0][0]:
        musics_info += f"{line}.{info[0][0]} ~ {info[0][1]}\n"
        line += 1

    await loading_msg.delete()
    await callback_query.message.edit_text(text=musics_info, reply_markup=keyboard)


