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


# -----------------------------------
# CREATE BOT APPLICATION
# -----------------------------------
app = Application.builder().token(TOKEN).build()


# -----------------------------------
# START COMMAND
# -----------------------------------
app.add_handler(
    CommandHandler("start", start)
)


# -----------------------------------
# ADMIN FILE UPLOAD
# -----------------------------------
app.add_handler(upload_handler)


# -----------------------------------
# SEARCH NOTES / QUESTION PAPERS
# -----------------------------------
app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        get_notes
    )
)


# -----------------------------------
# RUN BOT
# -----------------------------------
print("MongoDB Connected Successfully")
print("Bot Running...")


app.run_polling(
    drop_pending_updates=True
)