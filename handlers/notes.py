from database.mongo import db

notes_collection = db["notes"]

async def get_notes(update, context):

    subject = update.message.text.lower()

    note = notes_collection.find_one({"subject": subject})

    if note:
        await update.message.reply_document(note["file_id"])
    else:
        await update.message.reply_text("Notes not found.")