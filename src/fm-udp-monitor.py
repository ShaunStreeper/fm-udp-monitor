import socket
import os # For clearing the console as I'm running the file from a powershell window.

def main():
    # Define UDP server address and port to listen on
    UDP_IP = "127.0.0.1"
    UDP_PORT = 53001

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the specified address and port
    sock.bind((UDP_IP, UDP_PORT))

    print("Listening, waiting for data.")

    try:
        while True:
            # Receive data from the socket
            data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes

            # Display the received data
            os.system('cls') # Clear the console.
            print(f"Data: {data}") # Just print the raw data, not useful and need to parse it.

    except KeyboardInterrupt:
        print("\nUDP server stopped.")

    finally:
        # Close the socket when done
        sock.close()

if __name__ == "__main__":
    main()