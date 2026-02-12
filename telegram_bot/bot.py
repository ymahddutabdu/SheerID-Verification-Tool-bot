from telegram.ext import Updater, CommandHandler
import subprocess

BOT_TOKEN = "6776491200:AAG4zoYPenOHzVZbJa7DIqYIZnecGwD4pWk"

def start(update, context):
    update.message.reply_text(
        "أهلاً! استخدم الأوامر للتحقق مع الرابط:\n"
        "/spotify <رابط>\n"
        "/youtube <رابط>\n"
        "/canva <رابط>\n"
        "/googleone <رابط>\n"
        "/chatgpt <رابط>\n"
        "/veteran <رابط>"
    )

def run_service(script_name, update, args):
    try:
        cmd = ["python", f"services/{script_name}.py"]
        if args:
            cmd.extend(args)  # نمرر الرابط أو المدخلات للسكربت
        result = subprocess.check_output(cmd)
        update.message.reply_text(result.decode("utf-8"))
    except Exception as e:
        update.message.reply_text(f"خطأ أثناء التنفيذ: {e}")

def spotify(update, context): run_service("spotify_check", update, context.args)
def youtube(update, context): run_service("youtube_check", update, context.args)
def canva(update, context): run_service("canva_check", update, context.args)
def googleone(update, context): run_service("googleone_check", update, context.args)
def chatgpt(update, context): run_service("chatgpt_check", update, context.args)
def veteran(update, context): run_service("veteran_check", update, context.args)

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("spotify", spotify))
    dp.add_handler(CommandHandler("youtube", youtube))
    dp.add_handler(CommandHandler("canva", canva))
    dp.add_handler(CommandHandler("googleone", googleone))
    dp.add_handler(CommandHandler("chatgpt", chatgpt))
    dp.add_handler(CommandHandler("veteran", veteran))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
