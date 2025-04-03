#  Copyright (c) 2025 Jotheeswar-devpy.
#  Joe_Musicbot is an open-source Telegram music bot licensed under AGPL-3.0.
#  All rights reserved where applicable.
#
#

from aiofiles import os

import config
from Joe_Musicbot import client


async def create_directories() -> None:
    """Create necessary directories."""
    from Joe_Musicbot.platforms.save_cookies import save_all_cookies
    try:
        await os.makedirs(config.DOWNLOADS_DIR, exist_ok=True)
        await os.makedirs("database/photos", exist_ok=True)
        await save_all_cookies(config.COOKIES_URL)
    except Exception as e:
        raise SystemExit(1) from e


if __name__ == "__main__":
    client.loop.create_task(create_directories())
    client.run()
