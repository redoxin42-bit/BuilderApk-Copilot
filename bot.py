import telebot
from github import Github

# Данные
TOKEN = "8781245369:AAHTA0EFtI6cTDotq3XlxtdmTIW5HIKxJGg"
GH_TOKEN = "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"
REPO_NAME = "redoxin42-bit/BuilderApk-Copilot"

bot = telebot.TeleBot(TOKEN)
gh = Github(GH_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    btn1 = telebot.types.InlineKeyboardButton("📂 Показать файлы", callback_data="list_files")
    btn2 = telebot.types.InlineKeyboardButton("🚀 Запустить Build APK", callback_data="trigger_build")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "<b>Wellon Terminal Online</b>", parse_mode="HTML", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "list_files")
def list_files(call):
    try:
        repo = gh.get_repo(REPO_NAME)
        contents = repo.get_contents("")
        text = "<b>Корень репозитория:</b>\n"
        for item in contents:
            icon = "📁" if item.type == "dir" else "📄"
            text += f"{icon} <code>{item.path}</code>\n"
        bot.send_message(call.message.chat.id, text, parse_mode="HTML")
    except Exception as e:
        bot.send_message(call.message.chat.id, f"Ошибка: {e}")

if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()
