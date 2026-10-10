from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from config import ADMIN_IDS
from database import add_file

router = Router()

@router.message(Command("addfile"))
async def cmd_add_file(message: Message):
    if message.from_user.id in ADMIN_IDS:
        # Simple file addition logic can be implemented here via FSM
        await message.answer("Yangi fayl qo'shish uchun, iltimos, fayl ma'lumotlarini jo'nating. (Hozircha faqat baza funksiyasi yaratildi, to'liq FSM bilan boyitish mumkin)")
