Resources:

https://www.geeksforgeeks.org/extracting-mac-address-using-python/#:~:text=Method%201%20%3A%20using%20mac%20module,use%20getmac%20module%20of%20Python.&text=Method%202%20%3A%20Using%20uuid.,is%20defined%20in%20uuid%20module.
https://docs.python.org/3/library/time.html


# Networks
#This is the readme file of assignment1 for Networks Course:
#This code follows the below instructions:

# Objective:
# To practice socket programming by developing a client-server application in Python.
# Description:
# Download the latest version of Python 3.11.1 for windows and consult the python code
# example posted on Moodle.
# Also read RFC 9110 – HTTP Semantics (https://www.rfc-editor.org/rfc/rfc9110) to understand
# the http protocol and its messages. We are most interested in the HTTP Get method.
# Write a python program for a client and a proxy server to access http webpages.
# Your server should:
# - listen on a port of your own choice for incoming connections
# - parse the request to get the destination server IP address
# - print a message describing this request with the IP and exact time of the request
# - send the client's request to the destination server
# - print a message with exact time of the actual request
# - receive the response from the destination server
# - print a message that the response was received with the exact time
# - send the response back to the client
# - print a message that the response was sent with the exact time
# - If there was any error from the client side or from the server side, the proxy server
# should display a message and return an error message to the client
# Your client should:
# - take as input the website IP you want to access
# - send the request to the proxy server
# - print a message with the request details and the exact time sent
# - receive the reply back from the proxy server and display it to the user with the exact
# time received
# - Calculate and display the total round-trip time and your physical (not VM) MAC address.
# Assignment will not be accepted without the MAC displayed. 
