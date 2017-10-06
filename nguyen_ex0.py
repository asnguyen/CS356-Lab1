#!/lusr/bin/python

#start
from socket import *				#imports the socket module
import random					#imports the random module

serverName = "128.83.144.56" 			#paris.cs.utexas.edu
serverPort = 35601 				#can be 35601, 35602, or 35603

#The following creates a TCP socket. If it fails, an error is thrown.
try:
	clientSocket = socket(AF_INET,SOCK_STREAM)
	print "Socket successfully created"
except socket.error as err:
	print "socket creation failed with error %s" %(err)

#The following creates a connection between our client and the server
#using the hostname and port defined above. If it fails, it will throw
#an error
try:
	clientSocket.connect((serverName,serverPort))
	print "Socket successfully connected"
except socket.gaierror as err:
	print "socket failed to connect because %s" %(err)

clientName  = clientSocket.getsockname()	#gets a tuple (hostname, port)

#The following defines the multiple components of the client request
requestType = "ex0"
conSpec     = serverName + "-" +str(serverPort) + " " + clientName[0] + "-" +str(clientName[1])
usernum     = random.randrange(0,9000)
username    = "A.S.Nguyen"
newline     = '\n'
request     = requestType+" "+conSpec+" "+str(usernum)+" "+username+newline

clientSocket.send(request)
print "Request Successfully Sent"

#The following reads from the socket until two newline characters are read
#After the second newline is read it checks for the OK status and creates
#an ack
newline_count = 0
while newline_count <2:
	data2 = clientSocket.recv(4096)
	if data2.endswith('\n'):		#endswith(a) returns true if 'a' is the last character in the string
		newline_count +=1
copy_data2 = data2.split()			#returns an list of the tokens split by whitespaces

if copy_data2[0] == "OK":
	clientAck = requestType+' '+str(usernum+1)+' '+str(int(copy_data2[3])+1)+newline
else:
	print "Error. Message not OK. "+data2

clientSocket.send(clientAck)
print "Ack Successfully Sent"

#The following reads the socket for a single newline character and returns
#the servernum
newline_count = 0
while newline_count <1:
	data3 = clientSocket.recv(4096)
	if data3.endswith('\n'):
		newline_count +=1
copy_data3 = data3.split()


if copy_data3[9] == "OK":
	print "\nSeversum+1 = "+copy_data3[10]
else:
	print "Error. Message not OK. "+data3

clientSocket.close()

#end
