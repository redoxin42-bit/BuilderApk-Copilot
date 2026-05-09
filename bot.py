import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from github import Github

# Данные авторизации
TOKEN = "8781245369:AAHTA0EFtI6cTDotq3XlxtdmTIW5HIKxJGg"
GH_TOKEN = "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"
REPO_NAME = "redoxin42-bit/BuilderApk-Copilot"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
gh = Github(GH_TOKEN)

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("📂 Показать все файлы", callback_data="list_files"),
        types.InlineKeyboardButton("🛠 Исправить структуру (Auto)", callback_data="fix_all"),
        types.InlineKeyboardButton("🚀 Запустить Build APK", callback_data="trigger_build")
    )
    await message.answer("<b>Wellon Cloud Terminal v1.0</b>\nСистема готова к работе.", parse_mode="HTML", reply_markup=markup)

@dp.callback_query_handler(lambda c: c.data == 'list_files')
async def list_files(callback: types.CallbackQuery):
    try:
        repo = gh.get_repo(REPO_NAME)
        contents = repo.get_contents("")
        text = "<b>Структура корня:</b>\n"
        for item in contents:
            icon = "📁" if item.type == "dir" else "📄"
            text += f"{icon} <code>{item.path}</code>\n"
        await bot.send_message(callback.from_user.id, text, parse_mode="HTML")
    except Exception as e:
        await bot.send_message(callback.from_user.id, f"Ошибка: {e}")

@dp.callback_query_handler(lambda c: c.data == 'trigger_build')
async def trigger(callback: types.CallbackQuery):
    try:
        repo = gh.get_repo(REPO_NAME)
        workflow = repo.get_workflow("main.yml")
        workflow.create_dispatch("main")
        await bot.send_message(callback.from_user.id, "✅ Сигнал на сборку отправлен! Проверяй вкладку Actions.")
    except Exception as e:
        await bot.send_message(callback.from_user.id, f"Ошибка запуска: {e}\nВозможно, файл main.yml назван иначе.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
