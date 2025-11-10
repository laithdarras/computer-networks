# tcp_client.py
# Author: Laith Darras
# Description:
#   Opens a TCP connection to www.ucmerced.edu on port 80,
#   sends an HTTP GET request, receives the response, and prints it.
#
# How to run:
#   python tcp_client.py
#
# Requirements:
#   Python 3.x (no external libraries needed)


import socket

client = socket.socket() # create the socket endpoint

client.connect(("www.ucmerced.edu", 80)) # Connect to server

request = "GET / HTTP/1.1\r\nHost: www.ucmerced.edu:80\r\nConnection: close\r\n\r\n"
client.send(request.encode())  # Send request to connected socket

response = client.recv(4096)
print(response.decode(errors="ignore"))  # Receives data from the connection with a buffer size of 4KB

client.close() # close connection