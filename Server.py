# import socket
# import requests
# import time
# import uuid
#
#
# # Proxy Server
#
#
# def server():
#     host = '127.0.0.1'
#     port = 9999
#     # listen on a port of your own choice for incoming connections
#     # Create a socket
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # Bind a socket
#     server_socket.bind((host, port))
#     # Listen on socket
#     server_socket.listen()
#     print("Proxy server listening on", str(host) + ":" + str(port))
#
#     # Create a while loop to always be ready to accept
#     while True:
#         client_socket, client_address = server_socket.accept()
#         print("Accepted connection from client address: " + str({client_address[0]}))
#
#         # Receive request
#         request = client_socket.recv(1024).decode('utf-8')
#         print(str([{time.ctime()}]) + "Request received: " + str({request}),  "from: " + str(client_address))
#
#         # Use the IP address provided by the user
#         ip = request.split()[1]
#
#         # Make the request to the target website using the `requests` library
#         try:
#             print(str([{time.ctime()}]), "Sending request to", str({ip}))
#             response = requests.get(ip)
#             print(str([{time.ctime()}]) + "Response received from", str({ip}))
#         except Exception as e:
#             print(str([{time.ctime()}]), "Error: " + str({e}))
#             # I used the "b" prefix indicates that the string should be stored as a sequence of bytes, rather than a text string.
#             client_socket.sendall(b" HTTP Server Error")
#             client_socket.close()
#             continue
#
#         # Send the response
#         client_socket.sendall(response.content)
#         print(str([{time.ctime()}]), "Response sent to the client")
#         client_socket.close()
#
# server()