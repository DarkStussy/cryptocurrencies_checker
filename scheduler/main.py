import asyncio

import aioschedule

from .currencies import diff_currency


async def scheduler():
    aioschedule.every(1).hours.do(diff_currency)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
