# import socket
# import requests
# import time
# import uuid
#
#
# # Client
#
# def client():
#     host = '127.0.0.1'
#     port = 9999
#
#     # Create a socket
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # Connect to server
#     client_socket.connect((host, port))
#
#     # Get the MAC address Formatted way("Got the code for mac address only from https://www.geeksforgeeks.org/extracting-mac-address-using-python/")
#     print("The MAC address in formatted way is : ", end="")
#     print(':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
#                     for ele in range(0, 8 * 6, 8)][::-1]))
#
#     # Unformated way is:
#     mac = uuid.getnode()
#     print("Client MAC address: " + str({mac}))
#
#     # - print a message with the request details and the exact time sent
#     ip = input("Enter the IP address of the website or its url you want to access (for e.g: use 40.127.138.74 for accessing aub.edu.lb): ")
#     # I used this string since it represents an http request using the GET command. The \r\n\r\n is the end of request which r represents
#     # the return and n represents new line. This marker separates http headers.
#     request = "GET http://" + ip + " HTTP/1.0\r\n\r\n"
#     t1 = time.time()
#     client_socket.sendall(request.encode('utf-8'))
#     print(str([{time.ctime()}]), "Request sent:", str({request}))
#
#     # receive the reply back from the proxy server and display it to the user with the exact
#     # time received:
#
#     response = client_socket.recv(4096)
#     t2 = time.time()
#
#     # Decode the response:
#
#     decoded_response = response.decode('utf-8')
#
#     print(str([{time.ctime()}]), "Response received: " + str({decoded_response}))
#
#     # RoundTripTime
#     rtt = t2 - t1
#     print("The round trip time is: " + str(rtt))
#
# client()