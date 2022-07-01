#!/usr/bin/env python
#---------------------------------------------------------------------|
#  Matheus Martins 3mhenrique@gmail.com
#  https://github.com/mateuscomh/raspberryPowerButton
#  30/03/2021 v1.7  GPL3
#  Config and enable phisical power switch button.
#---------------------------------------------------------------------|
##colocar função para serviço - enable

#-----Import libs 
import RPi.GPIO as GPIO #Lib das GPIO
import time #Lib temporizador
import os #Lib comandos sistema

#----Setup GPIO, defines interruptor
GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#-----timer power off  and mensage for all terminals active
def Shutdown(channel):
    os.system("wall shuting down in 5 secs...")
    time.sleep(5)
    os.system("sudo shutdown -h now")

#----fails, call again 
GPIO.add_event_detect(7, GPIO.FALLING, callback=Shutdown, bouncetime=2000)
while 1:
    time.sleep(1)
