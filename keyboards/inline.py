from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import CARD_NUMBER, CARD_OWNER

def get_file_buy_keyboard(file_id, price):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=f"Sotib olish ({price} so'm)", callback_data=f"buy_file_{file_id}")]
        ]
    )

def get_vip_buy_keyboard(price):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=f"VIP sotib olish ({price} so'm)", callback_data="buy_vip")]
        ]
    )

def get_payment_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💳 To'lov qildim", callback_data="check_payment")]
        ]
    )

def get_admin_contact_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Admin bilan bog'lanish", url="https://t.me/orifjonovv_77")] # Admin usernameni o'zgartiring
        ]
    )
