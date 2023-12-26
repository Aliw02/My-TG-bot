from decouple import config
import google.generativeai as genai
import PIL.Image




google_api = config("GOOGLE_API")
genai.configure(api_key=google_api)

model2 = genai.GenerativeModel('gemini-pro-vision')
    
model2
        
    
# print(gemini_reply2())