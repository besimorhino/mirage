import socket, threading, time


class FakeTelnet(threading.Thread):

    def __init__(self,ip,port,clientsocket):
    	threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.csocket = clientsocket
        print "[+] New thread started for "+self.ip+":"+str(self.port)
    
    def run(self):
        self.csocket.recv(65535)
        time.sleep(3)
        self.csocket.send("Welcome to Microsoft Telnet Service\n\n")
        count = 0
        while count < 3:
            username = ""
            while username.rstrip() == "":
                self.csocket.send("login: ")
                username = self.csocket.recv(65535)
            self.csocket.send("password: ")
            password = self.csocket.recv(65535)
            self.csocket.send("\n")
            print "Client(%s:%s) sent : username: %s password: %s\n" % (self.ip, str(self.port), username, password)
	    
            if (username.rstrip() == "smithr2" and password.rstrip() == "adama"):
                count = 3
                self.csocket.send("""
*===============================================================
Microsoft Telnet Server.
*===============================================================""")


                self.csocket.send("\nMicrosoft Windows [Version 6.1.7601] \nCopyright (c) 2009 Microsoft Corperation. All rights reserved. \n\nC:\Users\smithr2> ")
                comm = ['dir', 'net use', '', 'ipconfig']

                data = "dummydata"
                data1 = ""
                datas = ""
                while len(data):
                    data = self.csocket.recv(2048)
                    print "Client(%s:%s) sent : %s"%(self.ip, str(self.port), data)
                    #self.csocket.send("You sent me : "+data)
                    datas = data.rstrip()
                    if datas in comm:
                        if datas == 'dir':
                            self.csocket.send(" Volume in drive C has no label.\n Volume Serial Number is 932B-6544\n\n Directory of C:\Users\smithr2\n\n03/12/2014\t10:56 PM\t <DIR>\t\t.\n03/12/2014\t10:56 PM\t <DIR>\t\t..\n03/12/2014\t10:56 PM\t <DIR>\t\tpassword.txt\n03/12/2014\t10:56 PM\t <DIR>\t\t2014-Finacials.xls\n\nC:\Users\smithr2> ")
                        elif datas == "":
                            self.csocket.send("C:\Users\smithr2> ")
                        elif datas == 'cd':
                            self.csocket.send("Access is denied.\n\nc:\Users\smithr2>")
                        elif datas == 'exit':
                            self.csocket.close()
			elif datas == 'ipconfig':
                            self.csocket.send("""
Windows IP Configuration


Ethernet adapter Bluetooth Network Connection:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Ethernet adapter Local Area Connection:

   Connection-specific DNS Suffix  . :
   IPv4 Address. . . . . . . . . . . : 172.16.111.12
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 172.16.111.2

Tunnel adapter isatap.{A88EC8A0-1FD3-4691-AA5A-D8BD18FA4D20}:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Tunnel adapter Local Area Connection* 11:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Tunnel adapter isatap.{D9732E65-1C0A-4A80-B5CD-1B1BDC354418}:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :


""")
                        elif datas == 'ipconfig /all':
                            pass
                        else:
                            pass
                            #data1 = data.split(' ', 1)[0]
                            #self.csocket.send ("'" + data1 + dates + data + "' is not recognized as an internal or external command, operable program or batch file.\n\nC:\Users\smithr2> ")
                    else:
                        self.csocket.send (("'" + datas.split(' ', 1)[0]).rstrip('\n') + "' is not recognized as an internal or external command, operable program or batch file.\n\nC:\Users\smithr2> ")

            else:
                self.csocket.send("\nThe handle is invalid.\n\nLogin Failed\n\n")
                count = count +1
        self.csocket.close() 
