import pyttsx3
import speech_recognition as sr
import datetime
import google.generativeai as genai
from PIL import ImageGrab
import webbrowser
import wikipedia
import os
import pywhatkit as kit
import random 
import time
import cv2
from instagrapi import Client
import pywhatkit as kit



def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hearing.....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing....")
            data = recognizer.recognize_google(audio)
            print(f"You said: {data}\n")
            return data
        except sr.UnknownValueError:
            print("NOT UNDERSTAND")
            return ""

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)  
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 150)
    engine.say(x)
    engine.runAndWait()

def date():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    current_date = now.strftime("%Y-%m-%d")
    hour = now.hour
    if hour >= 0 and hour < 12:
        speechtx(f"Good morning sir. The current time is {current_time} and today's date is {current_date}. How can I help you?")
    elif hour >= 12 and hour < 18:
        speechtx(f"Good afternoon sir. The current time is {current_time} and today's date is {current_date}. How can I help you?")
    else:
        speechtx(f"Good evening sir. The current time is {current_time} and today's date is {current_date}. How can I help you?")

def gpt():
    import google.generativeai as genai

    
    genai.configure(api_key="# insert the End point key #")
    generation_config = {"temperature": 0.9, "top_p": 1, "max_output_tokens": 2048}
    model = genai.GenerativeModel("gemini-pro", generation_config=generation_config)


    
    convo = model.start_chat()

    while True:
        
        user_command = input("Enter 'start' to begin or 'end' to exit: ").strip().lower()

        if user_command == "start":
            while True:
                user_input = input("Tech Marvel: ")
                if user_input.strip().lower() == "end":
                    break
                convo.send_message(user_input)
                response = convo.last.text
                print(f"Marvel: {response}")
        elif user_command == "end":
            
            print("Ending the chat session.")
            break
        else:
            print("Please enter 'start' to begin or 'end' to exit.")
            break
def screenshot():
    path="somu.png"
    screenshot=ImageGrab.grab()
    rgb_screenshot=screenshot.convert('RGB')
    rgb_screenshot.save(path,quality=15)


def wiki_search(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        speechtx(summary)
    except wikipedia.exceptions.DisambiguationError as e:
        speechtx("There are multiple results for your query. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speechtx("No page found for your query.")
    except Exception as e:
        speechtx("An error occurred while searching Wikipedia.")

def open_settings():
    try:
        os.system("start ms-settings:")
        speechtx("Settings opened")
    except Exception as e:
        speechtx("An error occurred while opening settings")
    
def music():
    music="C:\\Users\\somna\\Downloads\\Telegram Desktop"
    songs=os.listdir(music)
    rd=random.choice(songs)
    os.startfile(os.path.join(music,rd))

def youtube():
    webbrowser.open("www.youtube.com")

def Notpad():
    path = "C:\\Windows\\System32\\notepad.exe"  
    os.startfile(path)




def send_whatsapp_message():
    
    speechtx("Please tell me the phone number.")
    phone_no = sptext().replace("", "")

   
    phone_no = "+91" + phone_no

    
    speechtx(f"You said: {phone_no}. Please tell me the message you want to send.")
    message = sptext()

    
    try:
        kit.sendwhatmsg_instantly(phone_no, message)
        speechtx("Message sent successfully")
    except Exception as e:
        speechtx("An error occurred while sending the message")




def instagram():
    username = "#################"
    password = "#################"


    recipient_username = input("Enter the recipient's Instagram username: ")
    message_text = input("Enter the message to send: ")


    client = Client()
    client.login(username, password)


    try:
        user_id = client.user_id_from_username(recipient_username)
        client.direct_send(message_text, [user_id])
        print(f"Message sent to {recipient_username}")
    except Exception as e:
        print(f"An error occurred: {e}")


    client.logout()

def capture_photo_from_camera():
    
    vc = cv2.VideoCapture(0)

   
    cv2.namedWindow("preview")

    if vc.isOpened(): 
        rval, frame = vc.read()
    else:
        rval = False

    while rval:

        cv2.imshow("preview", frame)

        
        key = cv2.waitKey(20)

        if key == 27: 
            break
        elif key == ord('c'):  
           
            cv2.imwrite("captured_photo.png", frame)
            print("Photo captured and saved as 'captured_photo.png'")

      
        rval, frame = vc.read()

    vc.release()
    cv2.destroyWindow("preview")



def set_alarm():
    def get_valid_number(prompt):
        while True:
            speechtx(prompt)
            try:
                number = int(sptext())
                return number
            except ValueError:
                speechtx("I didn't catch that. Please say a valid number.")

    speechtx("Please tell me the hour to set the alarm.")
    alarm_hour = get_valid_number("Please tell me the hour to set the alarm.")
    
    speechtx("Please tell me the minutes to set the alarm.")
    alarm_minute = get_valid_number("Please tell me the minutes to set the alarm.")
    
    speechtx("Is it AM or PM?")
    period = sptext().strip().lower()
    
    if period == "pm" and alarm_hour != 12:
        alarm_hour += 12
    elif period == "am" and alarm_hour == 12:
        alarm_hour = 0
    
    now = datetime.datetime.now()
    alarm = datetime.datetime(now.year, now.month, now.day, alarm_hour, alarm_minute)
    
    if alarm < now:
        alarm += datetime.timedelta(days=1)  
    speechtx(f"Alarm set for {alarm.strftime('%I:%M %p')}.")
    
    while datetime.datetime.now() < alarm:
        time.sleep(1)
    
    speechtx("Wake up! It's time!")



if __name__ == '__main__':
    while True:
        data1 = sptext().lower()
        if "wake up" in data1:
            date()


        elif "somu" in data1:
            speechtx("Somu is great")
        
        elif "open gpt" in data1:
            gpt()
        
        elif "take screenshot" in data1:
            screenshot()
            speechtx("Done sir")
        
        elif "open settings" in data1:
            open_settings()
        
        elif "search " in data1:
            query = data1.replace("search wikipedia for", "").strip()
            wiki_search(query)

        elif "send whatsapp message" in data1:
             send_whatsapp_message()
        
        elif "music" in data1:
             music()

        elif "notepad" in data1:
            Notpad()

        elif "youtube" in data1:
             youtube()
             speechtx("Browser opened")
             
        elif "set alarm" in data1:
            set_alarm()

        elif "instagram" in data1:
            instagram()

        elif "camera" in data1:
            capture_photo_from_camera()

        elif "go to sleep" in data1:
            speechtx("Okay sir, call me any time")
            break