
import socket
import struct 

ESP8266AddressPort   = ("192.168.43.18", 8888)
bufferSize          = 1024

# Create a UDP socket at client side
UDPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


while(True):
    msgFromPython = input("Select angle XX (-30 to +30) with sign S and velocity VVV (100 to 900) with the format SXXVVV...")
    #msgFromPython = "Move to 90 deg"
    bytesToSend = str.encode(msgFromPython)
    UDPSocket.sendto(bytesToSend, ESP8266AddressPort)
    # SERVER CODE (receive message):
    print('\nWaiting to receive message...')
    data, address = UDPSocket.recvfrom(1024)                          
    print('Received {} bytes from {}'.format(len(data), address))       
    print('Received data from Arduino is: {}'.format(data))

#####################
