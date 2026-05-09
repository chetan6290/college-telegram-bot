import os
import re

PAPERS_FOLDER = "files/papers"

async def search_pdf(update, context):

    if not update.message or not update.message.text:
        return

    query = update.message.text.lower()

    query_words = query.split()

    found = False

    for file in os.listdir(PAPERS_FOLDER):

        file_lower = file.lower()

        matched = all(
            word in file_lower
            for word in query_words
        )

        if matched:

            found = True

            file_path = os.path.join(
                PAPERS_FOLDER,
                file
            )

            with open(file_path, "rb") as pdf:

                await update.message.reply_document(
                    document=pdf
                )

    if not found:

        await update.message.reply_text(
            "No PDFs found."
        )