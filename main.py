import speech_recognition as sr
import os
import webbrowser
import datetime
from openai import OpenAI

api_key = "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"
chatStr = ""
def chat(query):
    global chatStr
    
    chatStr+= f"Aditya: {query}\nCuxy: "
    client = OpenAI(api_key=api_key)
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": chatStr}
        ],
        temperature=1,
        max_tokens=1576,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    # todo: wrap this in a try-catch block
    chatStr += f"{response.choices[0].message.content} \n"
    # print(chatStr)
    say(response.choices[0].message.content)
    return response.choices[0].message.content

    
def ai(prompt):
    client = OpenAI(api_key=api_key)
    text = f"\n ************************************** \n Openai response for prompt: {prompt} \n ***************************** \n"  
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=1,
        max_tokens=1576,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    # todo: wrap this in a try-catch block
    # print(response.choices[0].message.content)
    text+= response.choices[0].message.content
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
        
    with open("Openai/prompt.txt","a") as f:
        f.write(text)
    
def say(text):
    os.system(f'say -v Alex "{text}" ')
    
def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source: # using default microphone as source
        r.pause_threshold = 1 # python will wait 1 sec of silence before stop listening
        audio = r.listen(source) # listen to microphone(source)
        print("Recognizing...")
        
        try:
            query = r.recognize_google(audio, language="en-in") # convert audio to text
            print(f"User said : {query}")
            return query
        
        except Exception as e:
            return "Some error occured. Sorry from cuxy."
        
if __name__=="__main__": # only run if i am running this file from this file
    say("cuxy here")
    
    while True:                 # will continue listening without ending the program
        print("Listening...")
        query = takeCommand()      # listen to my voice and store in query  
        
        sites = [["youtube", "https://youtube.com"],["wikipedia","https://wikipedia.com"], ["google", "https://google.com"], ["my website", "https://aadityabaniya.netlify.app"], ["my friend website", "https://shivendrabhagat.com"], ["facebook", "https://facebook.com"]]
        
        # check if my query(my voice) contains any of the website names, then open the same website
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                if "my" in site[0]:
                    text = site[0].replace("my", "your")
                    say(f'opening "{text}"')
                else:
                    say(f'Opening "{site[0]}" sir...')
                
                webbrowser.open(site[1])
                
        # open music
        if "open music" in query.lower():
            say("Opening music")
            musicpath = "/Users/aadityabaniya/Downloads/song.mp3"
            os.system(f'open "{musicpath}"') # this is written in f'open "{}" ' format
            
        # saying time
        elif "the time" in query.lower():
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f'The time is "{strfTime}"')
            
        # open facetime(apps)
        elif "open facetime".lower() in query.lower():
            os.system(f"open /System/Applications/FaceTime.app")
            
        # using openai
        elif "using artificial intelligence".lower() in query.lower():
            ai(query)
            
        elif "quit".lower() in query.lower():
            exit()
            
        else:
            chat(query)
            
        # say(query)