# The  Objectives are:
To practice socket programming by developing a client-server application in Python.
Description:
Download the latest version of Python 3.11.1 for windows and consult the python code
example.
Also read RFC 9110 – HTTP Semantics (https://www.rfc-editor.org/rfc/rfc9110) to understand
the http protocol and its messages. We are most interested in the HTTP Get method.
This is a python program for a client and a proxy server to access http webpages.
My is able to:
- listen on a port of your own choice for incoming connections
- parse the request to get the destination server IP address
- print a message describing this request with the IP and exact time of the request
- send the client's request to the destination server
- print a message with exact time of the actual request
- receive the response from the destination server
- print a message that the response was received with the exact time
- send the response back to the client
- print a message that the response was sent with the exact time
- If there was any error from the client side or from the server side, the proxy server should display a message and return an error message to the client
Also my client is able to:
- take as input the website IP you want to access
- send the request to the proxy server
- print a message with the request details and the exact time sent
- receive the reply back from the proxy server and display it to the user with the exact
time received
- Calculate and display the total round-trip time and your physical (not VM) MAC address.
Assignment will not be accepted without the MAC displayed.
