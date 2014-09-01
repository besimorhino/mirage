import socket, threading


class ms08067(threading.Thread):
    
    def __init__(self,ip,port,clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.csocket = clientsocket
        print "[+] New thread started for " + self.ip + ":" + str(self.port)
    
    
    def run(self):    
        print "Connection from : "+self.ip+":"+str(self.port)
        self.csocket.send("\nMicrosoft Windows [Version 6.1.7601] \nCopyright (c) 2009 Microsoft Corperation. All rights reserved. \n\nC:\Users\smithr2> ")
        comm = ['dir', 'net use', '', 'ipconfig']
        
        data = "dummydata"
        data1 = ""
        datas = ""
        while len(data):
            data = self.csocket.recv(2048)
            print "Client(%s:%s) sent : %s"%(self.ip, str(self.port), data)
            self.csocket.send("You sent me : "+data)
            datas = data.rstrip()
        print "Client at "+self.ip+" disconnected..."
