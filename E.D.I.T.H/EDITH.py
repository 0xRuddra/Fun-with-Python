import datetime

import win32com.client
import speech_recognition as sr
import webbrowser
BD=False
speaker = win32com.client.Dispatch("SAPI.SpVoice")
all_voices = speaker.GetVoices() # list all the english_voices
speaker.Voice = all_voices.Item(1)
# change the voice to the second one in the list (indexing is 0-based)



def speak_english(text):
    global BD
    if BD!=True:
        speaker.Speak(text)

def transcribe_audio():
    global BD
    # Create an instance of the Recognizer class
    r = sr.Recognizer()
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")
        # Read the audio data from the default microphone
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        # Convert speech to text
        try:
            if BD:
                command = r.recognize_google(audio_data, language='bn-BD')
                print(f"given Command is {command})")
                return command

            else:
                command = r.recognize_google(audio_data, language='en-US')
                print(f"given Command is {command})")
                if command.lower()=="listen in bangla":
                    speak_english("switching to bangla and voice mood is shutting down!")
                    BD=True
                return command


        except Exception as e:
            speak_english("some error occured ! sorry")

def change_language(command_mode):
    global BD
    if command_mode.lower() == "listen in bangla":
        print('In Bangla Mood')
    if command_mode == "ইংরেজিতে যাও":
        BD = False
        speak_english("Voice Mood is On!")


fav_sites=[["youtube","ইউটিউব এ যাও","https://www.youtube.com"],["facebook","ফেসবুক এ যাও","https://www.facebook.com"],["google","গুগল এ যাও","https://www.google.com"],
           ["wikipedia","উইকিপিডিয়াতে যাও","https://www.wikipedia.com"]]
print("Listening")
speak_english("Listening")


while True:
    query_result=transcribe_audio()
    try:
        if query_result.lower() in ["listen in bangla","ইংরেজিতে যাও"]:
            change_language(query_result)
        elif query_result.lower() == "bye bye":
            break
        else:
            query=query_result.lower()
            if "internet" in query or "ইন্টারনেট":
                print("I am in internet mode")
                speak_english("Internet mode ON")
                webaddress=transcribe_audio()
                for site in fav_sites:
                        if f"Open {site[0]}".lower() in webaddress.lower() or site[1] in webaddress:
                            speak_english(f"Opening {site[0]}...")
                            webbrowser.open(site[2])
            if "the time" in query_result:
                strfTime=datetime.datetime.now().strftime("%H:%M:%S")


    except Exception as e:
        print("something went wrong")
















