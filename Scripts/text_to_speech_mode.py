import RPi.GPIO as GPIO
import time
import cv2
import pytesseract
from picamera.array import PiRGBArray
from picamera import PiCamera
from gtts import gTTS
import os
from langdetect import detect
import pygame
import subprocess
from tempfile import TemporaryFile




#####
pygame.mixer.pre_init(frequency=40000, buffer=64)

pygame.mixer.init()

def modename():


        pygame.mixer.music.load("/home/ibraheemt/mu_code/modenames/ttsEN.mp3")


        # Play the audio and wait for it to finish
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue


        pygame.mixer.music.load("/home/ibraheemt/mu_code/modenames/ttsAR.mp3")

        # Play the audio and wait for it to finish
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue


# Clean up
        pygame.mixer.quit()

####

def processing_sound():
    pygame.mixer.pre_init(frequency=45000, buffer=64)


    pygame.mixer.init()


    pygame.mixer.music.load("/home/ibraheemt/mu_code/threading pygame test/finalWaitingSound.ogg")

    # Play the audio and wait for it to finish
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.quit()

def notxt():
    pygame.mixer.pre_init(frequency=26000, buffer=64)


    pygame.mixer.init()


    pygame.mixer.music.load("/home/ibraheemt/mu_code/textNotFound.mp3")

    # Play the audio and wait for it to finish
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.quit()
#####
def TTS(text):
        processing_sound()

        pygame.mixer.pre_init(frequency=26000, buffer=64)


        pygame.mixer.init()
        speech = gTTS(text=text, lang=language, slow=False)

        # Saving the converted audio in a file named 'output.mp3'
        speech.save("output.mp3")



        pygame.mixer.music.load("output.mp3")

        # Play the audio and wait for it to finish
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue


        # Clean up
        pygame.mixer.quit()
#####
#####

#####
modename()
# Set up the GPIO pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

##GPIO.setup(2, GPIO.HIGH)
##GPIO.setup(3, GPIO.HIGH)
##GPIO.setup(4, GPIO.HIGH)
##GPIO.setup(17, GPIO.HIGH)
##GPIO.setup(27, GPIO.HIGH)
##GPIO.setup(22, GPIO.HIGH)

# Set up the camera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30
camera.brightness = 50
camera.contrast = 50
camera.saturation = 50
camera.rotation = 0
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9' '0']
# Capture frames from the camera
rawCapture = PiRGBArray(camera, size=(640, 480))
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    #cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)

#while True:
    input_state = GPIO.input(13)
    if input_state == False:

        # OCR the image
        text = pytesseract.image_to_string(image, lang='ara+eng')
        print(text)

                # text = 'text not found'
        #if any(char.isdigit() for char in text):
        #    for n in num:
        #        if n in text:
        #            language = 'en'
        ##            TTS(text)
        #        break
        #else:
        if not text.strip():
            notxt()

        if text.strip():
            language = detect(text)
            if language == "fa":
                language = "ar"
        #    if not language == "ar":
        #        language = "en"
            TTS(text)
            print(language)





cv2.destroyAllWindows()
