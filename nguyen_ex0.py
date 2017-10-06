#!/lusr/bin/python

#This the program for Lab 0 by Anthony Nguyen
#This project is split up into two exercises
#Exercise 0 is the Four Way Handshake
#Exercise 1 is Listening for a new connectio

#start
from socket import *
import random

serverName = "128.83.144.56" 			#paris.cs.utexas.edu
serverPort = 35601 				#can be 35601, 35602, or 35603
try:
	clientSocket = socket(AF_INET,SOCK_STREAM)
	print "Socket successfully created"
except socket.error as err:
	print "socket creation failed with error %s" %(err)

try:
	clientSocket.connect((serverName,serverPort))
	print "Socket successfully connected"
except socket.gaierror as err:
	print "socket failed to connect because %s" %(err)

clientName  = clientSocket.getsockname()

requestType = "ex0"
conSpec     = serverName + "-" +str(serverPort) + " " + clientName[0] + "-" +str(clientName[1])
usernum     = random.randrange(0,9000)
username    = "A.S.Nguyen"
newline     = '\n'
request     = requestType+" "+conSpec+" "+str(usernum)+" "+username+newline

clientSocket.send(request)
print "Request Successfully Sent"

data1 = clientSocket.recv(4096)
data2 = clientSocket.recv(4096)
copy_data2 = data2.split()

if copy_data2[0] == "OK":
	clientAck = requestType+' '+str(usernum+1)+' '+str(int(copy_data2[3])+1)+newline
else:
	print "Error. Message not OK. "+data2

clientSocket.send(clientAck)
print "Ack Successfully Sent"

data3 = clientSocket.recv(4096)
copy_data3 = data3.split()


if copy_data3[9] == "OK":
	print "\nSeversum+1 = "+copy_data3[10]
else:
	print "Error. Message not OK. "+data3

clientSocket.close()

#end
