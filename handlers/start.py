async def start(update, context):
    await update.message.reply_text(
        "🎓 Welcome to College Bot\n\n"
        "Send subject name to get Notes or Question Papers."
    )