from gtts import gTTS
import os
import time
from selenium import webdriver
from selenium.webdriver.opera.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def speak(audiostring):
    print(audiostring)
    tts=gTTS(text=audiostring,lang='tr')
    tts.save("audio.mp3")
    os.system("audio.mp3")

import speech_recognition as sr

def recordAudio():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Dinleniyor...")
        audio=r.listen(source)

        data= ""
    try:
        data=r.recognize_google(audio,language='tr-tr')
        data=data.lower()
        print(data)
    except sr.UnknownValueError:
        print("ne dedigini anlamadim")
    return data

def asistan(data):
    if ("merhaba"or"selam") in data:
       speak("Hosgeldin")
    elif "kapat" in data:
        speak("bay bay")
    elif "çal" in data.split():
        data=data.split()
        parcaismi=""
        for i in data[:-1]:
            parcaismi=parcaismi+i
        speak(parcaismi+" çalınıyor")
        driver=webdriver.Chrome('C:/Users/demur/Desktop/chromedriver.exe')
        driver.get("https://www.youtube.com/results?search_query="+parcaismi)
        select_element=driver.find_elemnts_by_xpath('//*[@id="video-title"]')
        for option in select_element:
            option.find_element_by_xpath('//*[@id="video-title"]').click()
            option.switch_to.frame(option.find_element_by_xpath('//iframe[starts-with(@src, "https://www.youtube.com/embed")]'))
            WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Play"]'))).click()
            break
       
    else:
        print("tamam")

time.sleep(2)
speak("Hosgeldiniz")
frag =1
while frag==1:
            data=recordAudio()
            asistan(data)
            if "kapat" in data:
                frag=0
    