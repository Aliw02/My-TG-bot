import telebot
import os
from decouple import config
from reply_messages import replies
from pytube import YouTube
from chatgpt import get_gpt_reply
# from gemini import gemini_reply
# from gemini2 import model2
# from PIL import Image

weather = ["weather"]
bot_tooken = config("took")
youtube = ["حملي", "حملّي", "نزلي", "نزلّي", "download".lower(), "3"]
gpt = ["4", 'gpt', "شات جي بي تي", "chat gpt"]
gemini = ["5", "gemini", "جيميني", "غوغل"]

bot = telebot.TeleBot(bot_tooken)

@bot.message_handler(commands=["start", "help"])
def welcome(message):
    return bot.send_message(message.chat.id, "Welcome to my bot😇❤️")


def isMSG(message):
    return True

@bot.message_handler(commands=gpt)
def reply_from_gpt(message):
    respons = message.text
    bot.reply_to(message, get_gpt_reply("".join(respons[1:])))
    

# @bot.message_handler(content_types=['photo'])
# def handle_photo(message):
#     file_id = message.photo[-1].file_id
#     file_info = bot.get_file(file_id)
#     downloaded_file = bot.download_file(file_info.file_path)
    
#     with open('photo.jpg', 'wb') as new_file:
#         new_file.write(downloaded_file)
    
#     img = Image.open('photo.jpg')
#     img.save(r'D:\MyFolder\venv\telegram-bot\photo.jpg')
#     bot.reply_to(message, "تم حفظ الصورة بنجاح!")
    
#     response2 = model2.generate_content(img, stream=True)
#     response2.resolve()
#     bot.reply_to(message, response2.text)
#     os.remove('photo.jpg')

# @bot.message_handler(commands=gemini)
# def reply_from_gemini(message):
#     respons = message.text
#     reply = gemini_reply(respons[1:])
#     bot.reply_to(message, reply)
    
    
@bot.message_handler(commands=youtube)
def on_download(message):
    chat_id = message.chat.id
    url_msg = bot.send_message(chat_id, "أرسل رابط الفيديو المراد تنزيله 😇😇")
    bot.register_next_step_handler(url_msg, download)
    
    
def download(message):
    chat_id = message.chat.id
    url = message.text
    yt = YouTube(url)
    yt.streams.filter(progressive= True, file_extension="mp4")
    path_save = yt.streams.get_highest_resolution().download("./Videos/")
    bot.send_message(chat_id, text=f"{yt.title}الرجاء الانتضار جاري تحميل المقطع⏳⏳")
    media = open(path_save, "rb")
    bot.send_video(chat_id, video=media)
    os.remove(path_save)

@bot.message_handler(func=isMSG)
def reply(message):

    bot.reply_to(message, replies(message.text))
    



bot.infinity_polling()

