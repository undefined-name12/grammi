from aiogram import (
    Router,
    F
)
from aiogram.types import (
    CallbackQuery
)
from sqlalchemy.ext.asyncio import AsyncSession
from .imgbw_callback import imgbw_callback

imgbw_router = Router()

@imgbw_router.callback_query(F.data == "process_bw")
async def on_process_bw_click(callback: CallbackQuery, session: AsyncSession):
    """
    on_process_bw_click
    """
    await imgbw_callback(callback, session)
