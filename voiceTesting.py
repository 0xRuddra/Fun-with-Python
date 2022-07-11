import json
import requests

def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)
usrip=input()
if __name__=='__main__':
   url="http://ip-api.com/json/"
   unfip=requests.get(url+usrip).text
   fip=json.loads(unfip)
   if fip["status"]=="success":

       speak("Here's your information")
       speak(f"your country is {fip['country']} ")
       speak(f"your city is {fip['city']}")
       speak(f"your isp is {fip['isp']}")
   else:
       print("You gave wrong ip ")