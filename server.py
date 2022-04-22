import socketserver
import sys
import socket
import random
import threading

RECV_BUFFER_SIZE = 2048
QUEUE_LENGTH = 10

def server(clientsocket):
    while True:        
        if(game(clientsocket) == False):
            break
    pass

def main():

    server_port = 15000

    # Create server socket
    serversocket = socket(AF_INET, SOCK_STREAM)
    serversocket.bind((localhost,server_port))
    serversocket.listen(QUEUE_LENGTH)
    
    # Listen for connections
    while 1:
        (clientsocket, address) = serversocket.accept()
        # If a client connects, run the server() function to start game 
        threading.Thread(target = server, args = (clientsocket)).start()

def game(clientsocket):
    randNum = random.randint(0, 1000)
    guess = -1
    guessCount = 0

    welcome = "Welcome to Guessing Game :)\n Enter a Number From 0-1000.\n"
    clientsocket.send(welcome.encode('ascii'))

    while guess != randNum:
        guessString = "string"
        convertedCorrectly = False
        while convertedCorrectly != True:
            guessString = clientsocket.recv(RECV_BUFFER_SIZE).decode()
            try:
                guess = int(guessString)
                convertedCorrectly = True
            except ValueError:
                convertedCorrectly = False
                error = "Please input a valid number.\n"
                clientsocket.send(error.encode('ascii'))

        guessCount += 1
        if guess == randNum:
            break
        elif guess > randNum:
            tooHigh = "That number is too high. Guess another number!\n"
            clientsocket.send(tooHigh.encode('ascii'))
        else:
            tooLow = "That number is too low. Guess another number!\n"
            clientsocket.send(tooLow.encode('ascii'))
    
    victory = "You Won in " + str(guessCount) + " guesses!\nPlay again? (y/n)\n"
    clientsocket.send(victory.encode('ascii'))

    replay = clientsocket.recv(RECV_BUFFER_SIZE).decode()
    while replay[0] != "y" and replay[0] != "Y" and replay[0] != "n" and replay[0] != "N":
        incorrectReplay = "Please enter either y(replay) or n(exit).\n"
        clientsocket.send(incorrectReplay.encode('ascii'))
        replay = clientsocket.recv(RECV_BUFFER_SIZE).decode()

    if replay == "n" or replay == "N": #PLAYER DOES NOT WANT TO START AGAIN
        return False
    else: # PLAYER WANTS TO START AGAIN
        return True

if __name__ == "__main__":
    main()
        