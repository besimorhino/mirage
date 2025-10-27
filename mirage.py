#!/usr/bin/env python

import socket, threading, logging, os, sys

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




def clear():
    os.system("cls" if os.name == "nt" else "clear")


def log_args():
        parser = OptionParser()
        parser.add_option("-b", action="store_true", dest="background", help="[1] Mirage Linux Backdoor\n[2] Linux Fake Web Server\n[3] Windows Fake Web Server\n[4] Fake port knock sequencer\n[5] Dev Random\n[6] Fake FTP Server\n[7] Fake Telnet\n[8] Anti-ReCon\n[9] Firewall Action(* Auto shun)")
        parser.add_option("-l", dest="file", help="Log output to file from tools")
        (options, args) = parser.parse_args()
          



class aux_options:
     def __init__(self,gen_numpeople,gen_domain,gen_username,options):
          self.gen_numpeople = gen_numpeople # number of people to generate 
          self.gen_domain = gen_domain # what domain is it?
          self.gen_username = gen_username # username convention 
          self.options = options # main cntrl of choices 
          


class intro:
    @staticmethod
    def start_logging():
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
    
    
    def menu():
        while True:
            print ("""1) Create bait data [NOT YET DONE]
            2) Setup listeners [NOT YET DONE]
            3) Assign actions [NOT YET DONE]

            99) Exit Mirage
            """)
                
            aux_options.options = input("mirage> ")
            match aux_options.options: 
                    case "1":
                        aux_options.gen_numpeople = input("How many people do you want to generate? ")
                        aux_options.gen_domain =  input("What domain is it? ")
                        aux_options.gen_username = input("Username convention? ")
                    case "2":
                        aux_options.options = input("1) Telnet\n2) WebServer\n\nmirage> ")

            print("""
                    [ Mirage - the NEXT Generation Honeypost for Enterprise systems ]
                            [ created by @bettersaftynet & @3nc0d3r ]


                    [+] Welcome to Mirage, you are now in interactive configuration builder mode.

                    You will be guided through setting up your own Mirage instance.  
                    Please complete the various tasks 

                    """)


host = "0.0.0.0"
port = 8888
 

class backdoor:
    @staticmethod
    def main():
# Backdoor 
            port = 445
            tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            tcpsock.bind((host,port))
            while True:
                tcpsock.listen(4)
                print ("\nListening for incoming connections on port {0} ...").format(port)
                (bdclientsock, (ip, port)) = tcpsock.accept()
                bdthread = Backdoor(ip, port, bdclientsock)
                bdthread.start()


class webserver:
    @staticmethod
    def main():
                     # Web Server 
            port = 8080
            websock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            websock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            websock.bind((host,port))
            while True:
                websock.listen(4)
                print ("\nListening for incoming connections on port {0} ...").format(port)
                (webclientsock, (ip, port)) = websock.accept()
                webthread = WebServer(ip, port, webclientsock)
                webthread.start()


class ms08067:
    @staticmethod
    def main():
            port = 445
            mssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            mssock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            mssock.bind((host,port))
            while True:
                mssock.listen(4)
                print ("\nListening for incoming connections on port {0} ...").format(port)
                (msclientsock, (ip, port)) = mssock.accept()
                msthread = ms08067(ip, port, msclientsock)
                msthread.start()


class port_knocker:
    @staticmethod
    def main():
            port = 1025
            portknock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            portknock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            portknock.bind((host,port))
            while True:
                portknock.listen(4)
                print ("\nListening for incoming connections on port {0} ...").format(port)
                (pkclientsock, (ip, port)) = portknock.accept()
                pkthread = Portknocker(ip, port, pkclientsock)
                pkthread.start()


class dev_random:
        @staticmethod
        def main():
            port = 37491
            devr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            devr.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            devr.bind((host,port))
            while True:
                devr.listen(4)
                print ("\nListening for incoming connections on port {0} ...").format(port)
                (drclientsock, (ip, port)) = devr.accept()
                drthread = Devrandom(ip, port, drclientsock)
                drthread.start()


class fake_ftp:
        @staticmethod
        def main():
             
            port = 21
            fftp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            fftp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            fftp.bind((host,port))
            while True:
                fftp.listen(4)
                print ("\nListening for incoming connections on port {0} ...").format(port)
                (fftpclientsock, (ip, port)) = fftp.accept()
                fftpthread = FakeFTP(ip, port, fftpclientsock)
                fftpthread.start()



class fake_telnet:
     @staticmethod
     def main():
            port = 23
            ftn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ftn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            ftn.bind((host,port))
            while True:
                ftn.listen(4)
                logger.info("Telnet server is listening.")
                print ("\nListening for incoming connections on port {0} ...").format(port)
                (ftnclientsock, (ip, port)) = ftn.accept()
                ftnthread = FakeTelnet(ip, port, ftnclientsock)
                ftnthread.start()



def main():
    log_args()
    intro.start_logging()
    intro.menu()
    while True:
        try:
            match aux_options.options:
                case "1":
                    backdoor.main()
                case "2":
                    webserver.main()
                case "3":
                    ms08067.main()
                case "4":
                    port_knocker.main()
                case "5":
                    dev_random.main()
                case "6":
                    fake_ftp.main()
                case "7":
                    fake_telnet.main()
        except KeyboardInterrupt:
                sys.exit(0)
            

if __name__ == "__main__":
    main()
