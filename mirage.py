#!/usr/bin/env python

import socket, threading, logging

#importing modules for Options to spawn
from core.backdoor import *
from core.misc import *
from core.webserver import *
from core.ms08067 import *
from core.portknocker import *
from core.devrandom import *
from core.fakeftp import *
from core.faketelnet import *
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-b", action="store_true", dest="background", help="[1] Mirage Linux Backdoor\n[2] Linux Fake Web Server\n[3] Windows Fake Web Server\n[4] Fake port knock sequencer\n[5] Dev Random\n[6] Fake FTP Server\n[7] Fake Telnet\n[8] Anti-ReCon\n[9] Firewall Action(* Auto shun)")
parser.add_option("-l", dest="file", help="Log output to file from tools")
(options, args) = parser.parse_args()

############################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> LOGGING  COMMANDS <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
############################################################################################
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler

handler = logging.FileHandler('mirageserver.log')
handler.setLevel(logging.INFO)

# create a logging format

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger

logger.addHandler(handler)

logger.info('[+] Mirage Server has started.....')


clear()

print "No config file detected, nor were CLI args used, entering interactive mode."

print("""
[ Mirage - the NEXT Generation Honeypost for Enterprise systems ]
         [ created by @bettersaftynet & @3nc0d3r ]


[+] Welcome to Mirage, you are now in interactive configuration builder mode.

You will be guided through setting up your own Mirage instance.  
Please complete the various tasks 

""")

gen_numpeople = 0
gen_domain = ""
gen_username = ""

host = "0.0.0.0"
port = 8888

while True:
    print ("""1) Create bait data [NOT YET DONE]
2) Setup listeners [NOT YET DONE]
3) Assign actions [NOT YET DONE]

99) Exit Mirage
""")
    options = raw_input("mirage> ")
    if options == "1":
        gen_numpeople = raw_input("How many people do you want to generate? ")
        gen_domain =  raw_input("What domain is it? ")
        gen_username = raw_input("Username convention? ")
    elif options == "2":
        options = raw_input("1) Telnet\n2) WebServer\n\nmirage> ")
        # If statemnet for choosing Options
        ############################################################################################
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> OPTIONS <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        ############################################################################################

        if options == str(1):
            # Backdoor --------------------------------------------------------------------------------------------------------------------
            port = 445
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
        elif options == str(7):
            # Fake Telnet Server -----------------------------------------------------------------------------------------------------------
            port = 23
            ftn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ftn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            ftn.bind((host,port))
            while True:
                ftn.listen(4)
                logger.info("Telnet server is listening.")
                print "\nListening for incoming connections on port %s ..." % (port)
                (ftnclientsock, (ip, port)) = ftn.accept()
                ftnthread = FakeTelnet(ip, port, ftnclientsock)
                ftnthread.start()
        else:
            pass

