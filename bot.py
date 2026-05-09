from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters
)

from config import TOKEN

from handlers.start import start
from handlers.notes import get_notes
from handlers.upload import upload_handler

app = Application.builder().token(TOKEN).build()

# Start
app.add_handler(CommandHandler("start", start))

# Upload System
app.add_handler(upload_handler)

# Search Notes
app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        get_notes
    )
)

print("Bot Running...")

app.run_polling()