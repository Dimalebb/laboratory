import json
import asyncio
from pathlib import Path
from typing import Optional
from config import settings

_cache_lock = asyncio.Lock()
_cache_path = Path(settings.cache_file)

# ensure directory exists
_cache_path.parent.mkdir(parents=True, exist_ok=True)

async def _read_cache_file() -> dict:
    def _read():
        if not _cache_path.exists():
            return {}
        try:
            with _cache_path.open("r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            # if file corrupted or empty, return empty dict
            return {}
    return await asyncio.to_thread(_read)

async def _write_cache_file(data: dict) -> None:
    def _write():
        with _cache_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    await asyncio.to_thread(_write)

async def get_cached(prompt: str) -> Optional[str]:
    async with _cache_lock:
        data = await _read_cache_file()
        return data.get(prompt)

async def set_cached(prompt: str, response: str) -> None:
    async with _cache_lock:
        data = await _read_cache_file()
        data[prompt] = response
        await _write_cache_file(data)

async def clear_cache() -> None:
    async with _cache_lock:
        await _write_cache_file({})