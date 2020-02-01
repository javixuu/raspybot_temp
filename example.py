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

	print 'Got command : %s' % command
        humidity, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,4)
	if command == '/hey':
		bot.sendMessage(chat_id, 'hellooou my friend')
        elif command == '/temp':
                bot.sendMessage(chat_id, 'temp = %.4f' % temp)
        else:
		bot.sendMessage(chat_id, 'sorry mate, i am stupid')

def notify():
        bot_token='1012793011:AAE-Y5p6Q6FfJWQ_6XGsVzjrLNDE64F6qcg'
        bot_chatID='401663194'
        temp = 24
        if temp > 20 : 
            send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + 'higt temp!!!'
            response=requests.get(send_text)
            print(response)
            
            
bot = telepot.Bot('1012793011:AAE-Y5p6Q6FfJWQ_6XGsVzjrLNDE64F6qcg')
bot.message_loop(handle)
print 'I am listening...'

while 1:
    print 'here...'
    notify()
    time.sleep(10)


