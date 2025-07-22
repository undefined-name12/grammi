from aiogram import (
    Router, 
    F
)
from aiogram.types import (
    Message, 
    CallbackQuery
)
from sqlalchemy.ext.asyncio import AsyncSession

from .imgupload_handler import (
    save_compressed_image,
    save_raw_image
)
from .imgupload_callback import upload_photo_callback

imgupload_router = Router()

@imgupload_router.message(F.photo)
async def on_photo_upload(message: Message, session: AsyncSession):
    """
    Handles photo upload from a user.

    Args:
        message (Message): The incoming Telegram message with photo.
        session (AsyncSession): Database session.
    """
    await save_compressed_image(message, session)

@imgupload_router.message(F.document)
async def on_document_upload(message: Message, session: AsyncSession):
    """
    Handles document upload that might contain an image.

    Args:
        message (Message): The incoming Telegram message with document.
        session (AsyncSession): Database session.
    """
    await save_raw_image(message, session)

@imgupload_router.callback_query(F.data == "upload_photo")
async def on_upload_photo_click(callback: CallbackQuery):
    """
    on_upload_photo_click
    """
    await upload_photo_callback(callback)
