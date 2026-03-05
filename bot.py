import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "futures" in text:
        reply = "Futures trading allows leverage and speculation."
    elif "spot" in text:
        reply = "Spot trading means direct buying and selling."
    elif "risk" in text:
        reply = "Never trade emotionally. Protect your capital."
    else:
        reply = "I am OpenClaw AI. Ask me about Binance trading."

    await update.message.reply_text(reply)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
