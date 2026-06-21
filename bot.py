from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import BOT_TOKEN, OWNER_ID

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("NightGuardBot Online ✅")

async def owner(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        await update.message.reply_text("❌ Access Denied")
        return

    await update.message.reply_text(
        "👑 Owner Panel\n\n"
        "/broadcast - Broadcast Message\n"
        "/stats - Bot Stats"
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("owner", owner))

    print("NightGuardBot Started")
    app.run_polling()

if __name__ == "__main__":
    main()
