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
	#with open("/dev/random") as f:
        #    for i in xrange(10):
        #        print f.readline()
        #        self.csocket.send(f.readline())
        while True:
            self.csocket.send(os.urandom(100000))
            time.sleep(4)
            

