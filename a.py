from telegram import Bot, Update
from telegram.ext import Application, MessageHandler, filters

# Replace these with your Bot Token
BOT_TOKEN = "xxxxxx"

# Channel usernames (include '@' symbol)
CHANNEL_A_USERNAME = "@xxx"
CHANNEL_B_USERNAME = "@xxx"

async def forward_message(update: Update, context):
    # Get the message
    message = update.channel_post

    # Forward the message to Channel B
    if message:
        await context.bot.forward_message(
            chat_id=CHANNEL_B_USERNAME,
            from_chat_id=CHANNEL_A_USERNAME,
            message_id=message.message_id
        )

def main():
    # Set up the application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add a handler to monitor Channel A
    application.add_handler(
        MessageHandler(filters.Chat(CHANNEL_A_USERNAME), forward_message)
    )

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
