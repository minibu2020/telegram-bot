from telegram import Update
from telegram import BotCommand
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from telegram.ext import CommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

BOT_TOKEN = "_API_KEY_"

# Main Menu
async def set_bot_commands(application):
    commands = [
        BotCommand("getmyownbot", "Get your own bot"),
        BotCommand("about", "About this bot"),
        BotCommand("contact", "Contact Support"),
    ]
    await application.bot.set_my_commands(commands)

async def get_my_own_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Want your own Telegram bot?\n\nFill out this form to get started:\nhttps://mytgbotafr.com/bot-request"
    )

async def about_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ *About This Bot*\n\nThis bot automatically welcomes new group members and helps you stay connected via our channel.\n\nMade with ❤️ using Python & Telegram Bot API.",
        parse_mode="Markdown"
    )

async def contact_us(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📬 *Contact Us*\n\nHave questions or need support?\nReach out via email: support@mytgbotafr.com\nOr DM @_uname_",
        parse_mode="Markdown"
    )

# DM New Group Members
async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    invite_link = "https://t.me/@Channel"

    for member in update.message.new_chat_members:
        try:
            await context.bot.send_message(
                chat_id=member.id,
                text=(
                    f"👋 Welcome, {member.first_name}!\n\n"
                    f"Thanks for joining our group. ..:\n"
                    f"{invite_link}"
                )
            )
        except Exception as e:
            print(f"Failed to message {member.username or member.id}: {e}")

# /start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Replace these URLs with your actual Telegram links
    channel_link = "https://t.me/@Channel"
    group_link = "https://t.me/+Group"

    # Define inline buttons
    keyboard = [
        [InlineKeyboardButton("📢 Join Channel", url=channel_link)],
        [InlineKeyboardButton("👥 Join Group", url=group_link)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send welcome message with buttons
    await update.message.reply_text(
        "👋 Welcome! We'll be sending feeds and suggestions on trades you should do📲. If you're not ready to learn, you can't earn 💡💵.\n"
        "Please consider joining both our *channel* for updates and our *group* for discussions 👇",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
# Register custom command handlers
app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("getmyownbot", get_my_own_bot))
app.add_handler(CommandHandler("about", about_bot))
app.add_handler(CommandHandler("contact", contact_us))
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_new_member))

# Set bot menu commands on startup
app.post_init = set_bot_commands

print("Bot is running...")
app.run_polling()
