from aiogram import types, Dispatcher
from aiogram.filters import Command
import logging

logger = logging.getLogger(__name__)


async def start_handler(message: types.Message):
    await message.answer(
        "Привіт! Я GPT-бoт.\n"
        "Просто напиши питання, і я передам його OpenAI."
    )


def register_start_handlers(dp: Dispatcher):
    dp.message.register(start_handler, Command(commands=["start", "help"]))
    logger.info("Start handlers registered")