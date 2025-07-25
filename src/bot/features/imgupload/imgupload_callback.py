from pathlib import Path
from aiogram.types import CallbackQuery
from src.bot.core.localization import (
    load_locale,
    localize_message
)

async def upload_photo_callback(callback: CallbackQuery
                                ):
    """
    upload_photo_callback
    """
    locale = load_locale(Path(__file__))    
    if callback.message:
        await callback.message.answer(localize_message(locale, "upload_image_message"))

    await callback.answer()
