#!/lusr/bin/python

#This the program for Lab 0 by Anthony Nguyen
#This project is split up into two exercises
#Exercise 0 is the Four Way Handshake
#Exercise 1 is Listening for a new connectio

#start
#setup
from socket import *
import random

#excerise 0

#create a socket(of the type SOCK_STEAM and family AF_INET) using socket()
serverName = "128.83.144.56" 					#paris.cs.utexas.edu
serverPort = 35601 								#can be 35601, 35602, or 35603
try:
	clientSocket = socket(AF_INET,SOCK_STREAM)
	print "Socket successfully created"
except socket.error as err:
	print "socket creation failed with error %s" %(err)

#Call connect() with the server's IP address () and port number() to 
#initiate a connection to the server. If unsuccessful, print out the reason
#for the error and exit
try:
	clientSocket.connect((serverName,serverPort))
	print "Socket successfully connected"
except socket.error as err:
	print "socket failed to connect because %s" %(err)

#generate a integer from 0-9000(usernum). Construct a request string using
#the server and client address information. To determine the client address
#information, the client can use the getsocketname() function
clientName  = clientSocket.getsockname()
print clientName
requestType = "ex0"
conSpec     = serverName + "-" +str(serverPort) + " " + clientName[0] + "-" +str(clientName[1])
usernum     = random.randrange(0,9000)
username    = "A.S.Nguyen"
newline     = r"\n"
request     = requestType+" "+conSpec+" "+str(usernum)+" "+username+newline

print request

#Write the client request string to the socket (using send()) 
clientSocket.send(request.encode())

#Read data from the socket (using recv()) until the SECOND newline character
#is encountered. Verfy that the first word on the second line is "OK", the 
#value of username+1, and outpit the recieve random number (servernum). If 
#word is not "OK", print an error indication and recieved string
serverReturn = clientSocket.recv(1024)
print serverReturn.decode()

#Contruct an ack string and write it to the socket (using send())

#Read data from the socket until the newline character is encountered. Verify
#that the string "OK" is recieved and output that recieved value of servernum
#if not verified, print an error indiction and the recieved string

#close the connection
clientSocket.close()

#end