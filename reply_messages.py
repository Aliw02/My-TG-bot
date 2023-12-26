from weather import getCurrentWeather
import random
# from chatgpt import get_gpt_reply
# from googletrans import Translator

greetings = ['شلونك', "شخبارك", "شونك", "whts up".lower()]
inf = ["منو انت", "انت منو", "أنت منو", "منوأنت", "ho r u".lower()]
inst = ["Instagram and telegram".lower(), "instagram", "facebook".lower(), "انستجرام","أنستجرام ", "حسابك", "تليجرام", "تليغرام", "فيسبوك", "فيس", "أنستغرام", "انستغرام", 'حساب المبرمج']
# gpt = ["4", 'gpt', "شات جي بي تي", "chat gpt"]


greet_rep = ["حبيبي بخير انت شونك", "هلو بالوردة", "بخير الحمدلله، انت شخبارك", "ماشي الحال:)"]
inst_rep = """ 
تكدر تتواصل وياي على حساباتي
--------------------------------
instg---> @https://instagram.com/abnaboodcode?igshid=cnJkOHVsNjZlb3hu
tele---> @a2_ab
facebook---> @https://www.facebook.com/ali.abood.94009841?mibextid=ZbWKwL
                """
                
weather = ['weather', "طقس", "الطقس"]
najaf = ['Najaf', "najaf", "النجف الأشرف", "النجف", "نجف"]
basra = ["basra".lower(), "البصره", "البصرة", "بصره", "بصرة"]

translate = ["translate", "ترجملي", "ترجم"]
mm = """
1- اكدر ادزلك طقس محافظتك😁
2- اكدر أترجملك للعربية من أي لغة😉 
3- اكدر احملّك فيديوهات من اليوتيوب بس دز /حملّي وبعدين الرابط😇
"""
youtube = ["download", "حملّي", "حملي", "نزلّي", "نزلي"]
ss = ["شتكدر تسوي؟", "شتكدر تسوي"]


def replies(message):
    words = message.split()  
    
    # if words[0] in translate:
    #     translator = Translator()
    #     translation = translator.translate(" ".join(words[1:]), dest="ar")
    #     return translation.text
    if words[0] in weather:
        if words[1] == "النجف" or words[1] == "najaf".lower():
            report = getCurrentWeather(words[1])
            return report
        elif words[1] == "البصرة":
            report = getCurrentWeather(words[1])
            return report
        elif words[1] == "baghdad".lower() or words[1] == "بغداد":
            report = getCurrentWeather(words[1])
            return report
    elif message in greetings:
        rand_greet_rep = random.choice(greet_rep)
        return rand_greet_rep
    # elif message in gpt:
    #     gpt_reply = get_gpt_reply(" ".join(words[1:]))
    #     return gpt_reply
    
    elif message == "مرحبا":
        return "مرحبتين حبيبي😍"
            
    elif message in ss:
        return mm
    
    elif message in inf:
        return "اني عبارة عن بوت, مُبَرمَج من قِبل عليوي عبود "
    
    
    elif message in inst :
        return inst_rep

    else:
        return "العفو، مافهمتك حالياً بطور التطوير :)"