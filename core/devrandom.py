import socket, threading, os, time


class Devrandom(threading.Thread):

    def __init__(self,ip,port,clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.csocket = clientsocket
        print "[+] New thread started for " + self.ip + ":" + str(self.port)


    def run(self):
        print "Connection from : "+self.ip+":"+str(self.port)
        try:
            while True:
                self.csocket.send(os.urandom(100000))
                time.sleep(4)
        except:
            print "[-] Thread %s on port %s has disconnected! \n" % (self.ip, self.port)
