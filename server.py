import sys
import socket
import random

RECV_BUFFER_SIZE = 2048
QUEUE_LENGTH = 10

def server(server_port):
    # create socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serversocket:
        #bind socket to port
        serversocket.bind((",server_port))
        serversocket.listen(QUEUE_LENGTH)
    
        while True:
            (clientsocket, address) = serversocket.accept
            if(game() == False)
                break
    pass

def main():
    # make sure they enter server port
    if len(sys.argv) != 2:
        sys.exit("Please enter the port to run the server on")
    server_port = int(sys.argv[1])
    server(server_port)

def game():
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
        