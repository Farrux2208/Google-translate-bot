from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


my_dict = {
    "O'zbekcha" : "uz",
    "Russcha" : "ru",
    "Englizcha" : "en",
}

async def lang_buttons():
    button = InlineKeyboardMarkup(row_width=3)
    for key,vel in my_dict.items():
        button.insert(InlineKeyboardButton(text=key,callback_data=f"lang_{vel}"
        ))
    return  button
