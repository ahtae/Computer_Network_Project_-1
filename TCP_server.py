# Kristy Li
# Professor Jie Chu
# CSCI 379-02: Computer Networking
# Project #1 - Enhanced Version Python TCP Server Program
# Due: April 4, 2018

from socket import*

serverPort = 9999
serverSocket = socket(AF_INET, SOCK_STREAM) #create TCP welcoming socket
serverSocket.bind(('localhost', serverPort))
serverSocket.listen(1) #server begins listening for incoming TCP requests

print 'The Server is ready to receive.'

while 1: #loop forever
     connectionSocket, addr = serverSocket.accept() #server waits on accept() for incoming requests, new socket created on return

     sentence = connectionSocket.recv(1024) #read bytes from socket (but not address as in UDP)
     command = connectionSocket.recv(1024) #read bytes from socket (but not address as in UDP)

     print("Received {} from {}:{}".format(sentence, addr[0], addr[1]))
          
     if(command == "1"):
          capitalizedSentence = sentence.upper()
          connectionSocket.send(capitalizedSentence)
     elif(command == "2"):
          uncapitalizedSentence = sentence.lower()
          connectionSocket.send(uncapitalizedSentence)
     elif(command== "3"):
          titledSentence = sentence.title()
          connectionSocket.send(titledSentence)
     elif(command == "4"):
         reversedSentence = ' '.join(reversed(sentence.split()))
         connectionSocket.send(reversedSentence)
     elif(command == "5"):
         reversedEachWordSentence = ' '.join(word[::-1] for word in sentence.split())
         connectionSocket.send(reversedEachWordSentence)
     else:
          connectionSocket.send("Sorry. Command is not an option.")

     connectionSocket.close() #close connection to this client (but not welcoming socket)
