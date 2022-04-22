import sys 
import socket 
 
SEND_BUFFER_SIZE = 2048 
 
def client(server_ip, server_port): 
    # create an INET, STREAMing socket 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
        # now connect to server 
        s.connect((server_ip, server_port)) 
         
        #Game Logic Here
        #Some sort of intro needed, response 1 here (play or not)

        answer = s.recv(1024)
        print(answer.decode('ascii'))


        playing = 1
        while playing: 
            
            #Input for number
            guess = input("Input your guess: ")
            s.send(guess.encode('ascii'))
            
            #Logic for figuring out if guess is correct
            response = s.recv(1024).decode('ascii')
	        print (response)

            #If guess was correct play again?
            #If guess is wrong input another number
            if(response == "Thanks for playing!\r\n")
                playing = 0
        s.close()
    pass 
 
 
def main(): 
    """Parse command-line arguments and call client function """ 
    if len(sys.argv) != 2: 
        sys.exit("Usage: python3 client.py [Server IP] ") 
    server_ip = sys.argv[1] 
    server_port = 15000
    client(server_ip, server_port) 
 
if __name__ == "__main__": 
    main() 
        