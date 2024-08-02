import socket
# ? an http request in python
# * The Internet Protocol Standards are published by the Internet Engineering Task Force (IETF).

mysock= socket.socket(socket.AF_INET , socket.SOCK_STREAM)
# * open socket
'''
socket.AF_INET: This specifies the address family. AF_INET is used for IPv4 addresses.
socket.SOCK_STREAM: This specifies the socket type. SOCK_STREAM indicates that the socket is a TCP 
(Transmission Control Protocol) socket, which is a connection-oriented, reliable, stream-based protocol
'''
mysock.connect( ('data.pr4e.org',80)) 
# * address is a tuple
cmd='GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() 
# * GET request method and URL of resource the client wants to retrieve
# * HTTP/1.0 version HTTP protocol being used
# * \r\n\r\n the sequencial of characters, consist of two carriage return and line feed pairs
# * The first \r\n ends the line that contains the request method, URL, and HTTP version
# * The second \r\n is a blank line that indicates the end of the header section and the beginning of the message body. 
mysock.send(cmd)

while True:
    data=mysock.recv(512) # * receive 512 characters
    if(len(data)<1):
        break
    print(data.decode())
mysock.close()