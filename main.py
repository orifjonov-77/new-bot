import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiohttp import web
from config import BOT_TOKEN
from handlers import user, admin
from database import init_db

logging.basicConfig(level=logging.INFO)

# Render port health check uchun dummy web server
async def handle(request):
    return web.Response(text="Bot is running!")

async def web_server():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    logging.info(f"Web server started on port {port}")

async def main():
    # Baza initsializatsiyasi
    init_db()
    
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    # Routerni ro'yxatdan o'tkazish
    dp.include_router(user.router)
    dp.include_router(admin.router)
    
    # Web serverni fonga yuborish
    asyncio.create_task(web_server())
    
    # Botni ishga tushirish
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
