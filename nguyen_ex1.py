#!/lusr/bin/python

#start
from socket import *				#imports the socket module
import random					#imports the random module

serverName = "128.83.144.56" 			#paris.cs.utexas.edu
serverPort = 35601 				#can be 35601, 35602, or 35603

#The following creates a TCP socket. If it fails, an error is thrown
try:
	clientSocket = socket(AF_INET,SOCK_STREAM)
	print "Client Socket successfully created"
except socket.error as err:
	print "socket creation failed with error %s" %(err)

#The following creates a TCP socket that will be used for listening
try:
	psock = socket(AF_INET, SOCK_STREAM)
	print "Listening Socket successfully created"
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

clientName  = clientSocket.getsockname()		#gets a tuple (hostname,port)
psock.bind((clientName[0],clientName[1]+1))		#binds psock to a port that is 1 more than the port that the client is using
print "PSock has successfully binded to a port"

psockName = psock.getsockname()				#gets a tuple (hostname,port)
print psockName
psock.listen(0)						#psock begins to listen to any connection. The 0 refers to the maximum number of backlog connections allow (we will allowed zero backlogs)

#The following defines the multiple components of the request
requestType = "ex1"
conSpec     = serverName + "-" +str(serverPort) + " " + clientName[0] + "-" +str(psockName[1])
usernum     = random.randrange(0,9000)
username    = "A.S.Nguyen"
newline     = '\n'
request     = requestType+" "+conSpec+" "+str(usernum)+" "+username+newline

clientSocket.send(request)
print "Request Successfully Sent"

#The following reads from the socket until two newline characters are read
#After the second newline is read it checks for the OK status
newline_count = 0
while newline_count <2:
	data2 = clientSocket.recv(4096)
	if data2.endswith('\n'):
		newline_count +=1
copy_data2 = data2.split()

if copy_data2[0] == "OK":
	clientAck = requestType+' '+str(usernum+1)+' '+str(int(copy_data2[3])+1)+newline
	servernum = int(copy_data2[3])
else:
	print "Error. Message not OK. "+data2

#accopt() tells the socket to accept connections and it will return a tuple
newsock = psock.accept()			#returns a tuple (socketObj, host)
print "PSock is accepting new connections"

#The following reads from our new socket for a single newline character and returns he new server number
newline_count = 0
while newline_count <1:
	data3 = newsock[0].recv(4096)
	if data3.endswith('\n'):
		newline_count +=1
copy_data3 = data3.split()

if copy_data3[1] != "NONE":
	print "CS 356 server sent "+copy_data3[4]
	new_req = str(servernum+1)+" "+str(int(copy_data3[4])+1)+newline
	newsock[0].send(new_req)
	psock.close()
else:
	psock.close()

data4 = clientSocket.recv(4096)
print data4

clientSocket.close()

#end
