from dotenv import load_dotenv
import speech_recognition as sr
import pyttsx3
import pyaudio
import time
import pvporcupine
import struct
import winsound
import os
import subprocess
import webbrowser
from google.cloud import dialogflow_v2beta1 as dialogflow
from jinxauto import *
from todoapp import *


load_dotenv()
DIALOGFLOW_PROJECT_ID = 'jinx-droo'
DIALOG_LANGUAGE_CODE = 'en'
SESSION_ID = 'me'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'private_key.json'


#-----------------------DIALOGFLOW---------------------------------------------
def DF(text_to_be_analyze): # sends text to dialogflow and return what bruno should do next
    session_client = dialogflow.SessionsClient() #used to interact with the dialogflow API allowing the function to send and receive messages
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID) #used to create a unique identifier necessary for maintaining the conversation context with Dialogflow.
    
    text_input = dialogflow.TextInput(text=text_to_be_analyze, language_code=DIALOG_LANGUAGE_CODE) # rep the user's input as a text input object, which is then used to send the user's message to Dialogflow for processing.
    query_input = dialogflow.QueryInput(text=text_input) #used by dialogflow API to understand the user's intent and context of the conversation for processing
    
    
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
        print("Query text:", response.query_result.query_text)
        
        jinx_do = response.query_result.intent.display_name # intent that you get back from dialogflow
        print("| Detected intent is: " + jinx_do + " Detected intent confidence : ", response.query_result.intent_detection_confidence, end="|")
        
        answer = response.query_result.fulfillment_text # response from dialogflow
        
    except Exception as e:
        print("Exception: " + str(e))
        
        answer = 'nu'
        jinx_do ='error'
        print("Dialogflow connection error= ", end="")
        pass
    if answer != 'nu':
        speak(answer)
        
        return jinx_do


def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    print("CEE: "+ text + "\n")
    engine.say(text)
    engine.runAndWait()



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        det_sound()
        print("listening...")
        audio = r.listen(source)
        rep_sound()
        
        try:
            command = r.recognize_google(audio, language='en-in')
            print("Cee think you said: "+ command)
            return command.lower()
            
        except Exception as e:
            print("Exception: " + str(e))
            return " "
        


def det_sound():
    winsound.Beep(500,200)

def rep_sound():
    winsound.Beep(600,200)
    
    
def website(url):
    webbrowser.get().open(url)
    
    
    
def convo_flow():
    load_task()
    while True:
        said = takeCommand()
        if not said:
            print("I didn't catch that, please try again.")
            continue
        
        
        do_now = DF(said)
        if "do_now" == "exit":
            speak("exiting the loop sir")
            break
        if do_now == "music":
            if "play my favourite song" in said:
                speak("this is my favourite to")
                website("https://www.youtube.com/watch?v=ZrPNkjE7x1M&list=RDZrPNkjE7x1M&start_radio=1")
                break
            elif " ":
                playPlaylist()
                break
        if 'play alex rider' in said:
            speak("playing alex rider for you sir")
            playAlexRider()
            break
        if 'next song' in said:
            speak("playing next song")
            next()
            break
            
    
        if "are you good" in said:
            speak("Hello, how can I help you?")
        
        elif "is this thing good" in said:
            speak("yes it is the best thing")
            
        elif "open my email" in said:
            speak("I will open your email right away")
        
        elif "are you evil" in said:
            speak("if I am in the wrong hands then I can be evil, but I am not evil, I am just a program created to assist you in your daily tasks")
            
        elif "how are you" in said:
            speak("doing well,")
        elif "goodbye" in said:
            speak("")
            break
        
        elif "Good Morning" in said:
            speak("good morning sir, how are doing today, did you sleep well")
        
        elif "what is your name" in said:
            speak("My name is Jinx, your personal assistant.")
            
        elif "who are you" in said:
            speak("I am jinx, your personal assistant.")
            
        elif "good morning" in said:
            speak("good morning! How can I assist you today?")
        
        elif "thank you" in said:
            speak("You are welcome!") 
        
        elif "open youtube please" in said:
            speak("opening youtube for you sir")
            website("https://www.youtube.com/")
            break
        
        
        elif "play my favourite song" in said:
            speak("this is my favourite to")
            website("https://www.youtube.com/watch?v=ZrPNkjE7x1M&list=RDZrPNkjE7x1M&start_radio=1")
            break
            
        elif "open task manager" in said:
            try:
                subprocess.Popen("taskmgr")
                speak("task manager is now open sir")
            except:
                speak("Error opening task manager, please try again later.")
            
        elif "open my email" in said:
            speak("Opening your email right away.")
            website("https://mail.google.com/mail/u/0/#inbox")
            break
        
        elif "open calculator" in said:
            try:
                subprocess.Popen("calc")
                speak("opening Calculator right away sir")
            except:
                speak("Error opening calculator, please try again later.")
            
            break
            
            
        elif "goodnight"  in said:
            speak("Goodnight! Sleep well.")
        
        
### add task, show task, complete task, delete task

### --------ADD TASKS--------

        elif do_now == "add task":
            
            
            follow_up = takeCommand().strip()
            
           
            if follow_up and follow_up.lower() != " ":
                result = add_new_task(follow_up)
            else:
                result = "I didn't catch that task. Please try again."


                
            speak(result)
            break
            
           
            
            

###----------SHOW TASKS--------
        elif do_now == "show task":
            result = show_list()
            speak(result)

        elif "complete task" in said:
            try:
                num = int(said.split()[-1]) - 1
                result = mark_task(num)
            except:
                result = "Please say a valid task number."
            speak(result)
            
#####-----------DELETE TASKS--------
        elif "delete task" in said:
            try:
                num = int(said.split()[-1])-1
                result = delete_task(num)
            except:
                result = "Please say a valid task number."
            speak(result)
        
        elif do_now == "stop":
            break
            
    time.sleep(2)
    

def main():
    porcupine = None
    pa = None
    audio_stream = None
    
    print("Awaiting for your call sir")
    
    try:
        porcupine = pvporcupine.create(
        access_key='3qSfbhwjM61EHbIrYDw4Mvu8mTevIxNnNFaATtIb4J4OPleW1+7L1Q==', 
        keyword_paths=['bruno_en_windows_v3_0_0.ppn']
    )
        pa = pyaudio.PyAudio()
        audio_stream = pa.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )
        while True:
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
            
            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                print("Keyword Detected")
                det_sound()
                speak("Yes, how can I help you?")
                convo_flow()
                time.sleep(1)
                print("bruno:Awaiting your call")
        
        
    finally:
        if porcupine is not None:
            porcupine.delete()
        
        if audio_stream is not None:
            audio_stream.close()
            
        if pa is not None:
            pa.terminate()
 
main()