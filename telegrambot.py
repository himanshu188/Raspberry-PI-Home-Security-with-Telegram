
# This Program will be used to send pic to Telegram by using Command "pic"
# Made by Himanshu Patel
# Email : contact@himanshuptl.me

import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO
import urllib
import requests
import pygame, sys
from pygame.locals import *
import pygame.camera
SIZE = (1280,960)
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0],SIZE)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == 'pic': 
	cam.start()
	image= cam.get_image()
	pygame.image.save(image,'tmp.jpg')
	cam.stop()
 	url = "https://api.telegram.org/bot<token>/sendPhoto";
    	files = {'photo': open('/home/pi/Telegram_bot/tmp.jpg', 'rb')}
    	data = {'chat_id' : chat_id}
    	r= requests.post(url, files=files, data=data)
    	print(r.status_code, r.reason, r.content)


bot = telepot.Bot('<Token>') # Put token from the telegram Bot
bot.message_loop(handle)
print 'I am listening...'

while 1:
     time.sleep(10)

