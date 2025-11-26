import logging
from openai import AsyncOpenAI

from cache.file_cache import get_cached, set_cached
from config import settings

logger = logging.getLogger(__name__)

client = AsyncOpenAI(api_key=settings.openai_api_key)

DEFAULT_SYSTEM_PROMPT = (
    "Ти — помічник для студентської лабораторної роботи. "
    "Відповідай коротко, по суті і зрозуміло."
)

FREE_MODEL = "gpt-4o-mini"


async def ask_gpt_with_cache(prompt: str) -> str:
    cached = await get_cached(prompt)
    if cached:
        logger.info("Cache hit")
        return cached

    logger.info("Cache miss — sending to OpenAI")

    try:
        response = await client.chat.completions.create(
            model=FREE_MODEL,
            messages=[
                {"role": "system", "content": DEFAULT_SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )

        content = response.choices[0].message.content.strip()
        await set_cached(prompt, content)
        return content

    except Exception as e:
        logger.exception("OpenAI error")
        return f"Помилка під час звернення до GPT: {e.__class__.__name__}"