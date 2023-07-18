import datetime
import win32com.client
import speech_recognition as sr
import webbrowser
import os
import openai
from config import API_key


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


def ai_mood(prompt):
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
    if not os.path.exists("OpenAI"):
        os.mkdir("OpenAI")

    with open(f"OpenAI/{''.join(prompt[0:20])}.txt","w") as file:
        file.write(text)
    # print(response["choices"][0]["text"])


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
            if "internet" in query or query in "ইন্টারনেট":
                print("I am in internet mode")
                speak_english("Internet mode ON")
                webaddress=transcribe_audio()
                for site in fav_sites:
                        if f"Open {site[0]}".lower() in webaddress.lower() or site[1] in webaddress:
                            speak_english(f"Opening {site[0]}...")
                            webbrowser.open(site[2])
            if "the time" in query_result or "কয়টা বাজে" in query_result:
                strfTime=datetime.datetime.now().strftime("%H:%M:%S")
                print(f"Time is {strfTime}")
                speak_english(strfTime)
            if "a software" in query_result:
                pass

            if "call ai".lower() in query:
                speak_english("AI mode is ON")
                ai_query=transcribe_audio()
                ai_mood(ai_query)



    except Exception as e:
        print("something went wrong")










# This is in working-stage
# def open_application_on_desktop(application_name):
#     try:
#         desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
#         application_path = os.path.join(desktop_path, application_name)
#         os.startfile(application_path)
#
#     except Exception as e:
#         print(f"Error occurred: {e}")
#
# if __name__ == "__main__":
#     # Replace 'YourApplication.lnk' with the name of the application shortcut on your desktop
#     application_name = "OpenVPN Connect"
#     open_application_on_desktop(application_name)


