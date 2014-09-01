import socket, threading


class WebServer(threading.Thread):

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
    	data = self.csocket.recv(2048)
        print "Client(%s:%s) sent : %s"%(self.ip, str(self.port), data)

        server_resp = ("""HTTP/1.1 200 OK
Content-type: text/html; charset=UTF-8
Server: Apache/2.1
Set-Cookie: SessionID: vdsf432l5lw21k5l3f7x3lk6f276h; S2=MNDAHSdbsaihbd4;

<html>
<head>
<title> Communications Technology Financials Inc.</title>
</head>
<body bgcolor="#E6E6FA">
<br><br>
<form name="input" action="auth.php" method="get">
Username: <input type="text" name="user"><br>
Password: <input type="password" name="pwd"><br>
<input type="submit" value="Submit">

<img src="./smile.jpg" alt="Smiley face"> 
</form> 
</body>
</html>


""")
        print " [+] Connection from : " + self.ip + ":" + str(self.port)
        self.csocket.send(server_resp)
        self.csocket.close()