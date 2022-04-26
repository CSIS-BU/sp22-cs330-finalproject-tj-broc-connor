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

# Main logic for the game
def game(clientsocket):
    #Generate a random number and instantiate necessary variables
    randNum = random.randint(0, 1000)
    guess = -1
    guessCount = 0

    # Send welcome message
    welcome = "Welcome to Guessing Game :)\nEnter a Number From 0-1000."
    clientsocket.send(welcome.encode('ascii'))

    # Main gameplay loop while the number hasn't been guessed
    while guess != randNum:
        # Initialize loop variables
        guessString = "string"
        convertedCorrectly = False

        # 
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

    if replay == "n" or replay == "N": #Player enters n or N, and the game stops
        goodbye = "Thanks for playing!"
        clientsocket.send(goodbye.encode('ascii'))
        return False
    else: #Player enters y or Y, and the game repeats
        return True

if __name__ == "__main__":
    main()
        