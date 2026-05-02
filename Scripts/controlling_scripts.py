import RPi.GPIO as GPIO
import os
import subprocess
import time

import pygame

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pins = [2, 3, 4, 17, 27, 22]



def select_a_mode():
        pygame.mixer.pre_init(frequency=40000, buffer=64)

        pygame.mixer.init()


        pygame.mixer.music.load("/home/ibraheemt/mu_code/modenames/select_a_mode_EN.mp3")

        # Play the audio and wait for it to finish
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue

        pygame.mixer.music.load("/home/ibraheemt/mu_code/modenames/select_a_mode_AR.mp3")

        pygame.mixer.init(devicename='default')

        # Play the audio and wait for it to finish
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue

# Define a function to start a script
def start_script(combined_code):
    proc = subprocess.Popen(['python3', "/home/ibraheemt/mu_code/TTS.py"])
    return proc

# Define a function to stop a script
def stop_script(proc):
    proc.terminate()

# Example usage:
# Start a script
time.sleep(15)
c = 1
select_a_mode()
while True:
    input_state = GPIO.input(21)

    if input_state == False and c == 4:
        time.sleep(0.7)

        os.system('pkill -f "limitswitchod-backup.py"')
        stop_script(script_proc)
        print("stop")
        select_a_mode()
        c = 1
    else:
        if input_state == False and c == 1:
            for pin in pins:
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, GPIO.LOW)


            c = c+1
            os.system('pkill -f "limitswitchod-backup.py"')
            def start_script(combined_code):
                proc = subprocess.Popen(['python3', "/home/ibraheemt/mu_code/TTS.py"])
                return proc
            time.sleep(0.5)

            script_proc = start_script('/home/ibraheemt/mu_code/TTS.py')
            print("start")
            time.sleep(0.5)
        else:
            if input_state == False and c == 2:
                for pin in pins:
                    GPIO.setup(pin, GPIO.OUT)
                    GPIO.output(pin, GPIO.LOW)


                c = c+1

                stop_script(script_proc)
                def start_script(combined_code):
                    proc = subprocess.Popen(['python3', "/home/ibraheemt/mu_code/Teaching_Braille.py"])
                    return proc
                time.sleep(0.5)

                script_proc = start_script('/home/ibraheemt/mu_code/Teaching_Braille.py')
                print("start")
            else:
                if input_state == False and c == 3:
                    for pin in pins:
                        GPIO.setup(pin, GPIO.OUT)
                        GPIO.output(pin, GPIO.LOW)

                    c = 1
                    stop_script(script_proc)
                    def start_script(combined_code):


                        proc = subprocess.Popen(['python', '/home/ibraheemt/mu_code/limitswitchod-backup.py', '--weights', '/home/ibraheemt/mu_code/object detection/tfdetection', '--resolution', '640x480'])
                        return proc
                    time.sleep(0.5)

                    script_proc = start_script('/home/ibraheemt/mu_code/limitswitchod-backup.py')

                    print("start")

