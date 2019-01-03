# Kristy Li
# Professor Jie Chu
# CSCI 379-02: Computer Networking
# Project #1 - Enhanced Version Python TCP Client Program
# Due: April 4, 2018

from socket import*
serverName = 'localhost'
serverPort = 9999

def print_menu():       ## Your menu design here
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. Uppercase"
    print "2. Lowercase"
    print "3. Titlecase"
    print "4. Reverse each word"
    print "5. Reverse the entire sentence"
    print 67 * "-"

clientSocket = socket(AF_INET, SOCK_STREAM) #create TCP socket for server, remote port 9999
clientSocket.connect((serverName, serverPort))

sentence = raw_input("\nPlease enter a sentence to modify. The sentence to modify is: ") #no need to attach server name, port
print_menu()
command = raw_input("\nEnter a choice: ")
clientSocket.send(sentence)
clientSocket.send(command)
modifiedSentence = clientSocket.recv(1024)
print "\nFrom Server, the modified sentence is: ", modifiedSentence
clientSocket.close()



