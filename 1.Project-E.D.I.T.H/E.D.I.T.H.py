import datetime
import sys
import time
import win32com.client
import speech_recognition as sr
import webbrowser
import os
import openai
import requests
import json
from datetime import datetime

API_key=""
#Add your api key here
BD=False
current_AI="edith"
chat=""
speaker = win32com.client.Dispatch("SAPI.SpVoice")
all_voices = speaker.GetVoices() # list all the english_voices


fav_sites=[["youtube","ইউটিউব এ যাও","https://www.youtube.com"],["facebook","ফেসবুক এ যাও","https://www.facebook.com"],["google","গুগল এ যাও","https://www.google.com"],
           ["wikipedia","উইকিপিডিয়াতে যাও","https://www.wikipedia.com"]]
desktop_app=[["Telegram","telegram"],["Zoom","zoom"],["CodeBlocks","codeblock"],["Opera GX Browser","opera"],["Visual Studio Code","visual studio"]]



def speak_english(text):
    global BD
    if BD!=True:
        speaker.Speak(text)

def transcribe_audio():
    global BD
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        try:
            if BD:
                command = r.recognize_google(audio_data, language='bn-BD')
                print(f"Given Command is {command}\n----------x---------------\n")
                return command

            else:
                command = r.recognize_google(audio_data, language='en-US')
                print(f"given Command is {command}\n-------------x-------------\n")
                if command.lower()=="listen in bangla":
                    speak_english("switching to bangla and voice mood is shutting down!")
                    BD=True
                return command
        except Exception as e:
            speak_english("I did not Hear You ! sorry")

def change_language(command_mode):
    global BD
    if command_mode.lower() == "listen in bangla":
        print('In Bangla Mood')
    if command_mode == "ইংরেজিতে যাও":
        BD = False
        speak_english("Voice Mood is On!")


def chat_mood(query):
    global chat
    openai.api_key = API_key
    if current_AI=='friday':
        chat+=f"Rudro: {query}\n Friday: "
    else:
        chat += f"Rudro: {query}\n Edith: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chat ,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    speak_english(response["choices"][0]['text'])
    chat+=f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

def help_mood(prompt):
    openai.api_key = API_key
    text=f"OpenAI response for prompt: {prompt} \n *****************************************\n\n"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt ,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text +=response["choices"][0]["text"]
    if not os.path.exists("GivenTask"):
        os.mkdir("GivenTask")

    with open(f"GivenTask/{''.join(prompt[0:20])}.txt","w") as file:
        file.write(text)
    if current_AI=='edith':
        speak_english("Done Sir!")
    else:
        speak_english("Done Boss!!")
    # print(response["choices"][0]["text"])



def fetch_upcoming_hacking_events(limit=3):
#limit parameter defines the information of the number of ctf events.
    current_date = datetime.now().strftime('%Y-%m-%d')
    params = {
        "limit": limit,
        "start": current_date,
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }

    response = requests.get('https://ctftime.org/api/v1/events/', params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for event in data:
            event_name=event.get("title")
            start_time=event.get("start")
            finish_time=event.get("finish")
            print(f'Event: {event_name}')
            print(f'Start Time: {start_time.split(":")[0][:int(len(start_time.split(":")[0])-3)]}')
            print(f'Finish Time: {finish_time.split(":")[0][:int(len(finish_time.split(":")[0])-3)]}')
            print('-'*50)
            speak_english(f'Event Name is : {event_name}  It will Start: {start_time.split(":")[0][:int(len(start_time.split(":")[0])-3)]}  It will Finish: {finish_time.split(":")[0][:int(len(finish_time.split(":")[0])-3)]}')
    else:
        print(f'Request failed with status code {response.status_code}')


def launchFromDesktop(application_name):
    try:
        desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        application_path = os.path.join(desktop_path, application_name)
        os.startfile(application_path)

    except Exception as e:
        print(f"Error occurred: {e}")
        print("You have to start it manually !")




def main():
    if current_AI=="edith":
        speak_english("At your service,sir.")
    else:
        speak_english("Welcome Boss !!")

    while True:
        print("Taking Command in Normal Mode\n***********************************\n")
        query_result = transcribe_audio()
        try:
            if query_result.lower() in ["listen in bangla", "ইংরেজিতে যাও"]:
                change_language(query_result)
            elif query_result.lower() == "go to sleep":
                if current_AI=="edith":
                    speak_english("Goodbye! Have a great day!")
                else:
                    speak_english("See you later, Alligator. BYE!")
                break
            else:
                query = query_result.lower()
                if "internet" in query or query in "ইন্টারনেট":
                    time.sleep(1)
                    speak_english("Internet Mode Activated")
                    print("Internet Mode Activated ")
                    print("Taking Command in Internet Mode\n***********************************\n")
                    webaddress = transcribe_audio()
                    for site in fav_sites:
                        if f"{site[0]}".lower() in webaddress.lower() or site[1] in webaddress:
                            speak_english(f"Opening {site[0]}...")
                            webbrowser.open(site[2])
                elif "time" in query or "কয়টা বাজে" in query_result:
                    strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"Time is {strfTime}")
                    speak_english(strfTime)
                elif "assistant" in query_result:
                    time.sleep(1)
                    speak_english("assistant mood Activated!!")
                    print("assistant mood Activated")
                    print("Taking Command in Assistent Mode\n***********************************")
                    application_name=transcribe_audio()
                    for app in desktop_app:
                        if f"{app[1]}".lower() in application_name.lower():
                            speak_english(f"Opening {app[1]}...")
                            time.sleep(2)
                            launchFromDesktop(app[0])

                elif "hacking" in query:
                    time.sleep(1)
                    speak_english("HACKING mood Activated!!")
                    print("HACKING mood Activated")
                    print("Taking Command in Hacking Mode\n***********************************")
                    hacker_query=transcribe_audio()
                    if "event" in hacker_query.lower():
                        fetch_upcoming_hacking_events()
                elif "help".lower() in query:
                    time.sleep(1)
                    speak_english("Help mood is activated!!")
                    print("HELP mood is activated!!")
                    print("Taking Command in Help Mode\n***********************************\n")
                    ai_query = transcribe_audio()
                    help_mood(ai_query)

                elif "conversation".lower() in query or "clear the conversation".lower() in query:
                    time.sleep(1)
                    chat = " "
                    speak_english("our conversation has been cleared !!")
                else:
                    chat_mood(query)

        except Exception as e:
            speak_english("I can't hear you !")
            print("I can't hear you! ")




if __name__=='__main__':
    print("Listening \n---------------------------------------\n")

    try:
        artificial_intelligence = transcribe_audio()

        if 'edi' in artificial_intelligence.lower():
            speaker.Voice = all_voices.Item(0)
            current_AI='edith'
            print("waking up E.D.I.T.H")
            time.sleep(3)
            main()
            sys.exit()
        elif 'friday' in artificial_intelligence.lower():
            speaker.Voice = all_voices.Item(1)
            current_AI = 'friday'
            print("waking up FRIDAY")
            time.sleep(3)
            main()
            sys.exit()
        else:
            print("Wake up the AI by their name.")
    except Exception as e:
        print("AI did not wake up . Try Again!!!")
