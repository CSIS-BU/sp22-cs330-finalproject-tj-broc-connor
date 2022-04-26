import sys 
import socket 
 
SEND_BUFFER_SIZE = 2048 
 
def client(server_ip, server_port): 
    # create an INET, STREAMing socket 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
        # now connect to server 
        s.connect((server_ip, server_port)) 

        answer = s.recv(1024)
        print(answer.decode('ascii'))

        playing = 1
        while playing: 
            
            #Input for number and send to server
            guess = input("")
            s.send(guess.encode('ascii'))
            
            #Get response from server and print
            response = s.recv(1024).decode('ascii')
            print(response)

            #If server sends game ending response, exit
            if(response == "Thanks for playing!"):
                playing = 0
        s.close()
    pass 
 
 
def main(): 
    """Parse command-line arguments and call client function """ 
    if len(sys.argv) != 2: 
        sys.exit("Usage: python3 client.py [Server IP]") 
    server_ip = sys.argv[1] 
    server_port = 15000
    client(server_ip, server_port) 
 
if __name__ == "__main__": 
    main() 
        