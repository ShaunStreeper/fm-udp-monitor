# A console app to act as a HUD for some race data that I am trying to use in Forza Motorsport 2023.

import socket
import os # For clearing the console as I'm running the file from a powershell window.
from fdp import ForzaDataPacket

def main():
    # Define UDP server address and port to listen on
    UDP_IP = "127.0.0.1"
    UDP_PORT = 53001

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the specified address and port
    sock.bind((UDP_IP, UDP_PORT))

    os.system('cls') # Clear the console.

    try:
        while True:
            # Receive data from the socket
            data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes

            # Create a ForzaDataPacket object from the received data
            fdpacket = ForzaDataPacket(data)

            # Return the cursor to the top-left of the console.
            print("\033[H", end="")

            # Format the RPM as a 5-character string, right-justified
            rpm_int = int(round(fdpacket.current_engine_rpm))
            rpm_string = str(rpm_int).rjust(5)

            # Format the speed as a 5-character string, right-justified
            speed_int = int(round(fdpacket.speed*3.6))
            speed_string = str(speed_int).rjust(5)

            # Print the desired attributes.
            print(rpm_string + " RPM" + '\n' 
                  + speed_string + " Km/h" + '\n' 
                  + "Gear " + str(fdpacket.gear).rjust(2) + '\n' 
                  + "Lap" + str(fdpacket.lap_no).rjust(4))

    except KeyboardInterrupt:
        print("\nStopped.")

    finally:
        # Close the socket when done
        sock.close()

if __name__ == "__main__":
    main()