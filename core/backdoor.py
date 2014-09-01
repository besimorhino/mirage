import socket, threading


class Backdoor(threading.Thread):
    
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
                    break             
                else:
                    data1 = data.split(' ', 1)[0]
                    self.csocket.send ("'" + data1 + "' is not recognized as an internal or external command, operable program or batch file.\n\nC:\Users\smithr2> ")
            else:
                self.csocket.send ("'" + data1 + "' is not recognized as an internal or external command, operable program or batch file.\n\nC:\Users\smithr2> ")
        print "Client at "+self.ip+" disconnected..."