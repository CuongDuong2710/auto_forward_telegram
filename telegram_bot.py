import logging
from telegram import Bot, Update
from telegram.ext import Application, MessageHandler, filters

# Replace these with your Bot Token
BOT_TOKEN = "xxxxxxxxxxxxxxxxxx"

# Channel ID (format: -100xxxxxxxxx)
CHANNEL_A_ID = -1000000000000
CHANNEL_B_ID = -1000000000000

# Channel usernames (include '@' symbol)
CHANNEL_A_USERNAME = "@xxx"
CHANNEL_B_USERNAME = "@xxx"

async def log_message(update: Update, context):
    print(update)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def forward_message(update: Update, context):
    # Get the message
    message = update.channel_post

    # Forward the message to Channel B
    if message:
        logger.info(f"Received message in Channel A: {message.text}")
        try:
            # Forward the message to Channel B
            await context.bot.forward_message(
                chat_id=CHANNEL_B_ID,
                from_chat_id=CHANNEL_A_ID,
                message_id=message.message_id
            )
            logger.info("Message forwarded successfully.")
        except Exception as e:
            logger.error(f"Failed to forward the message: {e}")
    else:
        logger.error(f"Failed to forward the message: {e}")

def main():
    # Set up the application
    application = Application.builder().token(BOT_TOKEN).build()

    # application.add_handler(MessageHandler(filters.ALL, log_message))

    # Add a handler to monitor Channel A
    application.add_handler(
        MessageHandler(filters.Chat(CHANNEL_A_ID), forward_message)
    )

    # Start the bot
    logger.info("Bot is starting...")
    application.run_polling()

if __name__ == "__main__":
    main()
