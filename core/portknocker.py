import socket, threading


class Portknocker(threading.Thread):

    def __init__(self,ip,port,clientsocket):
    	threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.csocket = clientsocket
        print "[+] New thread started for "+self.ip+":"+str(self.port)
    def run(self):
        #tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    	#tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    	#tcpsock.bind((host,port))
    	#data = self.csocket.recv(2048)
        #print "Client(%s:%s) sent : %s"%(self.ip, str(self.port), data)
	self.csocket.send("""
************************************************
*   Viper Blood Port Knocker Sequencer v6.4.8  *
************************************************

Unauthorized personal are subject to unlawfull 
imprisionment. This system is being managed and
logged by Viper.


Please Enter Sequence: """)
        data = self.csocket.recv(2048)
        print "Client(%s:%s) sent : %s"%(self.ip, str(self.port), data)
        self.csocket.send("Port Knocking sequence is wrong and has been logged: %s \n" % (self.ip))
