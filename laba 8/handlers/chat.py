from aiogram import types, Dispatcher, F
import logging

from business.gpt_service import ask_gpt_with_cache

logger = logging.getLogger(__name__)


async def handle_text(message: types.Message):
    text = message.text.strip()
    if not text:
        return await message.answer("Введи хоч щось.")

    try:
        reply = await ask_gpt_with_cache(text)

        MAX = 4000
        for i in range(0, len(reply), MAX):
            await message.answer(reply[i:i+MAX])

    except Exception:
        logger.exception("Error in chat handler")
        await message.answer("Сталася помилка. Спробуй пізніше.")


def register_chat_handlers(dp: Dispatcher):
    dp.message.register(handle_text, F.text & (~F.command))
    logger.info("Chat handlers registered")