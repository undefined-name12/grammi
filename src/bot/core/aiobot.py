""" tgrambuddy/src/bot/core/aiobot.py

aiobot.py defines the AioBot class, which encapsulates the logic for
interacting with the Telegram Bot API using the aiogram library.
It handles initialization of the bot and dispatcher, registration of
message handlers, and the main event polling loop.

TgramBuddy - A solution for building and managing Telegram bots.
Copyright (c) 2025 Maks V. Zaikin
Released by 01-May-2025 under the MIT License.
"""
import asyncio
import logging
from aiogram import (
    Bot,
    Dispatcher
)

from src.database.db_adapter import DBAdapter

from ..features import (
    onboarding,
    imgupload,
    imgbw,
)
from ..middleware.db_middleware import DbAdapterMiddleware

class AioBot:

    def __init__(self, token: str, logging: logging, db_adapter:DBAdapter)->None:
        self.bot = Bot(token)
        self.dp = Dispatcher()
        self.logging=logging

        self.dp.message.middleware(DbAdapterMiddleware(db_adapter))
        self.dp.callback_query.middleware(DbAdapterMiddleware(db_adapter))

    def register_routers(self):
        """
        register_routers
        """

        self.dp.include_router(onboarding.get_start_command_router())
        self.dp.include_router(imgupload.get_imgupload_router())
        self.dp.include_router(imgbw.get_imgbw_router())

    async def run(self):
        """
        run
        """

        self.register_routers()

        try:
            await self.dp.start_polling(self.bot)
        except asyncio.CancelledError:
            self.logging.info("Bot shutdown triggered by keyboard interrupt (Ctrl+C)")
        finally:
             
            #shutdown storage if it supports wait_closed
            storage = self.dp.fsm.storage
            wait_closed = getattr(storage, "wait_closed", None)
            if callable(wait_closed):
                await wait_closed()

            await self.bot.session.close()
            logging.info("Bot and resources closed successfully.")