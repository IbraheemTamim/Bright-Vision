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
def modename():
        pygame.mixer.pre_init(frequency=40000, buffer=64)

        pygame.mixer.init()


        pygame.mixer.music.load("/home/ibraheemt/mu_code/modenames/ttbEN.mp3")

        # Play the audio and wait for it to finish
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue


        pygame.mixer.music.load("/home/ibraheemt/mu_code/modenames/ttbAR.mp3")

        # Play the audio and wait for it to finish
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        pygame.mixer.pre_init(frequency=22050, buffer=64)


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

#####
#####
def TTB(text):
    braille_mapping = {
            'a': [0, 0, 0, 0, 0, 1],
            'b': [1, 1, 0, 0, 0, 0],
            'c': [1, 0, 0, 1, 0, 0],
            'd': [1, 0, 0, 1, 1, 0],
            'e': [1, 0, 0, 0, 1, 0],
            'f': [1, 1, 0, 1, 0, 0],
            'g': [1, 1, 0, 1, 1, 0],
            'h': [1, 1, 0, 0, 1, 0],
            'i': [0, 1, 0, 1, 0, 0],
            'j': [0, 1, 0, 1, 1, 0],
            'k': [1, 0, 1, 0, 0, 0],
            'l': [1, 1, 1, 0, 0, 0],
            'm': [1, 0, 1, 1, 0, 0],
            'n': [1, 0, 1, 1, 1, 0],
            'o': [1, 0, 1, 0, 1, 0],
            'p': [1, 1, 1, 1, 0, 0],
            'q': [1, 1, 1, 1, 1, 0],
            'r': [1, 1, 1, 0, 1, 0],
            's': [0, 1, 1, 1, 0, 0],
            't': [0, 1, 1, 1, 1, 0],
            'u': [1, 0, 1, 0, 0, 1],
            'v': [1, 1, 1, 0, 0, 1],
            'w': [0, 1, 0, 1, 1, 1],
            'x': [1, 0, 1, 1, 0, 1],
            'y': [1, 0, 1, 1, 1, 1],
            'z': [1, 0, 1, 0, 1, 1],
            ' ': [0, 0, 0, 0, 0, 0],


            'ا': [1, 0, 0, 0, 0, 0],
            'ب': [1, 1, 0, 0, 0, 0],
            'ت': [1, 0, 0, 1, 0, 0],
            'ث': [1, 0, 0, 1, 1, 0],
            'ج': [1, 0, 1, 1, 0, 0],
            'ح': [1, 1, 0, 1, 0, 0],
            'خ': [1, 1, 0, 1, 1, 0],
            'د': [0, 1, 1, 0, 0, 0],
            'ذ': [0, 1, 1, 0, 1, 0],
            'ر': [0, 1, 1, 1, 0, 0],
            'ز': [0, 1, 1, 1, 1, 0],
            'س': [0, 1, 0, 1, 0, 0],
            'ش': [0, 1, 0, 1, 1, 0],
            'ص': [0, 1, 1, 0, 1, 1],
            'ض': [0, 1, 1, 1, 0, 1],
            'ط': [0, 1, 1, 1, 1, 1],
            'ظ': [1, 0, 1, 1, 1, 0],
            'ع': [1, 1, 0, 0, 1, 0],
            'غ': [1, 1, 0, 0, 1, 1],
            'ف': [1, 1, 0, 1, 0, 0],
            'ق': [1, 1, 0, 1, 1, 0],
            'ك': [1, 0, 1, 0, 0, 0],
            'ل': [1, 1, 1, 0, 0, 0],
            'م': [1, 0, 1, 1, 0, 0],
            'ن': [1, 0, 1, 1, 1, 0],
            'ه': [1, 0, 0, 0, 1, 0],
            'و': [0, 1, 0, 1, 1, 1],
            'ي': [1, 0, 1, 1, 1, 1],
            'ى': [1, 0, 1, 0, 1, 1],
            'ة': [0, 0, 1, 1, 1, 0],

            '1': [1, 0, 0, 0, 0, 0],
            '2': [1, 1, 0, 0, 0, 0],
            '3': [1, 0, 0, 1, 0, 0],
            '4': [1, 0, 0, 1, 1, 0],
            '5': [1, 0, 0, 0, 1, 0],
            '6': [1, 1, 0, 1, 0, 0],
            '7': [1, 1, 0, 1, 1, 0],
            '8': [1, 1, 0, 0, 1, 0],
            '9': [0, 1, 0, 1, 0, 0],
            '0': [0, 1, 0, 1, 1, 0],



            # add more letters as needed
        }
    # Print the text and convert to lowercase
    print(str.lower(text).lstrip().rstrip())
    print("Detected language:", language)

    for letter in text:
            if letter.lower() in braille_mapping:
                # Set the appropriate pins for the current letter
               # GPIO.wait_for_edge(21, GPIO.FALLING)
                # Speak the letter
                if letter == " ":
                    letter = "space"
                #if letter not in braille_mapping:
                #    letter == ' '
                pygame.mixer.pre_init(frequency=26000, buffer=64)

                pygame.mixer.init()

                tts = gTTS(text=letter, lang=language)
                tts.save('temp.mp3')
                pygame.mixer.music.load("temp.mp3")

                # Play the audio and wait for it to finish
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    continue

# Clean up
                pygame.mixer.quit()
                os.remove('temp.mp3')
                if letter == "space":
                    letter = " "
                for i, pin in enumerate(pins):
                    GPIO.output(pin, braille_mapping[letter.lower()][i])


    # Remove newlines and form feed characters
    y = text.replace("\n", "")
    c = y.replace("\x0c", "")
    sentence = c + " "
        # Display each letter in the sentence
    for letter in sentence:
        pattern = letter
        # Get the braille pattern for the letter
        pattern = braille_mapping.get(letter.lower(), None)
        if pattern is not None:
            # Set the GPIO pins to match the pattern
            for i in range(len(pins)):
                GPIO.output(pins[i], pattern[i])

#####
modename()
# Set up the GPIO pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pins = [2, 3, 4, 17, 27, 22]
for pin in pins:

    GPIO.setup(pin, GPIO.OUT)

    GPIO.output(pin, GPIO.LOW)

# Set up the camera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30
camera.brightness = 50
camera.contrast = 50
camera.saturation = 50
camera.rotation = 0

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

                # text = 'text not found'


        if not text.strip():
            notxt()
        if text.strip():
            language = detect(text)
            if language == "fa":
                language = "ar"
            if not language == "ar":
                language = "en"

            processing_sound()

            TTB(text)
            print(text)






cv2.destroyAllWindows()
