import sys
import socket
import random
import threading

RECV_BUFFER_SIZE = 2048
QUEUE_LENGTH = 10

def server(clientsocket):
    while True:        
        if(game(clientsocket) == False)
            break
    pass

def main():
    # make sure they enter server port
    if len(sys.argv) != 2:
        sys.exit("Please enter the port to run the server on")
    server_port = int(sys.argv[1])

    # Create server socket
    serversocket = socket(AF_INET, SOCK_STREAM)
    serversocket.bind((",server_port))
    serversocket.listen(QUEUE_LENGTH)
    
    # Listen for connections
    while 1:
        (clientsocket, address) = serversocket.accept()
        # If a client connects, run the server() function to start game 
        threading.Thread(target = server, args = (clientsocket)).start()

def game(clientsocket):
    int randNum = random.randint(0, 1000)
    int guess = -1
    int guessCount = 0

    # SEND STARTING MESSAGE
    while(guess != randNum):
        # INPUT NEW GUESS FROM CLIENT AND VALIDATE IT
        guessCount += 1
        if guess == randNum:
            break
        elif guess > randNum:
            # SEND GUESS IS TOO HIGH MESSAGE
        else:
            # SEND GUESS IS TOO LOW MESSAGE
    
    # SEND VICTORY MESSAGE AND GUESS COUNT
    # INPUT WHETHER THE PLAYER WANTS TO PLAY AGAIN
    
    if(): #PLAYER DOES NOT WANT TO START AGAIN
        return False
    else(): # PLAYER WANTS TO START AGAIN
        return True

if__name__ == "__main__":
    main()
        