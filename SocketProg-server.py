#!/usr/bin/python3
import socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(("127.0.0.1",8888))
print("listening")
server.listen(1)

clientConnection,clientAddr=server.accept()
print("connected")

while True:
	cmd=input("command:")
	if cmd == "exit":
		clientConnection.send(cmd.encode())
		print(clientConnection.recv(1024).decode())
		break
	else:			
		clientConnection.send(cmd.encode())
		print(clientConnection.recv(1024).decode())
server.close()
clientConnection.close()

#this is a simple code on socket program which create a server on 127.0.0.1:8888 and any client
#connecting on this id and port can get a connection. 

	
