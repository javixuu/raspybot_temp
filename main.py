from mq2 import *
import sys
import time
import random
import datetime
import telepot
import Adafruit_DHT
import requests


def handle(msg):
	chat_id = msg['chat']['id']
	command = msg['text']

	print ('Got command : %s' % command)
	if command == '/hey':
		bot.sendMessage(chat_id, "LPG: %g ppm, CO: %g ppm, Smoke: %g ppm" % (perc["GAS_LPG"], perc["CO"], perc["SMOKE"]))
	elif command == '/temp':
		bot.sendMessage(chat_id, 'temp = %.4f' % temp)
	else:
		bot.sendMessage(chat_id, 'sorry mate, i am stupid')

def notify():
	bot_token='1012793011:AAE-Y5p6Q6FfJWQ_6XGsVzjrLNDE64F6qcg'
	bot_chatID='401663194'
	if temp > 35:
		send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + 'higt temp!!!'
		response=requests.get(send_text)
		print(response)
	if perc["CO"] > 1:
		send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + 'CO > 1!!!'
		response=requests.get(send_text)
		print(response)
	if perc["SMOKE"]>1:
		send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + 'Posible fuego!!!'
		response=requests.get(send_text)
		print(response)


bot = telepot.Bot('1012793011:AAE-Y5p6Q6FfJWQ_6XGsVzjrLNDE64F6qcg')
bot.message_loop(handle)
bot_token='1012793011:AAE-Y5p6Q6FfJWQ_6XGsVzjrLNDE64F6qcg'
bot_chatID='401663194'
send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + 'Started, sensors ready in 30 sec'
response=requests.get(send_text)
print(response)

mq = MQ();
send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + 'SENSORS READY'
response=requests.get(send_text)
print(response)
global temp
global perc
while 1:
	print ('here...')
	perc = mq.MQPercentage()
	humidity, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22,4)
	notify()
	time.sleep(10)
