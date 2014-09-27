import socket, threading, os, time


class FakeFTP(threading.Thread):

    def __init__(self,ip,port,clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.csocket = clientsocket
        print "[+] New thread started for " + self.ip + ":" + str(self.port)


    def run(self):
        try:

            print "Connection from : "+self.ip+":"+str(self.port)
            self.csocket.send("220 ProFTPD 1.2.4 Server (ProFTPD)\n")
            data = self.csocket.recv(1024)
            print "Username: %s" %(data)
            self.csocket.send("331 Password required for anonymous.\n")
            data = self.csocket.recv(2048)
            print "Password: %s\n" %(data)
            self.csocket.send("230 User anonymous logged in.\n")
            while True:
                data = self.csocket.recv(2048)
                print "[+] Connection from %s on port %s wrote: %s" % (self.ip, self.port, data) 
                if data.rstrip() == "PWD":
                    self.csocket.send('257 "/users/anonymous" is current directory.\n')
                elif data.rstrip() == "SYST":
                    self.csocket.send("215 UNIX Type: L8 Version: BSD-44\n")
                elif data.rstrip() == "FEAT":
                    self.csocket.send("211-Extensions supported\n211 End\n")
                elif data.rstrip() == "TYPE I":
                    self.csocket.send("501 Extensions supported\n")
                elif data.rstrip() == "PORT":
                    self.csocket.send("501 Extensions supported\n")
                elif data.rstrip() == "EPSV":
                    self.csocket.send("229 Entering Extended Passive Mode (|||34348|)")
                else:
                    self.csocket.send("501 Not valid")
        except:
            print "[-] Connection from %s on port %s has disconnected." % (self.ip, self.port)
        #self.csocket.send("Connected\n")
        #self.csocket.send("Retrieving directory listing...\n")
        
