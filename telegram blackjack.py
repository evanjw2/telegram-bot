
import os
import logging
import json
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Path to your service account key JSON file
SERVICE_ACCOUNT_FILE = 'path/to/your/service-account-file.json'

# Scopes for Google Drive API
SCOPES = ['https://www.googleapis.com/auth/drive.file']

# Authenticate and create the Drive API client
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
drive_service = build('drive', 'v3', credentials=credentials)

# Function to upload file to Google Drive
def upload_file_to_drive(file_path, file_name):
    file_metadata = {
        'name': file_name,
        'parents': ['YOUR_FOLDER_ID']  # Replace with your folder ID
    }
    media = MediaFileUpload(file_path, mimetype='image/jpeg')
    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    logger.info(f'File uploaded with ID: {file.get("id")}')
    return f'https://drive.google.com/file/d/{file.get("id")}/view'

# Start command handler
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Send me any image and I'll upload it to Google Drive!")

# Image handler
async def handle_image(update: Update, context: CallbackContext) -> None:
    file = await update.message.photo[-1].get_file()
    file_path = f'{file.file_id}.jpg'
    await file.download(file_path)

    # Upload to Google Drive
    link = upload_file_to_drive(file_path, file_path)
    os.remove(file_path)  # Clean up local file

    await update.message.reply_text(f'Image uploaded: {link}')

# Main function
async def main():
    app = ApplicationBuilder().token("7621604261:AAG4z2RzO6kowotr8ZpoJ-SGvzsxGoncPM4").build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_image))

    await app.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())

