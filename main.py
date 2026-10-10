import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import user, admin
from database import init_db

logging.basicConfig(level=logging.INFO)

async def main():
    # Baza initsializatsiyasi
    init_db()
    
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    # Routerni ro'yxatdan o'tkazish
    dp.include_router(user.router)
    dp.include_router(admin.router)

    
    # Botni ishga tushirish
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
