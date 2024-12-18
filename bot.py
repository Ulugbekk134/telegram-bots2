from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

# Start komandasi
async def start(update: Update, context):
    # Foydalanuvchiga tugmalarni ko'rsatish
    keyboard = [
        [InlineKeyboardButton("1-qism", callback_data="part_1")],
        [InlineKeyboardButton("2-qism", callback_data="part_2")],
        [InlineKeyboardButton("3-qism", callback_data="part_3")],
        [InlineKeyboardButton("4-qism", callback_data="part_4")],
        [InlineKeyboardButton("5-qism", callback_data="part_5")],
        [InlineKeyboardButton("6-qism", callback_data="part_6")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Salom! 'Uyda yolg'iz' filmining qaysi qismini ko'rmoqchisiz? Tugmalardan birini tanlang:",
        reply_markup=reply_markup
    )

# Film qismini yuborish
async def send_film(update: Update, context):
    query = update.callback_query
    await query.answer()
    part = query.data  # Foydalanuvchi tanlagan qism

    # Fayl nomlarini aniqlash
    files = {
        "part_1": "uyda_yolgiz_1qism.mp4",
        "part_2": "uyda_yolgiz_qism2.mp4",
        "part_3": "uyda_yolgiz_qism3.mp4",
        "part_4": "uyda_yolgiz_qism4.mp4",
        "part_5": "uyda_yolgiz_qism5.mp4",
        "part_6": "uyda_yolgiz_qism6.mp4",
    }

    # Tanlangan qismini yuborish
    video_path = files.get(part)
    if video_path:
        await query.message.reply_text(f"Mana shu kanalda link https://t.me/Uyda_yolgiz_6_qismi:, {part.replace('_', '-')} qism:shu kanalda link https://t.me/Uyda_yolgiz_6_qismi")
        await query.message.reply_video(open(video_path, 'rb'))
    else:
        await query.message.reply_text("Kechirasiz, fayl topilmadi.")

# Botni sozlash
app = ApplicationBuilder().token("7932835574:AAFTZiz3eiaBMrzQat8DeiJ1Ny6UN60mSCY").build()

# Handlerlarni qo'shish
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(send_film))

# Botni ishga tushirish
app.run_polling()
