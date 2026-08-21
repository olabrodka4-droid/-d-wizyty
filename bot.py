import os
import asyncio
from telegram import Bot

async def main():
    token = os.environ["TELEGRAM_TOKEN"]
    bot = Bot(token=token)

    me = await bot.get_me()
    print(f"Bot работает: @{me.username}")

if __name__ == "__main__":
    asyncio.run(main())
