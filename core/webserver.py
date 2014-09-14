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
        if "etc/passwd" in data:
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
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
bin:x:2:2:bin:/bin:/bin/sh
sys:x:3:3:sys:/dev:/bin/sh
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/bin/sh
man:x:6:12:man:/var/cache/man:/bin/sh
lp:x:7:7:lp:/var/spool/lpd:/bin/sh
mail:x:8:8:mail:/var/mail:/bin/sh
news:x:9:9:news:/var/spool/news:/bin/sh
uucp:x:10:10:uucp:/var/spool/uucp:/bin/sh
proxy:x:13:13:proxy:/bin:/bin/sh
www-data:x:33:33:www-data:/var/www:/bin/sh
backup:x:34:34:backup:/var/backups:/bin/sh
list:x:38:38:Mailing List Manager:/var/list:/bin/sh
irc:x:39:39:ircd:/var/run/ircd:/bin/sh
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh
nobody:x:65534:65534:nobody:/nonexistent:/bin/sh
libuuid:x:100:101::/var/lib/libuuid:/bin/sh
mysql:x:101:103:MySQL Server,,,:/nonexistent:/bin/false
messagebus:x:102:106::/var/run/dbus:/bin/false
colord:x:103:107:colord colour management daemon,,,:/var/lib/colord:/bin/false
usbmux:x:104:46:usbmux daemon,,,:/home/usbmux:/bin/false
miredo:x:105:65534::/var/run/miredo:/bin/false
ntp:x:106:113::/home/ntp:/bin/false
Debian-exim:x:107:114::/var/spool/exim4:/bin/false
arpwatch:x:108:117:ARP Watcher,,,:/var/lib/arpwatch:/bin/sh
avahi:x:109:118:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/bin/false
beef-xss:x:110:119::/var/lib/beef-xss:/bin/false
dradis:x:111:121::/var/lib/dradis:/bin/false
pulse:x:112:122:PulseAudio daemon,,,:/var/run/pulse:/bin/false
speech-dispatcher:x:113:29:Speech Dispatcher,,,:/var/run/speech-dispatcher:/bin/sh
haldaemon:x:114:124:Hardware abstraction layer,,,:/var/run/hald:/bin/false
iodine:x:115:65534::/var/run/iodine:/bin/false
postgres:x:116:127:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
sshd:x:117:65534::/var/run/sshd:/usr/sbin/nologin
redsocks:x:118:128::/var/run/redsocks:/bin/false
snmp:x:119:129::/var/lib/snmp:/bin/false
stunnel4:x:120:130::/var/run/stunnel4:/bin/false
statd:x:121:65534::/var/lib/nfs:/bin/false
sslh:x:122:133::/nonexistent:/bin/false
Debian-gdm:x:123:134:Gnome Display Manager:/var/lib/gdm3:/bin/false
rtkit:x:124:136:RealtimeKit,,,:/proc:/bin/false
saned:x:125:137::/home/saned:/bin/false

<img src="./smile.jpg" alt="Smiley face"> 
</form> 
</body>
</html>


""")
	elif "etc/shadow" in data:
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
root:$6$rWryW69C$9W6BQAFxJ841ccClyWcaGiJKKNJiQY6siWFQaehPGQwhAI4wFoaGbm2BbvqBpOPvkvN5zXWRmE1Rihst9Gu8e/:16316:0:99999:7:::
daemon:*:16078:0:99999:7:::
bin:*:16078:0:99999:7:::
sys:*:16078:0:99999:7:::
sync:*:16078:0:99999:7:::
games:*:16078:0:99999:7:::
man:*:16078:0:99999:7:::
lp:*:16078:0:99999:7:::
mail:*:16078:0:99999:7:::
news:*:16078:0:99999:7:::
uucp:*:16078:0:99999:7:::
proxy:*:16078:0:99999:7:::
www-data:*:16078:0:99999:7:::
backup:*:16078:0:99999:7:::
list:*:16078:0:99999:7:::
irc:*:16078:0:99999:7:::
gnats:*:16078:0:99999:7:::
nobody:*:16078:0:99999:7:::
libuuid:!:16078:0:99999:7:::
mysql:!:16078:0:99999:7:::
messagebus:*:16078:0:99999:7:::
colord:*:16078:0:99999:7:::
usbmux:*:16078:0:99999:7:::
miredo:*:16078:0:99999:7:::
ntp:*:16078:0:99999:7:::
Debian-exim:!:16078:0:99999:7:::
arpwatch:!:16078:0:99999:7:::
avahi:*:16078:0:99999:7:::
beef-xss:*:16078:0:99999:7:::
dradis:*:16078:0:99999:7:::
pulse:*:16078:0:99999:7:::
speech-dispatcher:!:16078:0:99999:7:::
haldaemon:*:16078:0:99999:7:::
iodine:*:16078:0:99999:7:::
postgres:*:16078:0:99999:7:::
sshd:*:16078:0:99999:7:::
redsocks:!:16078:0:99999:7:::
snmp:*:16078:0:99999:7:::
stunnel4:!:16078:0:99999:7:::
statd:*:16078:0:99999:7:::
sslh:!:16078:0:99999:7:::
Debian-gdm:*:16078:0:99999:7:::
rtkit:*:16078:0:99999:7:::
saned:*:16078:0:99999:7:::
<img src="./smile.jpg" alt="Smiley face">
</form> 
</body>
</html>


""")
        else:
            server_resp = ("""HTTP/1.1 200 OK
Content-type: text/html; charset=UTF-8
Server: Apache/2.1
Set-Cookie: SessionID: vdsf432l5lw21k5l3f7x3lk6f276h; S2=MNDAHSdbsaihbd4;

<html>
<head>
<title> Communications Technology Financials Inc.</title>
</head>
<body background="beard.jpeg">
<br><br>
<form name="input" action="auth.php" method="get">
Username: <input type="text" name="user"><br>
Password: <input type="password" name="pwd"><br>
<input type="submit" value="Submit">

<img src="./beard.jpeg" alt="Smiley face"> 
</form> 
</body>
</html>


""")
        print " [+] Connection from : " + self.ip + ":" + str(self.port)
        self.csocket.send(server_resp)
        self.csocket.close()
