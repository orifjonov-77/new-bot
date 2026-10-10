from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from keyboards.reply import get_main_menu
from keyboards.inline import get_file_buy_keyboard, get_vip_buy_keyboard, get_payment_keyboard, get_admin_contact_keyboard
from database import add_user, get_user, check_vip, get_files_by_category, get_file
from config import CARD_NUMBER, CARD_OWNER, VIP_PRICE

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    add_user(message.from_user.id)
    await message.answer(
        "👋 Xush kelibsiz! StudySpace botiga marhamat.\nQuyidagi menyudan kerakli bo'limni tanlang:",
        reply_markup=get_main_menu()
    )

@router.message(F.text == "👤 Shaxsiy kabinet")
async def cabinet_handler(message: Message):
    user = get_user(message.from_user.id)
    is_vip = check_vip(message.from_user.id)
    status = "VIP 💎" if is_vip else "Oddiy"
    
    text = (
        f"👤 Shaxsiy kabinet\n\n"
        f"🆔 ID: {message.from_user.id}\n"
        f"💰 Balans: {user[1]} so'm\n"
        f"💎 Holat: {status}\n"
    )
    if is_vip:
        text += f"⏳ VIP muddati: {user[3]}"
        
    await message.answer(text)

@router.message(F.text == "💎 VIP Obuna")
async def vip_handler(message: Message):
    if check_vip(message.from_user.id):
        await message.answer("Sizda allaqachon VIP obuna mavjud! 💎")
    else:
        await message.answer(
            f"💎 VIP Oylik Obuna\n\n"
            f"Narxi: {VIP_PRICE} so'm / oy\n"
            f"Imkoniyatlar: Barcha pullik fayllarni 1 oy davomida tekin yuklab olish.\n\n"
            f"Sotib olish uchun quyidagi tugmani bosing:",
            reply_markup=get_vip_buy_keyboard(VIP_PRICE)
        )

@router.message(F.text == "🌐 Vebsayt buyurtma qilish")
async def website_handler(message: Message):
    await message.answer(
        "🌐 Vebsayt yaratish xizmati\n\n"
        "Tayyor vebsayt yaratish xizmatlari (500 000 so'mdan $200 gacha, loyiha murakkabligiga qarab).\n"
        "Buyurtma berish yoki ma'lumot olish uchun admin bilan bog'laning:",
        reply_markup=get_admin_contact_keyboard()
    )

@router.message(F.text == "📞 Qo'llab-quvvatlash")
async def support_handler(message: Message):
    await message.answer(
        "Savollar va takliflar uchun admin bilan bog'laning:",
        reply_markup=get_admin_contact_keyboard()
    )

@router.callback_query(F.data == "buy_vip")
async def process_buy_vip(callback: CallbackQuery):
    await callback.message.edit_text(
        f"To'lov qilish uchun rekvizitlar:\n\n"
        f"💳 Karta: `{CARD_NUMBER}`\n"
        f"👤 Ega: {CARD_OWNER}\n"
        f"💰 Summa: {VIP_PRICE} so'm\n\n"
        f"To'lov qilib bo'lgach, 'To'lov qildim' tugmasini bosing.",
        parse_mode="Markdown",
        reply_markup=get_payment_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data == "check_payment")
async def process_check_payment(callback: CallbackQuery):
    await callback.message.edit_text("To'lov tekshirilmoqda... \n(Bu yerda Click/Payme integratsiyasi bo'ladi, hozircha admin tasdiqlashi kerak)")
    await callback.answer()

# Qolgan katalog va fayllarni chiqarish logikasi...

@router.message(F.text == "📊 Taqdimotlar")
async def taqdimotlar_handler(message: Message):
    await message.answer("📊 Taqdimotlar bo'limi:\n\nTez kunda bu yerga fanlar va mavzular bo'yicha taqdimotlar qo'shiladi.\nHozircha katalog bo'sh.")

@router.message(F.text == "📝 BSB va MSB Materiallari")
async def bsb_msb_handler(message: Message):
    await message.answer("📝 BSB va MSB Materiallari:\n\nTez kunda bu yerga yechimlar va materiallar joylanadi.")

@router.message(F.text == "🔬 Laboratoriya & Mustaqil ishlar")
async def lab_handler(message: Message):
    await message.answer("🔬 Laboratoriya & Mustaqil ishlar:\n\nBu yerda tayyor hisobotlar va titul varaqlari joylanadi.")
