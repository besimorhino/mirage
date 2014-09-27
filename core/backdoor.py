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
############################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> LOGGER COMMANDS <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
############################################################################################
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        # create a file handler
        handler = logging.FileHandler('Backdoor.log')
        handler.setLevel(logging.INFO)
        # create a logging format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        # add the handlers to the logger
        logger.addHandler(handler)
        logger.info('DOIT')

        data = "dummydata"
        data1 = ""
        datas = ""

        while len(data):
            print "Client(%s:%s) sent : %s"%(self.ip, str(self.port), data)
            #self.csocket.send("You sent me : "+data)
            datas = data.rstrip()
            if datas in comm:
                if datas == 'ls':
                    self.csocket.send("smith@smith01-PC:$ ")
                elif datas == "":
                    self.csocket.send("C:\Users\smithr2> ")
                elif datas == 'cd':
                    self.csocket.send("Access is denied.\n\nc:\Users\smithr2>")
                elif datas == 'exit':
                    self.csocket.close()
                else:
                    data1 = data.split(' ', 1)[0]
                    self.csocket.send ("'" + data1 + dates + data + "' is not recognized as an internal or external command, operable program or batch file.\n\nC:\Users\smithr2> ")
            else:
                self.csocket.send (("'" + data.split(' ', 1)[0]).rstrip('\n') + "' is not recognized as an internal or external command, operable program or batch file.\n\nC:\Users\smithr2> ")
        print "Client at "+self.ip+" disconnected..."
