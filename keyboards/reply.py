from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📊 Taqdimotlar"), KeyboardButton(text="📝 BSB va MSB Materiallari")],
            [KeyboardButton(text="🔬 Laboratoriya & Mustaqil ishlar")],
            [KeyboardButton(text="💎 VIP Obuna"), KeyboardButton(text="🌐 Vebsayt buyurtma qilish")],
            [KeyboardButton(text="👤 Shaxsiy kabinet"), KeyboardButton(text="📞 Qo'llab-quvvatlash")]
        ],
        resize_keyboard=True
    )
