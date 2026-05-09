from telegram.ext import ConversationHandler, MessageHandler, CommandHandler, filters
from database.mongo import notes_collection
from config import ADMIN_ID

PDF, SUBJECT = range(2)

temp_data = {}

# ---------------- START UPLOAD ----------------

async def upload_start(update, context):

    user_id = update.effective_user.id

    if user_id != ADMIN_ID:
        await update.message.reply_text("Unauthorized Access")
        return ConversationHandler.END

    await update.message.reply_text(
        "Send PDF File"
    )

    return PDF

# ---------------- GET PDF ----------------

async def get_pdf(update, context):

    document = update.message.document

    if document.mime_type != "application/pdf":
        await update.message.reply_text(
            "Please send PDF only."
        )
        return PDF

    temp_data["file_id"] = document.file_id

    await update.message.reply_text(
        "Send Subject Name"
    )

    return SUBJECT

# ---------------- GET SUBJECT ----------------

async def get_subject(update, context):

    subject = update.message.text.lower()

    notes_collection.insert_one({
        "subject": subject,
        "file_id": temp_data["file_id"]
    })

    await update.message.reply_text(
        f"{subject} notes uploaded successfully ✅"
    )

    return ConversationHandler.END

# ---------------- CANCEL ----------------

async def cancel(update, context):

    await update.message.reply_text(
        "Upload Cancelled"
    )

    return ConversationHandler.END

# ---------------- HANDLER ----------------

upload_handler = ConversationHandler(

    entry_points=[
        CommandHandler("upload", upload_start)
    ],

    states={

        PDF: [
            MessageHandler(filters.Document.PDF, get_pdf)
        ],

        SUBJECT: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, get_subject)
        ]
    },

    fallbacks=[
        CommandHandler("cancel", cancel)
    ]
)