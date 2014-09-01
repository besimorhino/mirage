#!/usr/bin/env python

import socket, threading

#importing modules for Options to spawn
from core.backdoor import *
from core.misc import *
from core.webserver import *
from core.ms08067 import *

clear()
logo = open("./logo/logo1.txt").read()
print logo + "\n"
options = raw_input("""\t\t[ Welcome to Mirage - the NEXT Generation Honeypost for Enterprise systems ]
\t\t\t\t[ created by @bettersaftynet & @3nc0d3r ]\n\n
Please Choose an option to load\n\n[1] Mirage Backdoor\n[2] Fake Web Server with Injection Vulns\n[3] Firewall Action(* Auto shun)\n[4] Fake port knock sequencer\n[5] Anti-ReCon\n[6]\n[7]\n[8]\nmirage> """)

host = "0.0.0.0"
port = 8888

# If statemnet for choosing Options
if options == str(1):
    # Backdoor
    tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpsock.bind((host,port))
    while True:
        tcpsock.listen(4)
        print "\nListening for incoming connections..."
        (bdclientsock, (ip, port)) = tcpsock.accept()
        bdthread = Backdoor(ip, port, bdclientsock)
        bdthread.start()

elif options == str(2):
    # Web Server
    port = 8080
    websock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    websock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    websock.bind((host,port))
    while True:
        websock.listen(4)
        print "\nListening for incoming connections..."
        (webclientsock, (ip, port)) = websock.accept()
        webthread = WebServer(ip, port, webclientsock)
        webthread.start()
elif options == str(3):
    port = 445
    mssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mssock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    mssock.bind((host,port))
    while True:
        mssock.listen(4)
        print "\nListening for incoming connections..."
        (msclientsock, (ip, port)) = mssock.accept()
        msthread = ms08067(ip, port, msclientsock)
        msthread.start()
else:
    pass




# Workable stuff
#tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#tcpsock.bind((host,port))



#while True:
#    tcpsock.listen(4)
#    print "\nListening for incoming connections..."
#    (clientsock, (ip, port)) = tcpsock.accept()
#    newthread = ClientThread(ip, port, clientsock)
#    newthread.start()
 
