import socket, threading, time, logging, syslog, getpass
from tncommands import *


class FakeTelnet(threading.Thread):

    def __init__(self,ip,port,clientsocket):
    	threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.csocket = clientsocket
        #self.systemname = systemname
        #self.telnetuname = telnetuname
        #slef.telnetpassword = telnetpassword
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
############################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> LOGGER COMMANDS <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
############################################################################################
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        # create a file handler
        handler = logging.FileHandler('FakeTelnet.log')
        handler.setLevel(logging.INFO)
        # create a logging format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        # add the handlers to the logger
        logger.addHandler(handler)
        #logger.info('DOIT')

############################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> CLIENT LOGIN <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
############################################################################################
        self.csocket.recv(65535)
        time.sleep(3)
        self.csocket.send("Welcome to Microsoft Telnet Service\n\n")
        count = 0
        while count < 3:
            username = ""
            while username.rstrip() == "":
                self.csocket.send("login: ")
                username = self.csocket.recv(65535)
                logger.info("Client(%s:%s) USERNAME: %s"%(self.ip, str(self.port), username))
            self.csocket.send("password: ")
            password = self.csocket.recv(65535)

            logger.info("Client(%s:%s) PASSWORD %s"%(self.ip, str(self.port), username))
            self.csocket.send("\n")

############################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> PASSWORD CRITERA <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
############################################################################################
            print "Client(%s:%s) sent : username: %s password: %s\n" % (self.ip, str(self.port), username, password)
	    
            if (username.rstrip() == "smithr2" and password.rstrip() == "adama"):
                count = 3
                logger.info("Client(%s:%s) [+] Authenticated...."%(self.ip, str(self.port)))
                self.csocket.send("""
*===============================================================
Microsoft Telnet Server.
*===============================================================""")

############################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> First string COMMANDS <~~~~!~~~~~~~~~~~~~~~~~~~~~~~~~~#
############################################################################################
                self.csocket.send("\nMicrosoft Windows [Version 6.1.7601] \nCopyright (c) 2009 Microsoft Corperation. All rights reserved. \n\nC:\Users\smithr2> ")
                comm = ['dir', 'net', 'cd', 'ipconfig', 'find', 'dir' ,'type', 'net', 'ping', 'telnet']

                data = "dummydata"
                data1 = ""
                datas = ""
                while len(data):

                    data = self.csocket.recv(2048)
                    logger.info("Client(%s:%s) sent : %s"%(self.ip, str(self.port), data))
                    print "Client(%s:%s) sent : %s"%(self.ip, str(self.port), data)
                    #self.csocket.send("You sent me : "+data)
                    datas = data.rstrip()
                    if (datas.split(' ', 1)[0]).rstrip() in comm:
############################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> DIR COMMANDS <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
############################################################################################
                        if datas == 'dir':
                            self.csocket.send(" Volume in drive C has no label.\n Volume Serial Number is 932B-6544\n\n Directory of C:\Users\smithr2\n\n03/12/2014\t10:56 PM\t <DIR>\t\t.\n03/12/2014\t10:56 PM\t <DIR>\t\t..\n03/12/2014\t10:56 PM\t      \t\tpasswords.txt\n03/12/2014\t10:56 PM\t      \t\t2014-Finacials.xls\n\nC:\Users\smithr2> ")
############################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> EMPTY COMMANDS <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
############################################################################################
                        elif datas == "":
                            self.csocket.send("C:\Users\smithr2> ")
############################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> TYPE COMMANDS <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
############################################################################################
                        elif (datas.split(' ', 1)[0]).rstrip() == "type":
                            if datas == "type passwords.txt":
                                self.csocket.send("Fin xls password - Amber123!!\nLogin - smithr2, adama\n10.1.1.142, 22 - Badgers147, $21gT1al!!\n\nc:\Users\smithr2>")
                            elif datas == "type":
                                self.csocket.send("The syntax of the command is incorrect.\n\n")
                            else:
                                self.csocket.send("System cannot find the file specified.\n\n")
############################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> CD COMMANDS <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
############################################################################################
                        elif datas == 'cd':
                            self.csocket.send("Access is denied.\n\nc:\Users\smithr2>")
############################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> EXIT COMMANDS <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
############################################################################################
                        elif datas == 'exit':
                            self.csocket.close()

############################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> IPCONFIG COMMANDS <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
############################################################################################
                        elif (datas.split(' ', 1)[0]).rstrip() == "ipconfig":
                            if datas == 'ipconfig':
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


c:\Users\smithr2> """)
############################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> IPCONFIG COMMANDS <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
############################################################################################
                            elif datas == 'ipconfig /all' :
                                self.csocket.send("""

Windows IP Configuration

   Host Name . . . . . . . . . . . . : Laptop-smithr2-PC
   Primary Dns Suffix  . . . . . . . :
   Node Type . . . . . . . . . . . . : Hybrid
   IP Routing Enabled. . . . . . . . : No
   WINS Proxy Enabled. . . . . . . . : No

Ethernet adapter Bluetooth Network Connection:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Bluetooth Device (Personal Area Network)
   Physical Address. . . . . . . . . : E4-CE-8F-0F-E2-85
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes

Ethernet adapter Local Area Connection:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Intel(R) PRO/1000 MT Network Connection
   Physical Address. . . . . . . . . : 00-0C-29-B0-4A-B2
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   IPv4 Address. . . . . . . . . . . : 172.16.111.160(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 172.16.111.2
   NetBIOS over Tcpip. . . . . . . . : Enabled

Tunnel adapter isatap.{A88EC8A0-1FD3-4691-AA5A-D8BD18FA4D20}:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Microsoft ISATAP Adapter
   Physical Address. . . . . . . . . : 00-00-00-00-00-00-00-E0
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes

Tunnel adapter Local Area Connection* 11:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Teredo Tunneling Pseudo-Interface
   Physical Address. . . . . . . . . : 00-00-00-00-00-00-00-E0
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes

Tunnel adapter isatap.{D9732E65-1C0A-4A80-B5CD-1B1BDC354418}:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Microsoft ISATAP Adapter #2
   Physical Address. . . . . . . . . : 00-00-00-00-00-00-00-E0
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes

c:\Users\smithr2> """)

                            else:
                                self.csocket.send("""

Error: unrecognized or incomplete command line.

USAGE:
    ipconfig [/allcompartments] [/? | /all |
                                 /renew [adapter] | /release [adapter] |
                                 /renew6 [adapter] | /release6 [adapter] |
                                 /flushdns | /displaydns | /registerdns |
                                 /showclassid adapter |
                                 /setclassid adapter [classid] |
                                 /showclassid6 adapter |
                                 /setclassid6 adapter [classid] ]

where
    adapter             Connection name
                       (wildcard characters * and ? allowed, see examples)

    Options:
       /?               Display this help message
       /all             Display full configuration information.
       /release         Release the IPv4 address for the specified adapter.
       /release6        Release the IPv6 address for the specified adapter.
       /renew           Renew the IPv4 address for the specified adapter.
       /renew6          Renew the IPv6 address for the specified adapter.
       /flushdns        Purges the DNS Resolver cache.
       /registerdns     Refreshes all DHCP leases and re-registers DNS names
       /displaydns      Display the contents of the DNS Resolver Cache.
       /showclassid     Displays all the dhcp class IDs allowed for adapter.
       /setclassid      Modifies the dhcp class id.
       /showclassid6    Displays all the IPv6 DHCP class IDs allowed for adapter.
       /setclassid6     Modifies the IPv6 DHCP class id.


The default is to display only the IP address, subnet mask and
default gateway for each adapter bound to TCP/IP.

For Release and Renew, if no adapter name is specified, then the IP address
leases for all adapters bound to TCP/IP will be released or renewed.

For Setclassid and Setclassid6, if no ClassId is specified, then the ClassId is removed.

Examples:
    > ipconfig                       ... Show information
    > ipconfig /all                  ... Show detailed information
    > ipconfig /renew                ... renew all adapters
    > ipconfig /renew EL*            ... renew any connection that has its
                                         name starting with EL
    > ipconfig /release *Con*        ... release all matching connections,
                                         eg. "Local Area Connection 1" or
                                             "Local Area Connection 2"
    > ipconfig /allcompartments      ... Show information about all
                                         compartments
    > ipconfig /allcompartments /all ... Show detailed information about all
                                         compartments

c:\Users\smithr2> """)

############################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> NET COMMANDS <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
############################################################################################

                        elif (datas.split(' ', 1)[0]).rstrip() == "net":
                            if datas == "net user":
                                self.csocket.send("""
User accounts for \\Laptop-smithr2-PC

-------------------------------------------------------------------------------
Administrator            Guest                    smithr2
test                     admin-user
The command completed successfully.

c:\Users\smithr2> """)
                            elif datas == "net localgroup":
                                self.csocket.send("""

Aliases for \\Laptop-smithr2-PC

-------------------------------------------------------------------------------
*Administrators
*Backup Operators
*Cryptographic Operators
*Distributed COM Users
*Event Log Readers
*Guests
*HomeUsers
*IIS_IUSRS
*Network Configuration Operators
*Performance Log Users
*Performance Monitor Users
*Power Users
*Remote Desktop Users
*Replicator
*TelnetClients
*Users
The command completed successfully.

c:\Users\smithr2> """)
                            elif datas == "net localgroup Administrators":
                                self.csocket.send("""
Alias name     Administrators
Comment        Administrators have complete and unrestricted access to the computer/domain

Members

-------------------------------------------------------------------------------
Administrator
admin-user
The command completed successfully.


c:\Users\smithr2> """)

                            elif datas == "net localgroup dd":
                                self.csocket.send("""

c:\Users\smithr2> """)

#Cryptographic Operators
#Distributed COM Users
#Event Log Readers
#Guests
#HomeUsers
#IIS_IUSRS
#Network Configuration Operators
#Performance Log Users
#Performance Monitor Users
#Power Users
#Remote Desktop Users
#Replicator
#TelnetClients
#Users


                            elif datas == 'net localgroup "Backup Operators"':
                                self.csocket.send("""
Alias name     Backup Operators
Comment        Backup Operators can override security restrictions for the sole purpose of backing up or restoring files

Members

-------------------------------------------------------------------------------
The command completed successfully.


c:\Users\smithr2> """)

                            elif datas == 'net localgroup "Cryptographic Operators"':
                                self.csocket.send("""

c:\Users\smithr2> """)

                            elif datas == 'net localgroup "Distributed COM Users"':
                                self.csocket.send("""

c:\Users\smithr2> """)

                            elif datas == 'net localgroup "Event Log Readers"':
                                self.csocket.send("""

c:\Users\smithr2> """)
                            elif datas == "net group":
                                self.csocket.send("""
This command can be used only on a Windows Domain Controller.

More help is available by typing NET HELPMSG 3515.


c:\Users\smithr2> """)
                            elif datas == "net use":
                                self.csocket.send("""
New connections will be remebered.

There are no entries in the list.


c:\Users\smithr2> """)
                            else:
                                self.csocket.send("""
The syntax of this command is:

NET
    [ ACCOUNTS | COMPUTER | CONFIG | CONTINUE | FILE | GROUP | HELP |
      HELPMSG | LOCALGROUP | PAUSE | SESSION | SHARE | START |
      STATISTICS | STOP | TIME | USE | USER | VIEW ]
c:\Users\smithr2> """)
############################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> PING COMMANDS <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
############################################################################################
                        elif (datas.split(' ', 1)[0]).rstrip() == "ping":
                            if datas == "ping 10.1.1.1":
                                self.csocket.send("/nPinging 127.0.0.1 with 32 bytes of data:\n")
                                time.sleep(1)
                                self.csocket.send("Reply from 127.0.0.1: bytes=32 time<1ms TTL=128\n")
                                time.sleep(1)
                                self.csocket.send("Reply from 127.0.0.1: bytes=32 time<1ms TTL=128\n")
                                time.sleep(1)
                                self.csocket.send("Reply from 127.0.0.1: bytes=32 time<1ms TTL=128\n")
                                time.sleep(1)
                                self.csocket.send("Reply from 127.0.0.1: bytes=32 time<1ms TTL=128\n\n")
                                self.csocket.send("""Ping statistics for 127.0.0.1:
    Packets: Sent = 4, Received = 4, Lost = 0 (0\% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms

C:\Users\smithr2> """)
                            elif datas == "ping":
                                self.csocket.send("""

Usage: ping [-t] [-a] [-n count] [-l size] [-f] [-i TTL] [-v TOS]
            [-r count] [-s count] [[-j host-list] | [-k host-list]]
            [-w timeout] [-R] [-S srcaddr] [-4] [-6] target_name

Options:
    -t             Ping the specified host until stopped.
                   To see statistics and continue - type Control-Break;
                   To stop - type Control-C.
    -a             Resolve addresses to hostnames.
    -n count       Number of echo requests to send.
    -l size        Send buffer size.
    -f             Set Don't Fragment flag in packet (IPv4-only).
    -i TTL         Time To Live.
    -v TOS         Type Of Service (IPv4-only. This setting has been deprecated
                   and has no effect on the type of service field in the IP Head
    -r count       Record route for count hops (IPv4-only).
    -s count       Timestamp for count hops (IPv4-only).
    -j host-list   Loose source route along host-list (IPv4-only).
    -k host-list   Strict source route along host-list (IPv4-only).
    -w timeout     Timeout in milliseconds to wait for each reply.
    -R             Use routing header to test reverse route also (IPv6-only).
    -S srcaddr     Source address to use.
    -4             Force using IPv4.
    -6             Force using IPv6.

C:\Users\smithr2> """)
                            else:
                                self.csocket.send("""

Ping request could not find host """ + (datas.split(' ', 1)[1]).rstrip() + """. Please check the name and try again.
C:\Users\smithr2> """)
                                

                        else:
                            data1 = data.split(' ', 1)[0]
                            self.csocket.send ("Access is denied.\n\nC:\Users\smithr2> ")
                    elif datas == "":
                        self.csocket.send("C:\Users\smithr2> ")
                    else:
                        self.csocket.send (("'" + datas.split(' ', 1)[0]).rstrip('\n') + "' is not recognized as an internal or external command, operable program or batch file.\n\nC:\Users\smithr2> ")
                        #self.csocket.send("Access is denied.\n\nc:\Users\smithr2>")
            else:
                self.csocket.send("\nThe handle is invalid.\n\nLogin Failed\n\n")
                count = count +1
        self.csocket.close() 
