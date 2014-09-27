import socket, threading, logging, syslog

class WebServer(threading.Thread):

    def __init__(self,ip,port,clientsocket):
    	threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.csocket = clientsocket
        print "[+] New thread started for "+self.ip+":"+str(self.port)
############################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> SYSLOG COMMANDS <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
############################################################################################
        syslog.openlog(logoption=syslog.LOG_PID, facility=syslog.LOG_SYSLOG)
        syslog.syslog('Attacker connected')
        #if error:
        #    syslog.syslog(syslog.LOG_ERR, 'Error: when attacker attempted to connect')
        #    syslog.closelog()

    def run(self):
      #tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    	#tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    	#tcpsock.bind((host,port))
############################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> Logs COMMANDS <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
############################################################################################
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        # create a file handler
        handler = logging.FileHandler('webserver.log')
        handler.setLevel(logging.INFO)
        # create a logging format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        # add the handlers to the logger
        logger.addHandler(handler)
        #logger.info('klklkl')
    	data = self.csocket.recv(65535)
        logger.info("Client(%s:%s) sent: %s"%(self.ip, str(self.port), data))
        print "Client(%s:%s) sent : %s"%(self.ip, str(self.port), data)
        if ":8080/files/client.exe" in data:
            file = (open("client.exe", "r")).read()
            server_resp = file

        elif "loko.html" in data:
            server_resp = ("""HTTP/1.1 200 OK
Content-type: text/html; charset=UTF-8 
Server: IIS/7.0
Set-Cookie: SessionID: vdsf432l5lw21k5l3f7x3lk6f276h; S2=MNDAHSdbsaihbd4;


<!-- This Script is from www.html5freecode.com, Coded by: Kerixa Inc-->

<head>
<script>
function allowdrag(e) {
	e.stopPropagation()
	e.preventDefault()
}
function addobj(e) {
	e.stopPropagation()
	e.preventDefault()
	var files = e.dataTransfer.files;
	document.getElementById ("pr").innerHTML= "<span style='font-size: x-large'><strong>Preview:</strong></span><strong><br style='font-size: x-large'>"
	for (var i = 0; i<files.length ; i++) {
		ParseFile(files[i])
	}
	dragColor('lightgreen')
}
function ParseFile(file) {
	document.getElementById ("pr").innerHTML = document.getElementById ("pr").innerHTML+
		"<p>File information: <strong>" + file.name +
		"</strong> type: <strong>" + file.type +
		"</strong> size: <strong>" + file.size +
		"</strong> bytes</p>"
	
	if (file.type.indexOf("text") == 0) {
		var reader = new FileReader();
		reader.onload = function(e) {
		document.getElementById ("pr").innerHTML = document.getElementById ("pr").innerHTML+ 
					"<p><strong>" + file.name + ":</strong></p><pre>" +
					e.target.result.replace(/</g, "&lt;").replace(/>/g, "&gt;") +
					"</pre>"
		}
		reader.readAsText(file)
	}
	if (file.type.indexOf("image") == 0) {
		var reader = new FileReader();
		reader.onload = function(e) {
		document.getElementById ("pr").innerHTML = document.getElementById ("pr").innerHTML+
					"<p><strong>" + file.name + ":</strong><br />" +
					'<img src="' + e.target.result + '" /></p>'
		}
		reader.readAsDataURL(file)
	}

}

function dragColor(clr){
	document.getElementById('drop').style.backgroundColor= clr}

</script>
</head>

<div style="border: medium dashed blue; height: 144px; padding: 1px 4px; width: 228px; text-align: center; color: maroon; font-size: 18pt"
id="drop" ondragover="allowdrag(event)" ondrop="addobj(event)" ondragenter="dragColor('lightyellow')" ondragleave="dragColor('white')"
><br>Drag and Drop<br>
	<br>any File Here</div>
<br><div id="pr">
<span style="font-size: x-large"><strong>Preview:</strong></span><strong><br style="font-size: x-large">
	</strong></div>

<div style="text-align: center"><br><font face="Tahoma"><a target="_blank" href="http://www.html5freecode.com"><span style="font-size: 8pt; text-decoration: none">HTML5 Free Code</span></a></font></div>


""")
        elif "beard.jpeg" in data:
            file = (open("beard.jpeg", "r")).read()
            server_resp = file

        elif "auth.php?user=%27%20OR%201%20in%20(select%20@@version)%20--" in data:
            server_resp = ("""HTTP/1.1 200 OK
Content-type: text/html; charset=UTF-8
Server: IIS/7.0
Set-Cookie: SessionID: vdsf432l5lw21k5l3f7x3lk6f276h; S2=MNDAHSdbsaihbd4;

<html>
<head>
</head>
<body>
<table>
<tr>Microsoft SQL Server 2008 (SP1) - 10.0.2746.0 (X64)  Nov 9 2009 16:37:47</tr>
<tr>Copyright (c) 1988-2008 Microsoft Corporation Enterprise Edition (64-bit) on Windows NT 6.1 <X64> (Build 7600: )</tr>
</table>
</body>
</html>
""")
        elif "auth.php?user=/etc/passwd" in data:
            server_resp = ("""HTTP/1.1 200 OK
Content-type: text/html; charset=UTF-8
Server: IIS/7.0
Set-Cookie: SessionID: vdsf432l5lw21k5l3f7x3lk6f276h; S2=MNDAHSdbsaihbd4;


""")



        else:
            server_resp = ("""HTTP/1.1 200 OK
Content-type: text/html; charset=UTF-8
Server: IIS/7.0
Set-Cookie: SessionID: vdsf432l5lw21k5l3f7x3lk6f276h; S2=MNDAHSdbsaihbd4;

<html>
<head>
<title> Communications Technology Financials Inc.</title>
</head>
<body background="http://127.0.0.1:8080/beard.jpeg">

<script>
function geoFindMe() {
  var output = document.getElementById("out");

  if (!navigator.geolocation){
    output.innerHTML = "<p>Geolocation is not supported by your browser</p>";
    return;
  }

  function success(position) {
    var latitude  = position.coords.latitude;
    var longitude = position.coords.longitude;

    output.innerHTML = '<p>Latitude is ' + latitude + '<br>Longitude is ' + longitude + '</p>';
    var img = new Image();
    img.src = "http://maps.googleapis.com/maps/api/staticmap?center=" + latitude + "," + longitude + "&zoom=13&size=300x300&sensor=false";

    output.appendChild(img);
  };

  function error() {
    output.innerHTML = "Unable to retrieve your location";
  };

  output.innerHTML = "<p>Locating_</p>";

  navigator.geolocation.getCurrentPosition(success, error);
}
</script>

<p><button onclick="geoFindMe()">Show my location</button></p>
<div id="out"></div>
<br><br>
<form name="input" action="auth.php" method="get">
Username: <input type="text" name="user"><br>
Password: <input type="password" name="pwd"><br>
<input type="submit" value="Submit">



</script>
</form> 
</body>
</html>


""")
        print " [+] Connection from : " + self.ip + ":" + str(self.port)
        self.csocket.send(server_resp)
        self.csocket.close()
