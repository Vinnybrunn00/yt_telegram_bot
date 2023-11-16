from telebot.async_telebot import AsyncTeleBot
from utils import downtube, buff_file, message_bot
import asyncio, os, sys

if sys.platform == 'win32':
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ModuleNotFoundError:
        print('usage: pip install python-dotenv')
else:
    from dotenv import load_dotenv
    load_dotenv()

token = os.getenv('TOKEN')
bot = AsyncTeleBot(token=token)
print('conectado')

@bot.message_handler(commands=['start'])
async def start(message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, message_bot, parse_mode='Markdown')

@bot.message_handler(content_types=['text'])
async def yt_bot(message):
    link = message.text
    chat_id = message.chat.id
    if ('youtube' in link) or ('youtu.be' in link):
        await bot.send_message(chat_id, '› Aguarde, desfragmentando o video... 🤖')
        downtube(link)
        if os.path.exists('video'):
            try:
                video = buff_file()
                await bot.send_message(chat_id, '› Quase pronto... 🤖')
                await bot.send_video(chat_id, video=video, caption='Baixado com Sucesso 🤖✔️')
                print('alguem baixou video')
                video.close()
            except Exception as e:
                print(e)
                await bot.send_message(chat_id, '❗ Ocorreu um erro inesperado, tente novamente ❗')
    else:
        await bot.send_message(chat_id, '❗ Este link não é válido ❗')
        
asyncio.run(bot.polling(non_stop=True))