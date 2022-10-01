import ntpath
from pydoc import cli
from grpc import server
from importlib.resources import path
import pyttsx3
from regex import R
from rsa import encrypt
from sklearn.ensemble import VotingClassifier                          
import speech_recognition as sr
import datetime
import wikipedia                        
import webbrowser
import random
import sys
import psutil
import time
import os
import os.path
import requests
import cv2                              #pip install opencv-python
from requests import get                #pip install requests
import pywhatkit as kit
import smtplib                          #pip install secure-smtplib
import pyjokes                                                #pip install pyautogui
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders, header                      
import operator
import PyPDF2
import instaloader
import pyautogui
from cryptography.fernet import Fernet
import  tkinter as tk
from tkinter import filedialog
import numpy
import socket
import termcolor
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import socket
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
newVoiceRate= 180
engine.setProperty('rate',newVoiceRate)

# text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(audio)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        #audio = r.listen(source,timeout=4,pharse_time_limit=7)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        # speak("say that again please...")
        return "none"
    return query

# to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M:%p")
    
    if hour >= 0 and hour <= 12:
        speak(f"good morning, its {tt}")
    elif hour >= 12 and hour <= 18:
        speak(f"good afternoon, its {tt}")
    elif hour >=18 and hour <=22:
        speak(f"good evening, its {tt}")
    
    elif hour >=22 and hour <=24:
        speak(f"good night sir, its time to sleep , its {tt} ")

    speak("Iam Laura sir. Please Tell me how may i help you")
 
# to sent email
def sentEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('YOUR EMAIL ADDRESS', 'YOUR PASSWORD')
    server.sentmail('YOUR EMAIL ADDRESS', to, content)
    server.close()

# for news update
def news():
    
    url = 'https://www.bbc.com/news'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h3')
    unwanted = ['BBC World News TV', 'BBC World Service Radio',
			'News daily newsletter', 'Mobile app', 'Get in touch']

    for x in list(dict.fromkeys(headlines)):
	    if x.text.strip() not in unwanted:
		    speak(x.text.strip())

def Reading():
    Tk().withdraw()
    filename = askopenfilename()
    #book =open('E:\\Laura(PREFINAL)\\sample.pdf', 'rb')
    pdfReader=PyPDF2.PdfFileReader(filename)
    paged = pdfReader.numPages
    print(paged)
    speak = pyttsx3.init()
    from_page = pdfReader.getPage(0)
    text=from_page.extractText()
    speak.say(text)
    speak.runAndWait()


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)

def bat():
    battery=psutil.sensors_battery()
    percentage = battery.percent
    speak(f"sir our system have {percentage} percent battery")

def taskexecution():    
    speak("verfication Successful")
    speak("Welcome Vignesh")
    pyautogui.press('esc')             
    wish()
    while True:

        query = takecommand().lower()

        #logical building for tasks

        if "open notepad" in query:
            #npath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\notepad.exe"
            #os.startfile(npath)
            os.system("start Notepad")
        
        elif "open mrt" in query or "open tool" in query:
            npath="C:\\Windows\\System32\\MRT.exe"
            os.startfile(npath)
            #os.system("start mrt")
            try:
                pyautogui.moveTo(470,550,duration=2)
                pyautogui.click(470,550,duration=1)
                pyautogui.click(470,550,duration=2)
            except Exception as e:
                    print(e)
                    speak("Sorry sir")

        elif "open adobe reader" in query:
            apath = "C:\\Program File (x86)\\Adobe\\Reader 11.0\\Reader\\AcroRd32.exe"
            os.startfile(apath)

        elif "open command prompt" in query:
            os.system("start cmd")
        
        elif "play music" in query or "play song" in query:
            speak("Here you go with music")
            music_dir = "E:\\music"
            songs = os.listdir(music_dir)
            print(songs)
            #Tk().withdraw()
            #filename = askopenfilename()
            #speak("Here you go with music")   
            random=os.startfile(os.path.join(music_dir, songs[0]))
            #random=os.startfile(os.path.join(filename))


        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=5)
            speak("according to wikipedia")
            speak(results)
            # print(result)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "search on internet" in query:
            speak("sir, what shoud i search on internet")
            cm = takecommand()
            #os.system("start chrome")
            webbrowser.open(f"{cm}")
        
        elif "cpu usage" in query or "cpu" in query:
            cpu()
        
        elif "battery" in query or "battery percentage" in query:
            bat()
        
        elif "good night" in query:
            speak("good night Vignesh")
        
        
       # elif "camera" in query or "take a photo" in query:
           # ec.capture(0, "Jarvis Camera ", "img.jpg")


        #elif "send whatsapp message" in query:
        #   kit.sendwhatsmsg("+91 user_number", "your_message",4,13)
        #   time.sleep(120)
        # speak("message has been sent")

        #elif "song on youtube" in query:
        #   kit.playonyt("see you again")

        #elif "email to yokesh" in query:
        #   try:
        #       speak("what should i say?")
        #       content = takecommand()
        #       to = "EMAIL OF THE OTHER PERSON"
        # sendEmail(to,content)
        #speak("Email has been sent to yokesh")
        #   except Exception as e:
        #       print(e)
        #       speak("sorry sir, i am not able to send this mail to yoki")

        elif "you can sleep" in query or "sleep now" in query or "good bye" in query or "quit" in query:
            speak("thanks for using me sir, have a good day")
            sys.exit()




        #to close any application
        elif "close notepad" in query:
            speak("okay sir, closing notepade")
            os.system("taskkill /f /im notepad.exe")
        
        elif "close chrome" in query:
            speak("okay sir, closing chrome")
            os.system("taskkill /f /im chrome.exe")
        
        elif "player" in query:
            speak("okay sir, closing musicplayer")
            os.system("taskkill /f /im groovemusic.exe")

        #to set a alarm
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour())
            if nn==22:
                music_dir = 'E:\\music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
            
        #to find a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
        
        elif "shutdown" in query or "shutdown the system" in query:
            os.system("shutdown /s /t 1")
    
                

        elif "restart" in query:
           os.system("shutdown /r /t 1")
        
        elif "log out" in query or "signout" in query:
            os.system("shutdown /l ")

        #elif "sleep the system" in query:
        #   os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "hello" in query or "hey" in query:
            speak("hello sir, may i help you with something.")

        elif "how are you" in query:
            speak("i am fine sir, what about you")

        elif "thank you" in query or "thanks" in query:
            speak("it's my pleasure sir.")

################################################################################################################################            
        elif 'switch the window' in query or "switch window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "tell me news" in query or "today news" in query:
            speak("please wait sir, feteching the latest news")
            news()

        elif "email" in query:
            speak("what should i do for you")
            query = takecommand()
            if "send a mail" in query or "sent a mail" in query:
                email = 'studyp695@gmail.com' #enter gmail
                password = 'thilak_2002 1' #enter the pass word
                send_to_email ='yokeshyoga399@gmailcom' #enter the receiver mail id here
                #speak("ok sir, what is the subject of the email")
                #query = takecommand()
                subject = query  # the subject in the email
                speak("and sir, what is the message for this email")
                query2 = takecommand()
                message = query2 # message in the mail
                speak("sir please enter the correct path of the file into the shell")
                file_location = input("please enter the path here") #file attachment in the mail
                
                speak("please wait , i am sending the email now")

                msg=MIMEMultipart()
                msg['From']=email
                msg['To']=send_to_email
                msg['subject'] = subject 

                msg.attach(MIMEText(message , 'plain'))

                #setup the attachment
                filename = os.path.basename(file_location)
                attachment = open(file_location, 'rb')
                part =MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Dispositition', "attachment ; filename= %s " % filename )

                #attach the attachment to the MIMEMultipart object
                msg.attach(part)

                server=smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit()
                speak("Email has been sent sucessfully")

            else:
                email = 'studyp695@gmail.com' #enter your gmail
                password = 'thilak_2002 1' #enter your pass word
                send_to_email ='yokeshyoga399@gmail.com' #enter the receiver mail id here
                message = query # Message in the mail

                server = smtplib.SMTP('smtp.gmail.com',587)#connecting the server
                server.starttls() #usetls
                server.login(email,password)
                server.sendmail(email, send_to_email , message)#send the mail
                server.quit() #Logout of the server
                speak("I Can't Understand")
        elif "do some calculations" in query or "calculate" in query or "can you calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("say what you want to calculate")
                print("Listening....")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string=r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return{
                    '+' : operator.add,
                    '-' : operator.sub,
                    'mul' : operator.mul,
                    'div' : operator.__truediv__,
                    '%' : operator.mod,
                    'mod' : operator.mod,
                    '^' : operator.xor,
                    }[op]
            def eval_binary_expr(op1 ,oper ,op2):
                op1,op2=int(op1) , int(op2)
                return get_operator_fn(oper)(op1 ,op2)
            print(eval_binary_expr(*(my_string.split())))

#________________________ To find My Location Using IP Adresses ________________________________________________#

        elif "where i am" in query or "where we are" in query:
            speak("wait sir, Let me check")
            try:
                ipAdd =requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data =geo_requests.json()
                #print(geo_data)
                city=geo_data['city']
                #state =geo_data['state']
                country=geo_data['country']
                speak(f"sir i am not sure , but i think we are in {city} city of {country} country")
            except Exception as e:
                speak("Sorry sir , Due to network issue i am not able to find where we are.")
                pass

#------------- to check  instagram profile-----------#
        elif "instagram profile " in query or "profile" in query:
            speak("sir please enter the use name correctly")
            name=input("enter usernane here:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user {name}")
            time.sleep(5)
            speak("sir would you like to download profile picture of this account.")
            condition = takecommand()
            if "yes" in condition:
                mod = instaloader.Instaloader() #pip install instadownloader
                mod.download_profile(name, profile_pic_only= True)
                speak("i'm done sir, profile picture is saved in our main folder. now i am ready for next command")
            else:
                pass


#--------------------- To take screenshot ---------------#
        elif "take screenshot" in query or "screenshot" in query :
            speak("sir. please tell me the name for this screenshot file")
            name=takecommand()
            speak("please sir hold the screen for few seconds , i am taking a shot")
            time.sleep(3)
            img=pyautogui.screenshot()
            img.save(f"{name}.jpeg")
            speak("i am done sir , the screenshot is saved in our main folder . now i am ready for next command")

#--------------------- To Read PDF FILE ----------------------#
        elif "read pdf" in query or "read PDF" in query or "read a pdf" in query:
            Reading()

#----------------------- To hide file and folder ----------------------#

        elif "hide all files" in query or "hide this folder" in query or "visible for every one" in query:
            speak("sir please tell me you want to hide this folder or make visible for everyone")
            Condition = takecommand()
            if "hide" in Condition:
                os.system("attrib +h /s /d")
                speak("sir,all the files in this folder are now hidden.")
    
            elif "visible" in condition:
                os.system("attrib -h /s /d")    
                speak("sir, all the files in this folder are now visible to everyone. i think yougotit....  ")

            elif "leave it" or "leave for now" in condition:
                speak("ok sir")
        
        elif "remember me" in query:
            speak("Waht should i remember")
            data= takecommand()
            speak("you said me to remember" + data)
            remember=open("data.txt","w")
            remember.write(data)
            remember.close()
        
        elif "do you know anything" in query or "i forgot anything" in query:
            remember = open("data.txt","r")
            speak("You said me to remember that" + remember.read())
        
        elif "encryption" in query or "encrypt" in query:
            key=Fernet.generate_key()
            file=open('key.key','wb')
            file.write(key)
            file.close()
            with open('test.txt','rb') as f:
                data=f.read()
            fernet=Fernet(key)
            encrypted=fernet.encrypt(data)
            
            with open('test.txt','wb') as f:
                f.write(encrypted)
            speak("Encryption done Successfully")

        elif "decrypt" in query:
            file=open('key.key','rb')
            key=file.read()
            file.close()
            with open('test.txt','rb') as f:
                data=f.read()
            fernet=Fernet(key)
            decrypted=fernet.decrypt(data)
            with open('test.txt','wb') as f:
                f.write(decrypted)
            speak("Decryption is done now")
        
        elif "open camera" in query:
            vid=cv2.VideoCapture(0)
            while(True):
                ret,frame=vid.read()
                cv2.imshow('frame',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            vid.release()
            cv2.destroyAllWindows()
        
        elif "internet speed" in query:
            import speedtest
            wifi  = speedtest.Speedtest()
            print("Wifi Download Speed is ", wifi.download())
            print("Wifi Upload Speed is ", wifi.upload())

if __name__ == "__main__":
    recognizer=cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainingData.yml')
    casacadePath="haarcascade_frontalface_default.xml"
    faceCascade=cv2.CascadeClassifier(casacadePath)
    font=cv2.FONT_HERSHEY_SIMPLEX
    id=1
    names=['','Vignesh']
    cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
    cam.set(3,640)
    cam.set(4,480)
    minW=0.1*cam.get(3)
    minH=0.1*cam.get(4)
    while True:
        ret,img=cam.read()
        convert_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(
        convert_image,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW),int(minH)),
    )
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            id, accuracy=recognizer.predict(convert_image[y:y+h,x:x+w])
        if(accuracy < 100):
            id=names[id]
            accuracy=" {0}%".format(round(100 -accuracy))
            taskexecution()
        else:
            id="unknown"
            accuracy=" {0}%".format(round(100 -accuracy))
        cv2.putText(img,str(id),(x+5,y-5),font,1,(255,255,255),2)
        cv2.putText(img,str(accuracy),(x+5,y+h-5),font,1,(255,255,0),1)
    
        cv2.imshow('camera',img)

        k=cv2.waitKey(10)&0xff
        if k==10:
            break
    
    cam.release()
    cv2.destroyAllWindows()





    
    

    