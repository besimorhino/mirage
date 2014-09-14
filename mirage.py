#!/usr/bin/env python

import socket, threading

#importing modules for Options to spawn
from core.backdoor import *
from core.misc import *
from core.webserver import *
from core.ms08067 import *
from core.portknocker import *
from core.devrandom import *
from core.fakeftp import *

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-b", action="store_true", dest="background", help="Launch Backdoor in the background")
parser.add_option("-l", dest="file", help="Log output to file from tools")
parser.add_option("-n", dest="verbose", help="Do Not Print Logo")
(options, args) = parser.parse_args()

clear()
logo = open("./logo/logo1.txt").read()
print logo + "\n"

options = raw_input("""\t\t[ Welcome to Mirage - the NEXT Generation Honeypost for Enterprise systems ]
\t\t\t\t[ created by @bettersaftynet & @3nc0d3r ]\n\n
Please Choose an option to load\n\n[1] Mirage Backdoor\n[2] Fake Web Server with Injection Vulns\n[3] Firewall Action(* Auto shun)\n[4] Fake port knock sequencer\n[5] Dev Random\n[6] Fake FTP Server\n[7] Anti-ReCon\n\nmirage> """)

host = "0.0.0.0"
port = 8888

# If statemnet for choosing Options
if options == str(1):
    # Backdoor --------------------------------------------------------------------------------------------------------------------
    port = 12345
    tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpsock.bind((host,port))
    while True:
        tcpsock.listen(4)
        print "\nListening for incoming connections on port %s ..." % (port)
        (bdclientsock, (ip, port)) = tcpsock.accept()
        bdthread = Backdoor(ip, port, bdclientsock)
        bdthread.start()

elif options == str(2):
    # Web Server -------------------------------------------------------------------------------------------------------------------
    port = 8080
    websock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    websock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    websock.bind((host,port))
    while True:
        websock.listen(4)
        print "\nListening for incoming connections on port %s ..." % (port)
        (webclientsock, (ip, port)) = websock.accept()
        webthread = WebServer(ip, port, webclientsock)
        webthread.start()
elif options == str(3):
    # ms08-067 --------------------------------------------------------------------------------------------------------------------
    port = 445
    mssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mssock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    mssock.bind((host,port))
    while True:
        mssock.listen(4)
        print "\nListening for incoming connections on port %s ..." % (port)
        (msclientsock, (ip, port)) = mssock.accept()
        msthread = ms08067(ip, port, msclientsock)
        msthread.start()
elif options == str(4):
    # Port Knocker -----------------------------------------------------------------------------------------------------------------
    port = 1025
    portknock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    portknock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    portknock.bind((host,port))
    while True:
        portknock.listen(4)
        print "\nListening for incoming connections on port %s ..." % (port)
        (pkclientsock, (ip, port)) = portknock.accept()
        pkthread = Portknocker(ip, port, pkclientsock)
        pkthread.start()
elif options == str(5):
    # Dev Random -------------------------------------------------------------------------------------------------------------------
    port = 37491
    devr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    devr.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    devr.bind((host,port))
    while True:
        devr.listen(4)
        print "\nListening for incoming connections on port %s ..." % (port)
        (drclientsock, (ip, port)) = devr.accept()
        drthread = Devrandom(ip, port, drclientsock)
        drthread.start()
elif options == str(6):
    # Fake FTP Server --------------------------------------------------------------------------------------------------------------
    port = 21
    fftp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    fftp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    fftp.bind((host,port))
    while True:
        fftp.listen(4)
        print "\nListening for incoming connections on port %s ..." % (port)
        (fftpclientsock, (ip, port)) = fftp.accept()
        fftpthread = FakeFTP(ip, port, fftpclientsock)
        fftpthread.start()
else:
    pass