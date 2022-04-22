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
    clientsocket.close()
    pass
    

def main():

    server_port = 15000

    # Create server socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(("127.0.0.1",server_port))
    serversocket.listen(QUEUE_LENGTH)
    
    # Listen for connections
    while 1:
        (clientsocket, address) = serversocket.accept()
        # If a client connects, run the server() function to start game 
        threading.Thread(target = server, args = (clientsocket,)).start()

def game(clientsocket):
    randNum = random.randint(0, 1000)
    guess = -1
    guessCount = 0

    welcome = "Welcome to Guessing Game :)\nEnter a Number From 0-1000."
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
                error = "Please input a valid number."
                clientsocket.send(error.encode('ascii'))

        guessCount += 1
        if guess == randNum:
            break
        elif guess > randNum:
            tooHigh = "That number is too high. Guess another number!"
            clientsocket.send(tooHigh.encode('ascii'))
        else:
            tooLow = "That number is too low. Guess another number!"
            clientsocket.send(tooLow.encode('ascii'))
    
    victory = "You Won in " + str(guessCount) + " guesses!\nPlay again? (y/n)"
    clientsocket.send(victory.encode('ascii'))

    replay = clientsocket.recv(RECV_BUFFER_SIZE).decode()
    while replay[0] != "y" and replay[0] != "Y" and replay[0] != "n" and replay[0] != "N":
        incorrectReplay = "Please enter either y(replay) or n(exit)."
        clientsocket.send(incorrectReplay.encode('ascii'))
        replay = clientsocket.recv(RECV_BUFFER_SIZE).decode()

    if replay == "n" or replay == "N": #PLAYER DOES NOT WANT TO START AGAIN
        goodbye = "Thanks for playing!"
        clientsocket.send(goodbye.encode('ascii'))
        return False
    else: # PLAYER WANTS TO START AGAIN
        return True

if __name__ == "__main__":
    main()
        